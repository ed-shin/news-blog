#!/bin/bash
# 대화에서 함께 쓴 글(기획·용어 등)을 발행 전에 GPT(Codex CLI)에게 한 번 검수받는다.
# 지시문은 docs/gpt-review.md. Codex는 읽기 전용으로 돌아 파일을 고치지 못한다.
# 쓰는 법: scripts/gpt_review.sh src/content/terms/mcp.md ["이번에 특히 볼 것"]
# 결과는 화면과 ${TMPDIR}/gpt-review/<파일 이름>.md 에 남는다. 저장소에는 넣지 않는다.
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "쓰는 법: $0 <글 파일> [이번에 특히 볼 것]" >&2
  exit 1
fi
post="$1"; shift
extra="${*:-}"
root="$(cd "$(dirname "$0")/.." && pwd)"

if [ ! -f "$root/$post" ] && [ ! -f "$post" ]; then
  echo "파일이 없다: $post" >&2
  exit 1
fi
if ! command -v codex >/dev/null; then
  echo "codex CLI가 없다. ChatGPT 앱의 Codex를 설치하고 로그인한다." >&2
  exit 1
fi

out_dir="${TMPDIR:-/tmp}/gpt-review"
mkdir -p "$out_dir"
out="$out_dir/$(basename "$post" .md).md"

# docs/gpt-review.md에서 사람용 머리말(--- 위)을 떼고 지시문만 넘긴다
instructions="$(awk 'f; /^---$/ {f=1}' "$root/docs/gpt-review.md")"
prompt="${instructions}

검수할 글: ${post}"
if [ -n "$extra" ]; then
  prompt="${prompt}
이번에 특히 볼 것: ${extra}"
fi

# 진행 기록(읽은 파일·연 링크)은 따로 두고, 화면에는 마지막 보고만 낸다
log="$out_dir/$(basename "$post" .md).log"
# 검수 모델은 GPT-6.1 Terra(2026-10-28 사용자 결정). Codex 기본 모델과 달라 따로 지정한다
model="${GPT_REVIEW_MODEL:-gpt-6.1-terra}"
codex exec -m "$model" -s read-only --ephemeral --color never -C "$root" -o "$out" "$prompt" </dev/null >"$log" 2>&1
cat "$out"
echo
echo "(저장: $out · 진행 기록: $log)"
