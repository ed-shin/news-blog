#!/bin/bash
# 데스크·주간 루틴의 커밋. 작성자를 여기서 고정한다.
# 쓰는 법: scripts/commit.sh <메시지 파일> <파일> [파일...]
# 푸시는 따로 한다: git push origin main
set -euo pipefail

if [ $# -lt 2 ]; then
  echo "쓰는 법: $0 <메시지 파일> <파일> [파일...]" >&2
  exit 1
fi
msg="$1"; shift

git add -- "$@"
git -c user.name=barney -c user.email=jp.shin.kor@gmail.com commit -q -F "$msg"
git log -1 --format='%h %an <%ae> %s'
