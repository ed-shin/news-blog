"""공식 자료에서 시장 수치를 읽는다. 기사 값을 대조하거나(market_check.py) 주간 차트를 그릴 때(weekly_data.py) 쓴다.

- 원/달러 오후 3시 30분 종가, 코스피 종가: 한국은행 경제통계시스템(ECOS) Open API.
  인증키는 환경 변수 ECOS_API_KEY, 없으면 저장소 루트의 .env(.gitignore에 있어 커밋되지 않는다)에서 읽는다.
  클라우드 루틴은 저장소를 새로 받아 .env가 없으니 루틴 환경 변수로 넣는다.
  둘 다 없으면 ECOS의 시험용 공개 키(sample)를 쓴다. sample은 한 번에 10건까지라 날짜를 잘라 여러 번 부른다.
- 미 10년물: 미 재무부 일별 수익률 곡선(그날 저녁에 올라온다), FRED DGS10(하루 늦다).
- S&P 500: FRED SP500. 하루 늦게 올라와 아침 발행 때는 전날 값이 아직 없을 수 있다.

서울 외환시장은 2026-07-06부터 24시간 열리고 토·일·1월 1일만 쉰다. 추석·대체공휴일처럼 증시가 쉬는
날에도 원/달러 종가가 있다. 휴장은 코스피에만 생긴다.
"""
import json
import os
import urllib.request
from datetime import date, timedelta
from pathlib import Path

ECOS = {
    'usdkrw': ('731Y003', '0000003'),   # 원/달러(종가 15:30)
    'kospi': ('802Y001', '0001000'),    # KOSPI지수
}
_cache = {}


def ecos_key():
    key = os.environ.get('ECOS_API_KEY', '').strip()
    env = Path(__file__).resolve().parent.parent / '.env'
    if not key and env.exists():
        for line in env.read_text(encoding='utf-8').splitlines():
            if line.strip().startswith('ECOS_API_KEY='):
                key = line.split('=', 1)[1].strip().strip('"\'')
    return key or 'sample'


def _get(url):
    # User-Agent를 따로 달면 FRED가 연결을 끊는 일이 있었다(2026-10-03). 기본값으로 둔다
    with urllib.request.urlopen(urllib.request.Request(url), timeout=30) as r:
        return r.read().decode('utf-8')


def ecos(name, start, end):
    """ECOS 일별 계열 → {date: 값}. start~end는 date. 값이 없는 날(주말·휴장)은 빠진다."""
    stat, item = ECOS[name]
    key = ecos_key()
    step = timedelta(days=9) if key == 'sample' else timedelta(days=3650)
    out, a = {}, start
    while a <= end:
        b = min(a + step, end)
        ck = (name, a, b)
        if ck not in _cache:
            n = 10 if key == 'sample' else 1000
            url = (f'https://ecos.bok.or.kr/api/StatisticSearch/{key}/json/kr/1/{n}/{stat}/D/'
                   f'{a:%Y%m%d}/{b:%Y%m%d}/{item}')
            data = json.loads(_get(url))
            rows = data.get('StatisticSearch', {}).get('row', [])
            if not rows and data.get('RESULT', {}).get('CODE') not in (None, 'INFO-200'):
                raise RuntimeError(f"ECOS {name}: {data['RESULT'].get('MESSAGE', '')[:80]}")
            _cache[ck] = {date(int(r['TIME'][:4]), int(r['TIME'][4:6]), int(r['TIME'][6:])): float(r['DATA_VALUE'])
                          for r in rows}
        out.update(_cache[ck])
        a = b + timedelta(days=1)
    return out


def ecos_link(name, start, end):
    """글에 근거로 다는 고정 주소(시험용 공개 키). 열면 그 기간의 값이 그대로 나온다."""
    stat, item = ECOS[name]
    return (f'https://ecos.bok.or.kr/api/StatisticSearch/sample/json/kr/1/10/{stat}/D/'
            f'{start:%Y%m%d}/{end:%Y%m%d}/{item}')


def fred(series, start, end):
    """FRED 일별 계열 → {date: 값}"""
    ck = ('fred', series, start, end)
    if ck not in _cache:
        text = _get(f'https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}&cosd={start}&coed={end}')
        out = {}
        for line in text.strip().splitlines()[1:]:
            d, v = line.split(',')
            if v not in ('.', ''):
                out[date.fromisoformat(d)] = float(v)
        _cache[ck] = out
    return _cache[ck]


def treasury_10y(year):
    """미 재무부 일별 수익률 곡선의 10년 만기 → {date: 값}"""
    ck = ('tsy', year)
    if ck not in _cache:
        text = _get('https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/'
                    f'{year}/all?type=daily_treasury_yield_curve&field_tdr_date_value={year}&page&_format=csv')
        lines = text.strip().splitlines()
        head = [h.strip('"') for h in lines[0].split(',')]
        i = head.index('10 Yr')
        out = {}
        for line in lines[1:]:
            cells = line.split(',')
            m, d, y = cells[0].split('/')
            if cells[i]:
                out[date(int(y), int(m), int(d))] = float(cells[i])
        _cache[ck] = out
    return _cache[ck]
