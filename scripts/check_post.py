#!/usr/bin/env python3
"""조간 일일 글(post.md)과 tracking.json 형식 검사.

사용법:
    python3 check_post.py <post.md> [tracking.json]

'오류'는 사이트 빌드가 깨지거나 편집 원칙에 어긋나는 것이라 반드시 고친다.
'경고'는 사람이 읽고 판단할 것. 종료 코드는 오류가 있으면 1.
PyYAML이 있으면 쓰고, 없으면 이 파일의 간이 해석기로 frontmatter를 읽는다.
"""
import json
import re
import sys
from datetime import date
from urllib.parse import urlparse

DESK_ORDER = ["rates", "energy", "geo", "tech", "etc"]
# 데스크 → 본문 섹션 제목 머리 (사이트가 이 머리로 섹션 id를 붙인다)
DESK_SECTION = {"rates": "금리", "energy": "에너지", "geo": "지정학", "tech": "IT", "etc": "그 외"}
SECTION_ORDER = ["3줄 요약", "오늘의 숫자", "금리", "시장", "에너지", "지정학", "IT", "그 외", "다음에 볼 것"]
MARKET_ROWS = ["코스피", "원/달러", "S&P 500", "미 10년물", "브렌트", "금"]
TOPIC_TAGS = {"금리", "시장", "에너지", "지정학", "테크", "부동산"}
TRENDS = {"up", "cool", "flat"}
# 열 때마다 내용이 바뀌어 근거가 될 수 없는 링크
LIVE_PAGE_PATTERNS = [
    (r"(^|\.)investing\.com$", r"^/(currencies|commodities|indices|rates-bonds|equities)/"),
    (r"(^|\.)polymarket\.com$", r".*"),
    (r"(^|\.)finance\.yahoo\.com$", r"^/quote/"),
    (r"^news\.hada\.io$", r"^/(?!topic)"),
    (r"^news\.ycombinator\.com$", r"^/(?!item)"),
]

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


# ── 간이 YAML 해석기 (이 블로그 frontmatter에 쓰는 문법만) ──────────────
def _split_flow(inner):
    parts, buf, depth, quote = [], "", 0, None
    for ch in inner:
        if quote:
            buf += ch
            if ch == quote and not buf.endswith("\\" + quote):
                quote = None
            continue
        if ch in "\"'":
            quote = ch
        elif ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        elif ch == "," and depth == 0:
            parts.append(buf.strip())
            buf = ""
            continue
        buf += ch
    if buf.strip():
        parts.append(buf.strip())
    return parts


def _scalar(s):
    s = s.strip()
    if s == "":
        return None
    if s.startswith('"'):
        return json.loads(s)
    if s.startswith("'"):
        return s[1:-1].replace("''", "'")
    if s.startswith("["):
        return [_scalar(p) for p in _split_flow(s[1:-1])]
    if s.startswith("{"):
        out = {}
        for p in _split_flow(s[1:-1]):
            k, _, v = p.partition(":")
            out[k.strip()] = _scalar(v)
        return out
    if s in ("true", "false"):
        return s == "true"
    if re.fullmatch(r"-?\d+", s):
        return int(s)
    return s


_KEY = re.compile(r"^([A-Za-z_][\w-]*):(\s|$)")


def mini_yaml(text):
    lines = []
    for raw in text.split("\n"):
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        lines.append([len(raw) - len(raw.lstrip(" ")), raw.strip()])

    def block(i, indent):
        return (lst if lines[i][1].startswith("- ") else mapping)(i, indent)

    def mapping(i, indent):
        out = {}
        while i < len(lines) and lines[i][0] == indent and not lines[i][1].startswith("- "):
            m = _KEY.match(lines[i][1])
            if not m:
                raise ValueError(f"해석할 수 없는 줄: {lines[i][1]}")
            key, rest = m.group(1), lines[i][1][m.end():].strip()
            i += 1
            if rest:
                out[key] = _scalar(rest)
            elif i < len(lines) and (lines[i][0] > indent or (lines[i][0] == indent and lines[i][1].startswith("- "))):
                out[key], i = block(i, lines[i][0])
            else:
                out[key] = None
        return out, i

    def lst(i, indent):
        out = []
        while i < len(lines) and lines[i][0] == indent and lines[i][1].startswith("- "):
            content = lines[i][1][2:].strip()
            if _KEY.match(content) and not content.startswith(("{", "[", '"', "'")):
                lines[i] = [indent + 2, content]
                item, i = mapping(i, indent + 2)
                out.append(item)
            else:
                out.append(_scalar(content))
                i += 1
        return out, i

    result, _ = block(0, lines[0][0]) if lines else ({}, 0)
    return result


def load_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        err("frontmatter(--- … ---)가 없다")
        return {}, text
    fm_text, body = m.group(1), m.group(2)
    try:
        import yaml  # type: ignore
        data = yaml.safe_load(fm_text)
    except ImportError:
        data = mini_yaml(fm_text)
    except Exception as e:  # yaml.YAMLError
        err(f"frontmatter YAML 문법 오류: {e}")
        return {}, body
    return data or {}, body


# ── 검사 ────────────────────────────────────────────────────────────────
def is_str(v):
    return isinstance(v, str) and v.strip() != ""


def check_url(url, where):
    if not re.match(r"^https?://", url or ""):
        err(f"{where}: http(s) 주소가 아니다 → {url}")
        return
    u = urlparse(url)
    host, path = u.netloc.lower(), u.path or "/"
    if path in ("", "/") and not u.query:
        err(f"{where}: 사이트 첫 화면 링크라 근거가 되지 않는다 → {url}")
    for host_re, path_re in LIVE_PAGE_PATTERNS:
        if re.search(host_re, host) and re.search(path_re, path):
            err(f"{where}: 내용이 계속 바뀌는 페이지(시세·첫 화면)라 근거가 되지 않는다 → {url}")


def is_weekend_edition(pub):
    """일요일·월요일판은 새 마감이 없다. 미국 시장이 주말에 쉬고 선물·외환은 한국 시간
    월요일 새벽에야 다시 열려 장중 값뿐이라, 직전 거래일(금) 마감을 반복하게 된다.
    그래서 '오늘의 숫자' 표를 만들지 않고 1면 지표의 등락도 비운다."""
    try:
        return date.fromisoformat(str(pub)).weekday() in (6, 0)  # 일=6, 월=0
    except ValueError:
        return False


def check_frontmatter(fm):
    title, desc, pub, tags = fm.get("title"), fm.get("description"), fm.get("pubDate"), fm.get("tags")
    if not is_str(title):
        err("title이 비었다")
    elif not re.match(r"^\d{1,2}월 \d{1,2}일 — .+", title):
        warn('title은 "M월 D일 — 헤드라인" 형식이 기본이다')
    if not is_str(desc):
        err("description이 비었다")
    pub_s = pub.isoformat() if isinstance(pub, date) else str(pub or "")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", pub_s):
        err(f"pubDate가 YYYY-MM-DD가 아니다 → {pub}")
    if not isinstance(tags, list) or not tags or tags[0] not in ("일일", "주간", "기획"):
        err('tags는 목록이고 첫 태그가 종류("일일"·"주간"·"기획") 중 하나여야 한다')
    else:
        for t in tags[1:]:
            if t not in TOPIC_TAGS:
                warn(f"새 주제 태그 '{t}' — 필요하면 desk-report에 적는다")
    # period와 highlights는 주간·기획의 몫이다. 일일 글에 있으면 알린다
    if isinstance(tags, list) and tags[:1] == ["일일"]:
        for k in ("updatedDate", "period", "highlights"):
            if k in fm:
                warn(f"일일 글에는 보통 {k}를 쓰지 않는다")
    for text in (title or "", desc or ""):
        if "브리핑" in text:
            warn('화면 용어는 "브리핑" 대신 "일일"')
    return pub_s


def check_front(fm, body):
    weekend = is_weekend_edition(fm.get("pubDate"))
    front = fm.get("front")
    if not isinstance(front, dict):
        err("front(1면 데이터)가 없다")
        return
    if not is_str(front.get("headline")):
        err("front.headline이 비었다")
    elif is_str(fm.get("title")) and front["headline"] not in fm["title"]:
        warn("title과 front.headline이 다르다")

    analysis = front.get("analysis")
    if not isinstance(analysis, list) or not analysis:
        err("front.analysis가 비었다")
    else:
        if len(analysis) != 3:
            warn(f"front.analysis가 {len(analysis)}갈래다(기본은 세 갈래)")
        for n, a in enumerate(analysis, 1):
            if not (isinstance(a, dict) and is_str(a.get("lead")) and is_str(a.get("text"))):
                err(f"front.analysis[{n}]에 lead와 text가 모두 있어야 한다")
            elif len(a["text"]) < 120:
                warn(f"front.analysis[{n}] 해설이 짧다 — 사용자는 짧고 얕은 해설을 싫어한다")

    markets = front.get("markets")
    if not isinstance(markets, dict) or not is_str(markets.get("asOf")) or not isinstance(markets.get("rows"), list):
        err("front.markets에 asOf와 rows가 있어야 한다")
    else:
        rows = markets["rows"]
        names = [r.get("name") for r in rows if isinstance(r, dict)]
        expected = (["기준금리"] if names[:1] == ["기준금리"] else []) + MARKET_ROWS
        if names != expected:
            err(f"1면 지표는 {MARKET_ROWS} 순서로 고정(기준금리가 바뀐 날만 맨 앞에 추가) → 지금: {names}")
        for r in rows:
            if not isinstance(r, dict):
                continue
            value, change = str(r.get("value", "")), str(r.get("change") or "")
            if value == "—":
                continue
            if weekend:
                # 등락은 비우는 것이 맞고, 마감 수치를 본문에 다시 쓰지도 않는다
                if change:
                    warn(f"지표 '{r.get('name')}'에 등락이 있다 — 일요일·월요일판은 비운다")
                continue
            if not re.match(r"^[+-]", change):
                err(f"지표 '{r.get('name')}' 등락 '{change}'에 +/- 부호가 없다")
            core = re.sub(r"^\$", "", value).split()[0]
            if core and core not in body:
                warn(f"지표 '{r.get('name')}' 값 {value}가 본문에 없다 — 본문 링크로 뒷받침되는지 확인")

    desks = front.get("desks")
    if not isinstance(desks, list) or not desks:
        err("front.desks가 비었다")
        return
    keys = [d.get("key") for d in desks if isinstance(d, dict)]
    if any(k not in DESK_ORDER for k in keys) or keys != sorted(keys, key=DESK_ORDER.index) or len(set(keys)) != len(keys):
        err(f"front.desks 순서는 {DESK_ORDER} 중 겹치지 않게 → 지금: {keys}")
    headings = re.findall(r"^## (.+)$", body, re.M)
    for d in desks:
        if not isinstance(d, dict):
            continue
        key = d.get("key")
        items = d.get("items")
        if not isinstance(items, list) or not 1 <= len(items) <= 2:
            err(f"데스크 {key}: items는 1~2개")
            items = items if isinstance(items, list) else []
        for n, it in enumerate(items, 1):
            where = f"데스크 {key} 항목 {n}"
            if not isinstance(it, dict) or not all(is_str(it.get(f)) for f in ("title", "text", "source", "url")):
                err(f"{where}: title·text·source·url이 모두 있어야 한다")
                continue
            check_url(it["url"], where)
            for num in re.findall(r"\d[\d,.]*\d|\d", it["text"]):
                if len(num) >= 3 and num not in body:
                    warn(f"{where}: 숫자 {num}이 본문에 없다 — 1면 항목 숫자는 본문에서 확인된 것이어야 한다")
            if it["url"] not in body:
                err(f"{where}: 링크가 본문에 없다 — 1면 항목은 본문에 실린 기사여야 한다 → {it['url']}")
        if not is_str(d.get("summary")):
            err(f"데스크 {key}: summary가 비었다")
        prefix = DESK_SECTION.get(key)
        if prefix and not any(h.startswith(prefix) for h in headings):
            err(f"데스크 {key}의 1면 링크가 갈 본문 섹션('## {prefix}…')이 없다")


def check_links_only(body):
    """주간·기획처럼 섹션이 자유로운 글에 쓰는 검사. 링크 규칙만 본다."""
    for m in re.finditer(r"\[[^\]]+\]\((https?://[^)]+)\)", body):
        check_url(m.group(1), "본문")
    for m in re.finditer(r"\]\((/blog/[^)]+)\)", body):
        err(f"옛 주소를 쓰고 있다 → {m.group(1)}")


def check_body(body, pub):
    headings = re.findall(r"^## (.+)$", body, re.M)
    order = []
    for h in headings:
        prefix = next((p for p in SECTION_ORDER if h.startswith(p)), None)
        if prefix is None:
            warn(f"정해진 섹션이 아닌 제목: '## {h}'")
            if "출처와 방법" in h:
                err('"출처와 방법" 섹션은 두지 않는다')
        else:
            order.append(SECTION_ORDER.index(prefix))
        if "브리핑" in h:
            warn('화면 용어는 "브리핑" 대신 "일일"')
    if order != sorted(order):
        err(f"섹션 순서는 {SECTION_ORDER} → 지금: {headings}")
    if is_weekend_edition(pub):
        if headings[:1] != ["3줄 요약"]:
            err("본문은 '## 3줄 요약'으로 시작한다")
        if "오늘의 숫자" in headings:
            warn("일요일·월요일판은 새 마감이 없다 — 오늘의 숫자 표 대신 직전 거래일 안내 한 줄로 대신한다")
    elif headings[:2] != ["3줄 요약", "오늘의 숫자"]:
        err("본문은 '## 3줄 요약', '## 오늘의 숫자'로 시작한다")

    summary = re.search(r"^## 3줄 요약\n(.*?)(?=^## )", body, re.M | re.S)
    if summary and len(re.findall(r"^\d+\. ", summary.group(1), re.M)) != 3:
        warn("3줄 요약이 세 줄이 아니다")

    if "**분석:**" in body:
        warn('해석 표시는 "**해설:**"을 쓴다')

    section_ids = {"summary", "numbers", "rates", "market", "energy", "geo", "tech", "etc"}
    for href in re.findall(r"\]\((/[^)\s]*)\)", body):
        if href.startswith("/blog/"):
            err(f"옛 /blog/ 주소다. 조간 글은 /jogan/daily/날짜/, /jogan/weekly/날짜/, /jogan/feature/이름/ → {href}")
            continue
        m = re.fullmatch(r"/jogan/(daily|weekly|today)/\d{4}-\d{2}-\d{2}/(#(.+))?|/jogan/feature/[\w%-]+/(#.+)?|#[^/]+", href)
        if not m:
            warn(f"내부 링크 형식이 낯설다 → {href} (예: /jogan/daily/2026-09-18/#rates)")
        elif m.group(1) == "daily" and m.group(3) and m.group(3) not in section_ids:
            err(f"일일 글 섹션 주소는 {sorted(section_ids)} 중 하나 → {href}")

    links = re.findall(r"\]\((https?://[^)\s]+)\)", body)
    if not links:
        err("본문에 출처 링크가 없다")
    for url in set(links):
        check_url(url, "본문 링크")

    # 오늘의 숫자 표에는 값까지 확인된 행만
    numbers = re.search(r"^## 오늘의 숫자\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    if numbers:
        for row in re.findall(r"^\|(.+)\|\s*$", numbers.group(1), re.M):
            cells = [c.strip() for c in row.split("|")]
            if len(cells) >= 2 and cells[1] in ("—", "-", ""):
                warn(f"오늘의 숫자 표 '{cells[0]}' 행에 값이 없다 — 값까지 확인된 행만 표에 넣고, 등락만 확인되면 본문 문장으로")

    # 출처 없는 숫자 단락 (해설·표·각주·제목 제외). 목록은 항목마다 보되,
    # 목록을 여는 바로 앞 문단에 출처가 있으면 그 출처를 이어받은 것으로 본다.
    section, prev_has_link = "", False
    for block in re.split(r"\n\s*\n", body):
        first = block.strip().split("\n")[0]
        if first.startswith("## "):
            section, prev_has_link = first, False
            continue
        if section.startswith(("## 3줄 요약", "## 오늘의 숫자")):
            continue
        is_table = first.startswith("|")
        is_footnote = first.startswith("*") and not first.startswith("**")
        is_analysis = first.startswith("**해설")
        if is_table or is_footnote or is_analysis:
            prev_has_link = False
            continue
        is_list = block.lstrip().startswith("- ")
        items = re.split(r"\n(?=\s*- )", block) if is_list else [block]
        parent_has_link = False  # 들여쓴 하위 항목은 바로 위 상위 항목의 출처를 이어받는다
        for item in items:
            text = item.strip()
            nested = is_list and len(item) - len(item.lstrip(" ")) > 0
            has_link = "](" in text
            inherited = is_list and (prev_has_link or (nested and parent_has_link))
            if re.search(r"\d", text) and not has_link and not inherited:
                warn(f"출처 링크 없이 숫자가 있는 단락({section[3:] or '처음'}): {text[:40]}…")
            if not nested:
                parent_has_link = has_link
        prev_has_link = "](" in block


def check_tracking(path, pub):
    try:
        data = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        err(f"tracking.json을 읽을 수 없다: {e}")
        return
    if data.get("asOf") != pub:
        warn(f"tracking.json asOf({data.get('asOf')})가 글 날짜({pub})와 다르다")
    topics = data.get("topics")
    if not isinstance(topics, list) or not topics:
        err("tracking.json topics가 비었다")
        return
    if len(topics) > 7:
        warn(f"추적 토픽이 {len(topics)}개다(다섯~여섯 개 권장)")
    for n, t in enumerate(topics, 1):
        if not all(is_str(t.get(f)) for f in ("name", "trend", "status", "note")):
            err(f"tracking topic {n}: name·trend·status·note가 모두 있어야 한다")
        elif t["trend"] not in TRENDS:
            err(f"tracking topic {n} trend는 {sorted(TRENDS)} 중 하나 → {t['trend']}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    text = open(sys.argv[1], encoding="utf-8").read()
    fm, body = load_frontmatter(text)
    if fm:
        pub = check_frontmatter(fm)
        tags = fm.get("tags")
        kind = tags[0] if isinstance(tags, list) and tags else ""
        # 1면 데이터와 고정 섹션 순서는 일일 글의 규칙이다.
        # 주간 흐름과 기획은 제목을 자유롭게 달고 front도 두지 않는다.
        if kind == "일일":
            check_front(fm, body)
            check_body(body, pub)
        else:
            check_links_only(body)
            if not fm.get("period"):
                err(f"{kind} 글은 period: {{ from, to }}로 다루는 기간을 적어야 한다")
        if len(sys.argv) > 2:
            check_tracking(sys.argv[2], pub)
    for m in errors:
        print(f"오류: {m}")
    for m in warnings:
        print(f"경고: {m}")
    print(f"\n오류 {len(errors)}건, 경고 {len(warnings)}건")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
