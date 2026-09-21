"""빌드 결과(dist/)의 내부 링크를 검사한다.

서버를 띄우지 않고 파일만 보고 확인하므로 자동 발행 파이프라인에서 그대로 쓸 수 있다.
글 사이를 잇는 링크가 많고 지난 글을 고치면 앵커가 사라질 수 있어서, 주소뿐 아니라
`#numbers` 같은 조각까지 실제로 있는지 본다.

    python3 scripts/linkcheck.py          # 기본값 dist/
    python3 scripts/linkcheck.py 다른경로

문제가 있으면 목록을 찍고 종료 코드 1로 끝난다.
"""

import os
import re
import sys
from urllib.parse import unquote, urldefrag, urljoin

ROOT = sys.argv[1] if len(sys.argv) > 1 else 'dist'
HREF = re.compile(r'<a\b[^>]*?href="([^"]+)"', re.I)


def page_files():
    for base, _, names in os.walk(ROOT):
        for name in names:
            if name.endswith('.html'):
                yield os.path.join(base, name)


def url_of(path):
    """dist/jogan/index.html → /jogan/"""
    rel = os.path.relpath(path, ROOT).replace(os.sep, '/')
    return '/' + (rel[: -len('index.html')] if rel.endswith('index.html') else rel)


def file_for(url_path):
    """주소를 dist 안의 파일로 바꾼다. 없으면 None."""
    rel = url_path.lstrip('/')
    for candidate in (
        os.path.join(ROOT, rel, 'index.html') if url_path.endswith('/') else None,
        os.path.join(ROOT, rel),
        os.path.join(ROOT, rel, 'index.html'),
        os.path.join(ROOT, rel + '.html'),
    ):
        if candidate and os.path.isfile(candidate):
            return candidate
    return None


def main():
    if not os.path.isdir(ROOT):
        print(f'{ROOT} 폴더가 없다. 먼저 빌드해야 한다.')
        return 1

    bodies = {}
    problems = []
    pages = sorted(page_files())

    for path in pages:
        html = open(path, encoding='utf-8').read()
        bodies[path] = html
        here = url_of(path)

        for href in HREF.findall(html):
            if re.match(r'^(https?:|mailto:|tel:|data:)', href):
                continue
            target, frag = urldefrag(urljoin(here, href))
            target = target.split('?')[0]  # ?tag=금리 같은 질의는 파일이 아니라 화면에서 거른다
            frag = unquote(frag)  # href는 퍼센트 인코딩, id는 한글 그대로
            if not target and not frag:
                problems.append(f'{here} → 빈 링크')
                continue

            target_file = path if not target or target == here else file_for(target)
            if target_file is None:
                problems.append(f'{here} → {href} (주소 없음)')
                continue
            if frag:
                body = bodies.get(target_file) or open(target_file, encoding='utf-8').read()
                bodies[target_file] = body
                if not re.search(rf'\bid="{re.escape(frag)}"', body):
                    problems.append(f'{here} → {href} (#{frag} 없음)')

    print(f'페이지 {len(pages)}개 검사')
    for line in problems:
        print('  ', line)
    print(f'문제 {len(problems)}건')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
