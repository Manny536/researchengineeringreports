#!/usr/bin/env bash
# Validate every skill folder has SKILL.md and name match.
set -euo pipefail

LIB_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPO_ROOT="$(cd "${LIB_ROOT}/.." && pwd)"
fail=0

check_dir() {
  local root="$1"
  local d name front
  for d in "$root"/*/; do
    [[ -d "$d" ]] || continue
    name="$(basename "$d")"
    if [[ ! -f "${d}SKILL.md" ]]; then
      echo "FAIL missing SKILL.md: $d"; fail=1; continue
    fi
    front="$(grep -E '^name:' "${d}SKILL.md" | head -1 | awk '{print $2}' | tr -d '\r')"
    if [[ "$front" != "$name" ]]; then
      echo "FAIL name mismatch folder=${name} frontmatter=${front}"
      fail=1
    else
      echo "OK  ${name}"
    fi
  done
}

echo "== library skills =="
check_dir "${LIB_ROOT}/skills"
echo "== agreeya skills =="
check_dir "${REPO_ROOT}/agreeya-skills/skills"

# optional pytest for kakeya
if [[ -f "${REPO_ROOT}/agreeya-skills/skills/pymath/eval/test_kakeyalogic_coherence.py" ]]; then
  echo "== kakeya tests =="
  python3 -m pytest "${REPO_ROOT}/agreeya-skills/skills/pymath/eval/test_kakeyalogic_coherence.py" -q || fail=1
fi

exit "$fail"
