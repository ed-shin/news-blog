#!/usr/bin/env python3
"""일일 글 1면 지표를 공식 자료와 맞춰 본다.

    python3 scripts/market_check.py src/content/blog/2026-10-07-daily.md [...]
    python3 scripts/market_check.py -v src/content/blog/2026-10-07-daily.md    # 공식 값도 함께 보기

기사는 틀리기도 하고, 같은 등락을 기사마다 다른 기준으로 셈하기도 한다(10/7 원/달러 -0.4원 대 -7.0원).
그래서 공식 자료가 있는 네 지표는 이 스크립트로 값과 등락을 다시 본다. 출처는 scripts/official.py.

| 1면 지표 | 공식 자료 | 다르면 |
|---|---|---|
| 코스피 | 한국은행 ECOS 코스피 종가 | 오류 |
| 원/달러 | 한국은행 ECOS 원/달러 종가(15:30) | 오류 |
| S&P 500 | FRED SP500 | 오류 |
| 미 10년물 | 미 재무부 일별 고시 | 경고(기사 마감 값과 고시 값은 0.01%p 안팎 다를 수 있다) |

브렌트·WTI·금 정산가는 무료 공식 자료가 없어 기사 대조로 둔다.

아침 발행 때는 전날 값이 아직 안 올라온 자료가 있다(ECOS 코스피, FRED는 하루 늦다). 그때는 '확인하지
못함'으로 알리고 넘어간다. 증시가 쉰 날도 공식 자료에 값이 없다. 원/달러는 2026-07-06부터 공휴일에도
거래하므로(토·일·1월 1일만 쉰다) 증시가 쉰 날에도 종가가 있다.

오류가 있으면 종료 코드 1.
"""
import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import official  # noqa: E402

CHECKS = [            # 1면 이름, 자료, 등락 형식, 다를 때
    ('코스피', 'kospi', 'pct', 'error'),
    ('원/달러', 'usdkrw', 'diff', 'error'),
    ('S&P 500', 'sp500', 'pct', 'error'),
    ('미 10년물', 'us10y', 'pp', 'warn'),
]
TOL = {'kospi': 0.005, 'usdkrw': 0.05, 'sp500': 0.005, 'us10y': 0.015}
CHANGE_TOL = {'pct': 0.015, 'diff': 0.05, 'pp': 0.015}

errors, warnings = [], []


def num(s):
    m = re.search(r'-?[\d,]+(?:\.\d+)?', s or '')
    return float(m.group(0).replace(',', '')) if m else None


def change_num(s):
    """'+0.58%' '-0.4' '-0.04%p' '+5bp' → 숫자(bp는 %p로)"""
    s = (s or '').strip()
    if not s:
        return None
    v = num(s.replace('+', ''))
    if v is None:
        return None
    if s.startswith('-') and v > 0:
        v = -v
    return v / 100 if 'bp' in s else v


def front(path):
    text = Path(path).read_text(encoding='utf-8')
    fm = text.split('---')[1]
    pub = re.search(r'^pubDate:\s*(\S+)', fm, re.M)
    tags = re.search(r'^tags:\s*\[(.*)\]', fm, re.M)
    rows = {name: (val, change or '') for name, val, change in re.findall(
        r'-\s*\{\s*name:\s*"([^"]+)",\s*value:\s*"([^"]*)"(?:,\s*change:\s*"([^"]*)")?\s*\}', fm)}
    return (date.fromisoformat(pub.group(1)) if pub else None), (tags.group(1) if tags else ''), rows


def last_weekday(d):
    d -= timedelta(days=1)
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    return d


def series(key, start, end):
    if key in ('kospi', 'usdkrw'):
        return official.ecos(key, start, end)
    if key == 'sp500':
        return official.fred('SP500', start, end)
    out = {}
    for y in range(start.year, end.year + 1):
        out.update({d: v for d, v in official.treasury_10y(y).items() if start <= d <= end})
    return out


def fmt(key, v):
    return {'kospi': f'{v:,.2f}', 'usdkrw': f'{v:,.1f}', 'sp500': f'{v:,.2f}', 'us10y': f'{v:.2f}%'}[key]


def computed_change(kind, v0, v1):
    return round((v1 / v0 - 1) * 100, 2) if kind == 'pct' else round(v1 - v0, 2 if kind == 'pp' else 1)


def check(path, verbose):
    pub, tags, rows = front(path)
    if not pub or '"일일"' not in tags:
        return
    weekend = pub.weekday() in (6, 0)           # 일요일·월요일판은 등락을 비운다
    expected = last_weekday(pub)                # 이 판이 실어야 할 마지막 거래일(공휴일은 따로 본다)
    start = pub - timedelta(days=14)
    tag = Path(path).name

    def say(level, msg):
        (errors if level == 'error' else warnings).append(f'{tag}: {msg}')

    for name, key, kind, level in CHECKS:
        if name not in rows:
            continue
        value, change = rows[name]
        try:
            obs = sorted(series(key, start, pub - timedelta(days=1)).items())
        except Exception as e:                  # 네트워크·키 문제는 글의 오류가 아니다
            warnings.append(f'{tag}: {name} 공식 자료를 읽지 못했다({e})')
            continue
        if len(obs) < 2:
            warnings.append(f'{tag}: {name} 공식 자료가 모자라 확인하지 못했다')
            continue
        (d0, v0), (d1, v1) = obs[-2], obs[-1]
        cc = computed_change(kind, v0, v1)
        if verbose:
            print(f'  {tag} {name}: 공식 {d1:%m/%d} {fmt(key, v1)} (전 거래일 {d0:%m/%d} {fmt(key, v0)}, 등락 {cc:+})')

        pv = num(value)
        if '—' in value or pv is None:
            say('warn', f'{name}이 비어 있는데 공식 자료에는 {d1:%m/%d} {fmt(key, v1)}이 있다')
            continue
        if '~' in value or '장중' in value:     # 범위·장중 값은 기준을 밝혀 실은 것이라 값만 넘어간다
            continue

        stale = d1 < expected and not (key == 'usdkrw' and expected.month == 1 and expected.day == 1)
        if stale and abs(pv - v1) > TOL[key]:
            # 공식 자료에 마지막 거래일 값이 아직 없다(늦게 올라오거나 증시 휴장). 글의 값을 확인할 수 없다
            warnings.append(f'{tag}: {name} {value}는 확인하지 못함 — 공식 자료의 마지막 값이 {d1:%m/%d}({fmt(key, v1)})다. '
                            f'{expected:%m/%d} 값이 아직 안 올라왔거나 그날 휴장이다')
            continue
        if abs(pv - v1) > TOL[key]:
            say(level, f'{name} 값 {value}가 공식 자료({d1:%m/%d} {fmt(key, v1)})와 다르다')
            continue

        pc = change_num(change)
        if weekend:
            if pc is not None:
                say('warn', f'{name}: 일요일·월요일판은 등락을 비운다(지금 {change})')
            continue
        if pc is None:
            if not stale:
                say('warn', f'{name}: {d1:%m/%d} 새 종가가 있는데 등락이 비었다(공식 {cc:+}, 전 거래일 {d0:%m/%d})')
            continue
        if stale:
            continue
        if kind == 'pct' and re.search(r'\dp$', change.strip()):     # '-0.06p'처럼 포인트로 적은 등락
            kind, cc = 'points', round(v1 - v0, 2)
        if abs(pc - cc) > CHANGE_TOL.get(kind, 0.015):
            say(level, f'{name} 등락 {change}가 공식 자료와 다르다 — {d0:%m/%d} {fmt(key, v0)} → '
                       f'{d1:%m/%d} {fmt(key, v1)}, {cc:+}')


def main():
    args = [a for a in sys.argv[1:] if a != '-v']
    if not args:
        print(__doc__)
        sys.exit(2)
    if official.ecos_key() == 'sample':
        warnings.append('ECOS_API_KEY가 없어 ECOS 시험용 공개 키로 읽었다')
    for p in args:
        check(p, '-v' in sys.argv)
    for e in errors:
        print('오류:', e)
    for w in warnings:
        print('경고:', w)
    print(f'\n오류 {len(errors)}건, 경고 {len(warnings)}건')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
