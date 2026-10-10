#!/usr/bin/env python3
"""주간 흐름의 고정 차트(네 지표의 한 주)를 그 주 일일 글에서 뽑아 그린다.

    python3 scripts/weekly_data.py 2026-09-21            # 값 표만 보기 (월요일 날짜)
    python3 scripts/weekly_data.py 2026-09-21 --chart    # 글에 붙일 차트 SVG
    python3 scripts/weekly_data.py 2026-09-21 --chart --gap-note "추석 휴장"   # 빈 구간 이름

값을 손으로 옮기면 틀리기 쉽다. 이 스크립트는 공식 자료와, 이미 검증을 거쳐 실린 일일 글의 1면 지표를
읽는다(공식 자료는 scripts/official.py). 기준은 이렇다.

- 원/달러(오후 3시 30분 종가)와 코스피(종가)는 한국은행 ECOS에서 읽는다. 값이 없는 날이 휴장이다.
  서울 외환시장은 2026-07-06부터 공휴일에도 열려 추석에도 원/달러 종가가 있다. 일일 글이 이 날들을
  휴장으로 처리했던 일이 있어(9/25·9/26·10/6) 글보다 공식 자료를 먼저 본다. ECOS를 읽지 못하면 일일 글로 돌아간다.
- 브렌트는 일일 글에서 읽는다. 거래일 T의 마감은 다음 날(T+1) 일일 글의 1면 지표에 있다. 월~금 마감 → 화~토 일일.
  기준선은 지난주 금요일 마감(지난주 토요일 일일)이다.
- 일일 글의 1면 등락(change)이 비어 있으면 그날 새 마감이 없는 것(휴장)으로 보고 비운다.
  휴장일에도 1면에는 직전 거래일 값을 이어 싣기 때문에, 값만 보면 휴장인지 알 수 없다.
- 미 10년물은 1면 값을 쓰지 않는다. 기사마다 종가·장중이 섞여 한 선으로 이을 수 없어서다.
  미 재무부 일별 자료(세인트루이스 연은 FRED, DGS10)를 받아 쓴다. FRED는 하루 늦게 올라오므로
  토요일에 돌면 금요일 값이 없다. 그날만 재무부 사이트의 같은 자료(10년 만기 수익률)로 채우고 캡션에 밝힌다.
  재무부 자료에도 없는 날만 휴장으로 본다.
- 브렌트유 계약 월물은 본문 "오늘의 숫자" 표에서 읽는다. 주중에 월물이 바뀌면(근월물 교체) 두 월물
  값을 잇지 않고 선을 끊는다. 바뀐 날의 1면 값과 등락(새 월물 기준)으로 새 월물의 전날 값을 셈해
  새 선을 거기서 시작하고, 캡션에 밝힌다. 그냥 이으면 오른 날이 내린 것처럼 그려진다(10/1 12월물 교체).
"""
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import chart  # noqa: E402
import official  # noqa: E402

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


def collect(monday):
    days = [monday - timedelta(days=3)] + [monday + timedelta(days=i) for i in range(5)]  # 지난 금 + 월~금
    labels = [f'{d.month}/{d.day}' for d in days]
    series = {k: [] for k in ROWS.values()}
    base = {}                               # 기준일(지난 금)이 휴장인 지표의 그 전 마지막 마감
    months, missing = [], []
    day_month, brent_change = [], []        # 날마다 브렌트 월물과 1면 등락(근월물 교체를 찾는 데 쓴다)
    for d in days:
        rows, month = front_rows(d + timedelta(days=1))
        if rows is None:
            missing.append(f'{d + timedelta(days=1)} 일일 글이 없다')
            for k in series:
                series[k].append(None)
            day_month.append(None)
            brent_change.append('')
            continue
        months.append(month)
        day_month.append(month)
        brent_change.append(rows.get('brent', (None, ''))[1])
        for k in series:
            v, change = rows.get(k, (None, ''))
            # 등락이 비면 그날 새 마감이 없다(휴장). 1면이 이어 실은 직전 값이라 선에 넣지 않는다
            series[k].append(v if change else None)
            if d == days[0] and not change and v is not None:
                base[k] = v                 # 이어 실은 값 = 그 전 마지막 마감. 기준선으로만 쓴다
    for k in ('usdkrw', 'kospi'):               # 원/달러·코스피는 공식 자료가 먼저다
        try:
            obs = official.ecos(k, days[0] - timedelta(days=10), days[-1])
        except Exception as e:
            print(f'주의: ECOS {k}를 읽지 못해 일일 글 값을 쓴다({e})', file=sys.stderr)
            continue
        series[k] = [obs.get(d) for d in days]
        base.pop(k, None)
        if series[k][0] is None:
            before = [v for d, v in sorted(obs.items()) if d < days[0]]
            if before:
                base[k] = before[-1]
    fred = {d.isoformat(): v for d, v in
            official.fred('DGS10', days[0] - timedelta(days=10), days[-1]).items()}
    series['us10y'] = [fred.get(d.isoformat()) for d in days]
    late = [d for d, v in zip(days, series['us10y']) if v is None and d.isoformat() > max(fred, default='')]
    if late:                                # FRED에 아직 안 올라온 날 → 재무부 자료로 채운다
        tsy = official.treasury_10y(late[-1].year)
        for i, d in enumerate(days):
            if d in late and tsy.get(d) is not None:
                series['us10y'][i] = tsy[d]
                series.setdefault('_tsy', []).append(d)
    if series['us10y'][0] is None:
        before = [v for k, v in sorted(fred.items()) if k < days[0].isoformat() and v is not None]
        if before:
            base['us10y'] = before[-1]
    # 근월물 교체: 월물이 바뀐 날의 등락은 새 월물끼리 비교한 값이다. 그 날 값을 등락으로 되돌려
    # 새 월물의 전날 값을 얻는다(예: 10/1 12월물 102.31, +4.37% → 9/30 12월물 98.03)
    roll = None
    for k in range(1, len(days)):
        a, b, v, ch = day_month[k - 1], day_month[k], series['brent'][k], brent_change[k].strip()
        if a and b and a != b and v is not None and ch.endswith('%'):
            roll = {'at': k, 'from': round(v / (1 + num(ch) / 100), 2), 'label': f'{b}월물', 'prev_label': f'{a}월물'}
            break
    return days, labels, series, base, [m for m in months if m], missing, roll


def josa(word, a, b):
    """받침이 있으면 a, 없으면 b (은/는)"""
    c = word[-1]
    if '가' <= c <= '힣':
        return a if (ord(c) - 0xAC00) % 28 else b
    return a if c in '0136789lmnr' else b


def span(days, vals):
    """None인 날들을 'M/D~M/D'로. 떨어진 휴장은 'M/D, M/D'로 따로 적는다(10/5·10/9 사이를 잇지 않게)"""
    runs, prev = [], False
    for d, v in zip(days, vals):
        if v is None:
            if prev:
                runs[-1][1] = d
            else:
                runs.append([d, d])
        prev = v is None
    return ', '.join(f'{a.month}/{a.day}' + (f'~{b.month}/{b.day}' if b != a else '') for a, b in runs)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    monday = date.fromisoformat(sys.argv[1])
    if monday.weekday() != 0:
        sys.exit(f'{monday}는 월요일이 아니다')
    days, labels, s, base, months, missing, roll = collect(monday)
    today = datetime.now(timezone(timedelta(hours=9))).date()

    if '--chart' not in sys.argv:
        print('날짜      ' + '  '.join(f'{l:>9}' for l in labels))
        for name, key in [('미 10년물', 'us10y'), ('브렌트', 'brent'), ('원/달러', 'usdkrw'), ('코스피', 'kospi')]:
            print(f'{name:8}' + '  '.join(f'{("—" if v is None else f"{v:,.2f}"):>9}' for v in s[key]))
        print(f'브렌트 월물: {sorted(set(months))}')
        for d in s.get('_tsy', []):
            print(f'미 10년물 {d.month}/{d.day}: FRED에 아직 없어 재무부 사이트 자료로 채웠다')
        if roll:
            print(f'근월물 교체: {labels[roll["at"]]}부터 {roll["label"]}. 선을 끊고, '
                  f'{labels[roll["at"] - 1]} {roll["label"]} 값 {roll["from"]:,.2f}(그날 값과 등락으로 셈)에서 새 선을 시작한다')
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
    kr_gap = span(days, s['kospi'])         # 원/달러는 공휴일에도 열리니 국내 휴장은 코스피로 본다
    us_gap = span(days, s['us10y'])
    notes = []
    if kr_gap:
        notes.append(f'국내 증시는 {kr_gap} 휴장이었다')
    if us_gap:
        notes.append(f'미국은 {us_gap} 휴장이었다')
    fmt = {'us10y': lambda v: f'{v:.2f}%', 'brent': lambda v: f'{v:.2f}',
           'usdkrw': lambda v: f'{v:,.1f}', 'kospi': lambda v: f'{v:,.2f}'}
    panels = [(n, fmt[k], s[k], base.get(k), roll if k == 'brent' else None) for n, k in
              [('미 10년물 금리', 'us10y'), ('브렌트유 (달러)', 'brent'), ('원/달러 (원)', 'usdkrw'), ('코스피', 'kospi')]]
    if base:
        notes.append('기준일이 휴장이던 지표는 그 전 마지막 마감을 점선으로 그었다')
    if roll:
        k = roll['at']
        notes.append(f'브렌트유는 {labels[k]}부터 {roll["label"]}이라 그 앞뒤 선을 잇지 않았다. '
                     f'{roll["label"]} 선의 첫 점은 {labels[k - 1]}의 {roll["label"]} 값({roll["from"]:.2f})이다')
    period = (f'{mon.month}월 {mon.day}~{days[-1].day}일' if days[-1].month == mon.month
              else f'{mon.month}월 {mon.day}일~{days[-1].month}월 {days[-1].day}일')
    tsy = s.get('_tsy', [])
    tsy_note = (f', {", ".join(f"{d.month}/{d.day}" for d in tsy)} 값은 FRED에 아직 없어 재무부 사이트'
                if tsy else '')
    caption = (f'{period} 네 지표. 점선은 지난주 금요일({fri.month}/{fri.day}) 값이다. '
               f'칸마다 축이 따로다. 미 10년물은 미 재무부 일별 자료(세인트루이스 연은 FRED{tsy_note}, '
               f'{today.year}년 {today.month}월 {today.day}일 조회), 브렌트유는 {month_note} 정산가, '
               f'원/달러는 서울 외환시장 오후 3시 30분 종가, 코스피는 종가(둘 다 한국은행 경제통계시스템)다.'
               + (' ' + '. '.join(notes) + '.' if notes else ''))
    def said(name, key):
        known = [(l, v) for l, v in zip(labels, s[key]) if v is not None]
        p = josa(name, '은', '는')
        return f'{name}{p} {fmt[key](known[0][1])}에서 {fmt[key](known[-1][1])}로' if known else f'{name}{p} 값 없음'
    alt = (f'{fri.month}월 {fri.day}일부터 {days[-1].month}월 {days[-1].day}일까지 네 지표. '
           + ', '.join(said(n, k) for n, k in [('미 10년물', 'us10y'), ('브렌트유', 'brent'),
                                                ('원/달러', 'usdkrw'), ('코스피', 'kospi')]) + ' 움직였다.')
    if roll:
        alt += f' 브렌트유는 {labels[roll["at"]]}부터 {roll["label"]}이다.'
    gap = sys.argv[sys.argv.index('--gap-note') + 1] if '--gap-note' in sys.argv else '휴장'
    print(chart.small_multiples(panels, labels, caption, alt, gap_note=gap))


if __name__ == '__main__':
    main()
