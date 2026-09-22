"""글에 넣을 차트(SVG)를 데이터에서 만들어 낸다.

손으로 SVG를 그리면 숫자와 그림이 어긋나기 쉽다. 값을 여기에 적어 넣고 생성하면
본문 수치와 그림이 같은 출처에서 나온다. 결과는 마크다운에 그대로 붙이는 조각이다.

    python3 scripts/chart.py curve   # 만기별 금리 곡선 비교
    python3 scripts/chart.py series  # 날짜별 추이

색은 사이트 토큰(--accent, --muted 등)을 쓰므로 어두운 화면에서 그대로 읽힌다.
글씨 크기는 11px 아래로 내리지 않는다. 가로는 viewBox로 잡아 좁은 화면에서도 줄어든다.
"""

import sys

W, H = 680, 300
PAD = {'l': 52, 'r': 18, 't': 26, 'b': 46}


def _scale(lo, hi, size, pad_lo, invert=False):
    span = hi - lo or 1
    def f(v):
        t = (v - lo) / span
        return pad_lo + (size * (1 - t) if invert else size * t)
    return f


def _axis(ticks, y_of, label_fmt):
    out = []
    for t in ticks:
        y = round(y_of(t), 1)
        out.append(f'<line class="grid" x1="{PAD["l"]}" y1="{y}" x2="{W - PAD["r"]}" y2="{y}"/>')
        out.append(f'<text class="tick" x="{PAD["l"] - 8}" y="{y + 4}" text-anchor="end">{label_fmt(t)}</text>')
    return out


def curve(series, ticks, caption, alt):
    """만기별 곡선 여러 개를 겹쳐 그린다. series = [(이름, [(만기라벨, 값), ...]), ...]"""
    xs = [p[0] for p in series[0][1]]
    values = [v for _, pts in series for _, v in pts]
    lo, hi = min(values) - 0.12, max(values) + 0.12
    y_of = _scale(lo, hi, H - PAD['t'] - PAD['b'], PAD['t'], invert=True)
    step = (W - PAD['l'] - PAD['r']) / (len(xs) - 1)
    x_of = lambda i: PAD['l'] + step * i

    out = _axis(ticks, y_of, lambda t: f'{t:.1f}%')
    for i, label in enumerate(xs):
        out.append(f'<text class="tick" x="{round(x_of(i), 1)}" y="{H - PAD["b"] + 22}" text-anchor="middle">{label}</text>')

    for n, (name, pts) in enumerate(series):
        cls = 'now' if n == 0 else 'prev'
        d = ' '.join(f'{"M" if i == 0 else "L"}{round(x_of(i), 1)} {round(y_of(v), 1)}' for i, (_, v) in enumerate(pts))
        out.append(f'<path class="line {cls}" d="{d}"/>')
        for i, (_, v) in enumerate(pts):
            out.append(f'<circle class="dot {cls}" cx="{round(x_of(i), 1)}" cy="{round(y_of(v), 1)}" r="4"/>')
            # 두 곡선이 가까워 값을 다 적으면 겹친다. 숫자는 최신 곡선에만 적고
            # 지난 곡선은 점선과 이름으로만 둔다. 정확한 값은 본문과 표에 있다.
            if cls == 'now':
                anchor = 'start' if i == 0 else ('end' if i == len(pts) - 1 else 'middle')
                out.append(f'<text class="val {cls}" x="{round(x_of(i), 1)}" y="{round(y_of(v) - 12, 1)}" text-anchor="{anchor}">{v:.3f}</text>')
        out.append(f'<text class="name {cls}" x="{W - PAD["r"]}" y="{round(y_of(pts[-1][1]) + (38 if n else -30), 1)}" text-anchor="end">{name}</text>')

    return _figure(out, caption, alt)


def series_chart(points, ticks, caption, alt, marks=()):
    """날짜별 추이. points = [(라벨, 값), ...], marks = [(라벨, 값, 설명)]"""
    values = [v for _, v in points] + [v for _, v, _ in marks]
    lo, hi = min(values) - 0.04, max(values) + 0.06
    y_of = _scale(lo, hi, H - PAD['t'] - PAD['b'], PAD['t'], invert=True)
    step = (W - PAD['l'] - PAD['r']) / (len(points) - 1)
    x_of = lambda i: PAD['l'] + step * i

    out = _axis(ticks, y_of, lambda t: f'{t:.2f}%')
    for i, (label, _) in enumerate(points):
        out.append(f'<text class="tick" x="{round(x_of(i), 1)}" y="{H - PAD["b"] + 22}" text-anchor="middle">{label}</text>')

    d = ' '.join(f'{"M" if i == 0 else "L"}{round(x_of(i), 1)} {round(y_of(v), 1)}' for i, (_, v) in enumerate(points))
    out.append(f'<path class="line now" d="{d}"/>')
    for i, (_, v) in enumerate(points):
        out.append(f'<circle class="dot now" cx="{round(x_of(i), 1)}" cy="{round(y_of(v), 1)}" r="4.5"/>')
        anchor = 'start' if i == 0 else ('end' if i == len(points) - 1 else 'middle')
        out.append(f'<text class="val now" x="{round(x_of(i), 1)}" y="{round(y_of(v) - 12, 1)}" text-anchor="{anchor}">{v:.3f}</text>')

    for label, v, note in marks:
        i = [p[0] for p in points].index(label)
        y = round(y_of(v), 1)
        out.append(f'<line class="mark" x1="{round(x_of(i), 1)}" y1="{y}" x2="{round(x_of(i), 1) + 90}" y2="{y}"/>')
        out.append(f'<text class="note" x="{round(x_of(i), 1) + 96}" y="{y + 4}">{note}</text>')

    return _figure(out, caption, alt)


def spread(points, ticks, caption, alt, zero_note=''):
    """스프레드 추이. 0선을 긋고 음수 구간을 표시한다. points = [(라벨, 값), ...]"""
    values = [v for _, v in points]
    lo, hi = min(values) - 0.12, max(values) + 0.12
    y_of = _scale(lo, hi, H - PAD['t'] - PAD['b'], PAD['t'], invert=True)
    step = (W - PAD['l'] - PAD['r']) / (len(points) - 1)
    x_of = lambda i: PAD['l'] + step * i

    out = _axis(ticks, y_of, lambda t: f'{t:+.1f}')
    zero = round(y_of(0), 1)
    # 음수 구간(역전)을 띠로 깔아 눈에 보이게 한다
    negs = [i for i, (_, v) in enumerate(points) if v < 0]
    if negs:
        x1, x2 = round(x_of(negs[0]), 1), round(x_of(negs[-1]), 1)
        out.append(f'<rect class="band" x="{x1}" y="{PAD["t"]}" width="{round(x2 - x1, 1)}" height="{H - PAD["t"] - PAD["b"]}"/>')
        out.append(f'<text class="note" x="{round((x1 + x2) / 2, 1)}" y="{PAD["t"] + 16}" text-anchor="middle">{zero_note}</text>')
    out.append(f'<line class="zero" x1="{PAD["l"]}" y1="{zero}" x2="{W - PAD["r"]}" y2="{zero}"/>')

    d = ' '.join(f'{"M" if i == 0 else "L"}{round(x_of(i), 1)} {round(y_of(v), 1)}' for i, (_, v) in enumerate(points))
    out.append(f'<path class="line now" d="{d}"/>')
    for i, (label, v) in enumerate(points):
        if label.endswith('-01') or i == len(points) - 1:
            out.append(f'<text class="tick" x="{round(x_of(i), 1)}" y="{H - PAD["b"] + 22}" text-anchor="middle">{label[:4]}</text>')
    last = points[-1]
    out.append(f'<circle class="dot now" cx="{round(x_of(len(points) - 1), 1)}" cy="{round(y_of(last[1]), 1)}" r="4.5"/>')
    out.append(f'<text class="val now" x="{round(x_of(len(points) - 1), 1)}" y="{round(y_of(last[1]) - 12, 1)}" text-anchor="end">{last[1]:+.2f}</text>')
    return _figure(out, caption, alt)


def decomp(bars, caption, alt):
    """명목금리를 실질금리와 기대인플레이션으로 나눠 막대로 쌓는다.
    bars = [(라벨, 실질, 기대인플레)] — 둘의 합이 명목금리다."""
    top = max(r + b for _, r, b in bars) * 1.18
    h = H - PAD['t'] - PAD['b']
    y_of = _scale(0, top, h, PAD['t'], invert=True)
    bw = 96
    gap = (W - PAD['l'] - PAD['r'] - bw * len(bars)) / (len(bars) + 1)
    out = _axis([0, 2, 4], y_of, lambda t: f'{t:.0f}%')

    for i, (label, real, be) in enumerate(bars):
        x = round(PAD['l'] + gap * (i + 1) + bw * i, 1)
        y_real, y_top = round(y_of(real), 1), round(y_of(real + be), 1)
        base = round(y_of(0), 1)
        out.append(f'<rect class="seg real" x="{x}" y="{y_real}" width="{bw}" height="{round(base - y_real, 1)}"/>')
        out.append(f'<rect class="seg be" x="{x}" y="{y_top}" width="{bw}" height="{round(y_real - y_top, 1)}"/>')
        mid = round(x + bw / 2, 1)
        out.append(f'<text class="seglab" x="{mid}" y="{round((y_real + base) / 2 + 4, 1)}" text-anchor="middle">{real:.2f}</text>')
        out.append(f'<text class="seglab" x="{mid}" y="{round((y_top + y_real) / 2 + 4, 1)}" text-anchor="middle">{be:.2f}</text>')
        out.append(f'<text class="val now" x="{mid}" y="{round(y_top - 10, 1)}" text-anchor="middle">{real + be:.2f}</text>')
        out.append(f'<text class="tick" x="{mid}" y="{H - PAD["b"] + 22}" text-anchor="middle">{label}</text>')

    lx = W - PAD['r'] - 150
    out.append(f'<rect class="seg be" x="{lx}" y="{PAD["t"]}" width="12" height="12"/>')
    out.append(f'<text class="note" x="{lx + 18}" y="{PAD["t"] + 11}">기대인플레이션</text>')
    out.append(f'<rect class="seg real" x="{lx}" y="{PAD["t"] + 20}" width="12" height="12"/>')
    out.append(f'<text class="note" x="{lx + 18}" y="{PAD["t"] + 31}">실질금리</text>')
    return _figure(out, caption, alt)


def _figure(body, caption, alt):
    inner = '\n    '.join(body)
    return f'''<figure class="chart">
  <svg viewBox="0 0 {W} {H}" role="img" aria-label="{alt}">
    {inner}
  </svg>
  <figcaption>{caption}</figcaption>
</figure>'''


CHARTS = {
    # 9월 18일과 21일 마감. 두 날 모두 만기가 길수록 금리가 높은 우상향 곡선이다.
    'curve': lambda: curve(
        [('9월 21일', [('2년물', 4.772), ('10년물', 4.949), ('30년물', 5.282)]),
         ('9월 18일', [('2년물', 4.748), ('10년물', 4.998), ('30년물', 5.327)])],
        [4.8, 5.0, 5.2],
        '만기별 미 국채 금리. 두 날 모두 만기가 길수록 금리가 높다(우상향). 역전이 아니다.',
        '9월 18일과 21일의 만기별 미 국채 금리 곡선. 2년물에서 30년물로 갈수록 금리가 높아진다.'),
    # 미 재무부 일일 par yield 원자료의 월평균. 2022년 7월~2024년 8월이 역전 구간이다.
    'spread': lambda: spread(
        [['2022-01', 0.783], ['2022-02', 0.499], ['2022-03', 0.218], ['2022-04', 0.21], ['2022-05', 0.281], ['2022-06', 0.145], ['2022-07', -0.14], ['2022-08', -0.352], ['2022-09', -0.338], ['2022-10', -0.392], ['2022-11', -0.613], ['2022-12', -0.672], ['2023-01', -0.676], ['2023-02', -0.787], ['2023-03', -0.64], ['2023-04', -0.556], ['2023-05', -0.558], ['2023-06', -0.891], ['2023-07', -0.929], ['2023-08', -0.734], ['2023-09', -0.643], ['2023-10', -0.27], ['2023-11', -0.38], ['2023-12', -0.437], ['2024-01', -0.265], ['2024-02', -0.337], ['2024-03', -0.38], ['2024-04', -0.334], ['2024-05', -0.374], ['2024-06', -0.432], ['2024-07', -0.247], ['2024-08', -0.095], ['2024-09', 0.101], ['2024-10', 0.123], ['2024-11', 0.098], ['2024-12', 0.166], ['2025-01', 0.357], ['2025-02', 0.241], ['2025-03', 0.31], ['2025-04', 0.501], ['2025-05', 0.504], ['2025-06', 0.495], ['2025-07', 0.51], ['2025-08', 0.561], ['2025-09', 0.552], ['2025-10', 0.54], ['2025-11', 0.544], ['2025-12', 0.642], ['2026-01', 0.677], ['2026-02', 0.654], ['2026-03', 0.531], ['2026-04', 0.52], ['2026-05', 0.489], ['2026-06', 0.358], ['2026-07', 0.377], ['2026-08', 0.468], ['2026-09', 0.344]],
        [-0.5, 0.0, 0.5],
        '미 국채 2년물과 10년물의 금리차(월평균, %p). 0 아래가 역전이다. 2022년 7월부터 2024년 8월까지 26개월간 역전이었고, 그 뒤 침체는 선언되지 않았다. 미 재무부 일일 수익률 원자료로 계산했다.',
        '2022년 1월부터 2026년 9월까지 미 국채 2년-10년 금리차 추이. 2022년 7월부터 2024년 8월까지 0 아래로 내려갔다가 이후 양수로 올라와 2026년 9월 +0.34%p다.',
        zero_note='역전 구간 26개월'),
    # 연준이 올린 9월 16일 전후. 명목금리는 그대로인데 구성이 바뀌었다.
    'decomp': lambda: decomp(
        [('9월 15일', 2.62, 2.38), ('9월 18일', 2.68, 2.33)],
        '미 10년물 명목금리를 실질금리와 기대인플레이션으로 나눈 것. 연준이 금리를 올린 9월 16일 전후로 명목금리는 5.00%에서 5.01%로 거의 그대로인데, 실질금리가 오르고 기대인플레이션이 내렸다. 세인트루이스 연은 FRED 자료(2026년 9월 22일 조회).',
        '9월 15일과 18일의 미 10년물 구성 비교. 명목금리는 5.00%와 5.01%로 비슷하지만 실질금리는 2.62%에서 2.68%로 오르고 기대인플레이션은 2.38%에서 2.33%로 내렸다.'),
    'series': lambda: series_chart(
        [('9/17', 4.939), ('9/18', 4.998), ('9/21', 4.949)],
        [4.94, 4.98],
        '미 10년물 마감 금리. 19~20일은 주말이라 마감이 없다.',
        '미 10년물 금리가 9월 17일 4.939%에서 18일 4.998%로 올랐다가 21일 4.949%로 내린 추이',
        marks=[('9/18', 4.998, '주중 장중 5.041% — 2007년 이후 최고')]),
}

if __name__ == '__main__':
    name = sys.argv[1] if len(sys.argv) > 1 else ''
    if name not in CHARTS:
        print(__doc__)
        sys.exit(2)
    print(CHARTS[name]())
