#!/usr/bin/env python3
"""새 글·고친 글의 주소를 IndexNow로 검색엔진에 바로 알린다(네이버·빙 등).

    python3 scripts/indexnow.py src/content/blog/2026-09-30-daily.md   # 글 파일 → 주소로 바꿔 알림
    python3 scripts/indexnow.py https://gyeonmunrok.com/jogan/          # 주소를 그대로 알림

구글은 IndexNow를 쓰지 않는다. 구글은 사이트맵과 서치 콘솔 색인 요청으로 간다.
인증 키는 public/{KEY}.txt에 있다. 키를 바꾸면 이 파일의 KEY와 키 파일을 함께 바꾼다.
글 파일은 src/lib/posts.ts의 postUrl과 같은 규칙으로 주소를 만든다. 어긋나면 알림이 헛돈다.
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

HOST = 'gyeonmunrok.com'
KEY = '6b36733a11663d38cacecd670769bf84'
ENDPOINT = 'https://api.indexnow.org/indexnow'   # 참여 검색엔진(네이버·빙 등)에 함께 전달된다


def url_of(path):
    """글 파일 → 공개 주소. 종류 태그(일일·주간·기획)에 따라 나뉜다."""
    text = Path(path).read_text(encoding='utf-8')
    fm = text.split('---')[1]
    slug = Path(path).stem
    tags = re.search(r'^tags:\s*\[(.*)\]', fm, re.M)
    tags = tags.group(1) if tags else ''
    pub = re.search(r'^pubDate:\s*(\S+)', fm, re.M).group(1)
    if '"일일"' in tags:
        return f'https://{HOST}/jogan/daily/{pub}/'
    if '"주간"' in tags:
        frm = re.search(r'from:\s*([\d-]+)', fm).group(1)
        return f'https://{HOST}/jogan/weekly/{frm}/'
    if '"기획"' in tags:
        return f'https://{HOST}/jogan/feature/{re.sub(r"^\d{4}-\d{2}-\d{2}-", "", slug)}/'
    return f'https://{HOST}/blog/{slug}/'


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    urls = [a if a.startswith('http') else url_of(a) for a in args]
    # 새 글이 올라오면 함께 바뀌는 목록 페이지도 알린다
    for extra in ('/', '/jogan/', '/jogan/all/', '/jogan/flow/'):
        u = f'https://{HOST}{extra}'
        if u not in urls:
            urls.append(u)
    body = json.dumps({'host': HOST, 'key': KEY, 'keyLocation': f'https://{HOST}/{KEY}.txt',
                       'urlList': urls}).encode()
    req = urllib.request.Request(ENDPOINT, data=body, method='POST',
                                 headers={'Content-Type': 'application/json; charset=utf-8'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f'IndexNow {r.status}: {len(urls)}개 주소를 알렸다')
            for u in urls:
                print('  ', u)
    except urllib.error.HTTPError as e:
        # 200·202가 정상이다. 403은 키 파일이 아직 배포되지 않은 것, 422는 주소가 호스트와 맞지 않는 것
        sys.exit(f'IndexNow 실패 {e.code}: {e.read().decode(errors="ignore")[:200]}')


if __name__ == '__main__':
    main()
