#!/usr/bin/env python3
"""주간 흐름의 고정 차트(네 지표의 한 주)를 그 주 일일 글에서 뽑아 그린다.

    python3 scripts/weekly_data.py 2026-09-21            # 값 표만 보기 (월요일 날짜)
    python3 scripts/weekly_data.py 2026-09-21 --chart    # 글에 붙일 차트 SVG
    python3 scripts/weekly_data.py 2026-09-21 --chart --gap-note "추석 휴장"   # 빈 구간 이름

값을 손으로 옮기면 틀리기 쉽다. 이 스크립트는 이미 검증을 거쳐 실린 일일 글의 1면 지표를
그대로 읽는다. 기준은 이렇다.

- 거래일 T의 마감은 다음 날(T+1) 일일 글의 1면 지표에 있다. 월~금 마감 → 화~토 일일.
  기준선은 지난주 금요일 마감(지난주 토요일 일일)이다.
- 1면 지표의 등락(change)이 비어 있으면 그날 새 마감이 없는 것(휴장)으로 보고 비운다.
  휴장일에도 1면에는 직전 거래일 값을 이어 싣기 때문에, 값만 보면 휴장인지 알 수 없다.
- 미 10년물은 1면 값을 쓰지 않는다. 기사마다 종가·장중이 섞여 한 선으로 이을 수 없어서다.
  미 재무부 일별 자료(세인트루이스 연은 FRED, DGS10)를 받아 쓴다.
- 브렌트유 계약 월물은 본문 "오늘의 숫자" 표에서 읽는다. 주중에 월물이 바뀌면 캡션에 밝힌다.
"""
import re
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import chart  # noqa: E402

BLOG = Path(__file__).resolve().parent.parent / 'src' / 'content' / 'blog'
DAYS = '월화수목금토일'
ROWS = {'브렌트': 'brent', '원/달러': 'usdkrw', '코스피': 'kospi'}


def num(s):
    m = re.search(r'-?[\d,]+(?:\.\d+)?', s or '')
    return float(m.group(0).replace(',', '')) if m else None


def front_rows(d):
    """d일 일일 글의 1면 지표 → {'brent': (값, 등락), ...}, 브렌트 월물"""
    f = BLOG / f'{d.isoformat()}-daily.md'
    if not f.exists():
        return None, None
    text = f.read_text(encoding='utf-8')
    rows = {}
    for name, val, change in re.findall(
            r'-\s*\{\s*name:\s*"([^"]+)",\s*value:\s*"([^"]*)"(?:,\s*change:\s*"([^"]*)")?\s*\}', text):
        key = ROWS.get(name)
        if key:
            rows[key] = (num(val), change or '')
    month = re.search(r'^\|\s*브렌트[^|]*?\((\d+)월물\)', text, re.M)
    return rows, (month.group(1) if month else None)


def fred_dgs10(start, end):
    url = f'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10&cosd={start}&coed={end}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        lines = r.read().decode().strip().splitlines()[1:]
    out = {}
    for line in lines:
        d, v = line.split(',')
        out[d] = float(v) if v not in ('.', '') else None
    return out


def collect(monday):
    days = [monday - timedelta(days=3)] + [monday + timedelta(days=i) for i in range(5)]  # 지난 금 + 월~금
    labels = [f'{d.month}/{d.day}' for d in days]
    series = {k: [] for k in ROWS.values()}
    base = {}                               # 기준일(지난 금)이 휴장인 지표의 그 전 마지막 마감
    months, missing = [], []
    for d in days:
        rows, month = front_rows(d + timedelta(days=1))
        if rows is None:
            missing.append(f'{d + timedelta(days=1)} 일일 글이 없다')
            for k in series:
                series[k].append(None)
            continue
        months.append(month)
        for k in series:
            v, change = rows.get(k, (None, ''))
            # 등락이 비면 그날 새 마감이 없다(휴장). 1면이 이어 실은 직전 값이라 선에 넣지 않는다
            series[k].append(v if change else None)
            if d == days[0] and not change and v is not None:
                base[k] = v                 # 이어 실은 값 = 그 전 마지막 마감. 기준선으로만 쓴다
    fred = fred_dgs10((days[0] - timedelta(days=10)).isoformat(), days[-1].isoformat())
    series['us10y'] = [fred.get(d.isoformat()) for d in days]
    if series['us10y'][0] is None:
        before = [v for k, v in sorted(fred.items()) if k < days[0].isoformat() and v is not None]
        if before:
            base['us10y'] = before[-1]
    return days, labels, series, base, [m for m in months if m], missing


def span(days, vals):
    """None인 날들을 'M/D~M/D'로"""
    gone = [d for d, v in zip(days, vals) if v is None]
    if not gone:
        return ''
    a, b = gone[0], gone[-1]
    return f'{a.month}/{a.day}' + (f'~{b.month}/{b.day}' if b != a else '')


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    monday = date.fromisoformat(sys.argv[1])
    if monday.weekday() != 0:
        sys.exit(f'{monday}는 월요일이 아니다')
    days, labels, s, base, months, missing = collect(monday)
    today = datetime.now(timezone(timedelta(hours=9))).date()

    if '--chart' not in sys.argv:
        print('날짜      ' + '  '.join(f'{l:>9}' for l in labels))
        for name, key in [('미 10년물', 'us10y'), ('브렌트', 'brent'), ('원/달러', 'usdkrw'), ('코스피', 'kospi')]:
            print(f'{name:8}' + '  '.join(f'{("—" if v is None else f"{v:,.2f}"):>9}' for v in s[key]))
        print(f'브렌트 월물: {sorted(set(months))}')
        for k, v in base.items():
            print(f'기준일 휴장 → 그 전 마지막 마감을 기준선으로: {k} {v:,.2f}')
        for m in missing:
            print('주의:', m)
        return

    if missing:
        sys.exit('일일 글이 빠져 차트를 그리지 않는다: ' + ', '.join(missing))
    fri, mon = days[0], days[1]
    month_note = (f'{months[0]}월물' if len(set(months)) == 1
                  else f'근월물(주중 {"→".join(sorted(set(months), key=months.index))}월물로 바뀜)')
    kr_gap = span(days, s['usdkrw'])
    us_gap = span(days, s['us10y'])
    notes = []
    if kr_gap:
        notes.append(f'국내는 {kr_gap} 휴장이었다')
    if us_gap:
        notes.append(f'미국은 {us_gap} 휴장이었다')
    fmt = {'us10y': lambda v: f'{v:.2f}%', 'brent': lambda v: f'{v:.2f}',
           'usdkrw': lambda v: f'{v:,.1f}', 'kospi': lambda v: f'{v:,.2f}'}
    panels = [(n, fmt[k], s[k], base.get(k)) for n, k in
              [('미 10년물 금리', 'us10y'), ('브렌트유 (달러)', 'brent'), ('원/달러 (원)', 'usdkrw'), ('코스피', 'kospi')]]
    if base:
        notes.append('기준일이 휴장이던 지표는 그 전 마지막 마감을 점선으로 그었다')
    caption = (f'{mon.month}월 {mon.day}~{days[-1].day}일 네 지표. 점선은 지난주 금요일({fri.month}/{fri.day}) 값이다. '
               f'칸마다 축이 따로다. 미 10년물은 미 재무부 일별 자료(세인트루이스 연은 FRED, '
               f'{today.year}년 {today.month}월 {today.day}일 조회), 브렌트유는 {month_note} 정산가, '
               f'원/달러는 서울 외환시장 오후 3시 30분 종가, 코스피는 종가다.'
               + (' ' + '. '.join(notes) + '.' if notes else ''))
    def said(name, key):
        known = [(l, v) for l, v in zip(labels, s[key]) if v is not None]
        return f'{name}는 {fmt[key](known[0][1])}에서 {fmt[key](known[-1][1])}로' if known else f'{name}는 값 없음'
    alt = (f'{fri.month}월 {fri.day}일부터 {days[-1].month}월 {days[-1].day}일까지 네 지표. '
           + ', '.join(said(n, k) for n, k in [('미 10년물', 'us10y'), ('브렌트유', 'brent'),
                                                ('원/달러', 'usdkrw'), ('코스피', 'kospi')]) + ' 움직였다.')
    gap = sys.argv[sys.argv.index('--gap-note') + 1] if '--gap-note' in sys.argv else '휴장'
    print(chart.small_multiples(panels, labels, caption, alt, gap_note=gap))


if __name__ == '__main__':
    main()
