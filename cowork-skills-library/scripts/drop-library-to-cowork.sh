#!/usr/bin/env bash
# Drop the full Cowork Skills Library + agreeya accuracy pack into Copilot Cowork.
# Usage:
#   ./cowork-skills-library/scripts/drop-library-to-cowork.sh
#   COWORK_SKILLS_ROOT=/path/to/skills ./cowork-skills-library/scripts/drop-library-to-cowork.sh
set -euo pipefail

LIB_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPO_ROOT="$(cd "${LIB_ROOT}/.." && pwd)"
DEST_ROOT="${COWORK_SKILLS_ROOT:-${HOME}/Documents/Cowork/skills}"
AGREEYA_SKILLS="${REPO_ROOT}/agreeya-skills/skills"
LIB_SKILLS="${LIB_ROOT}/skills"

copy_skill() {
  local src="$1"
  local name
  name="$(basename "$src")"
  if [[ ! -f "${src}/SKILL.md" ]]; then
    echo "skip (no SKILL.md): ${src}" >&2
    return 0
  fi
  local dest="${DEST_ROOT}/${name}"
  rm -rf "$dest"
  mkdir -p "$dest"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a \
      --exclude '.DS_Store' \
      --exclude '__pycache__/' \
      --exclude 'state/' \
      --exclude '.skill-me-*' \
      "${src}/" "${dest}/"
  else
    tar -C "${src}" -cf - . | tar -C "${dest}" -xf -
  fi
  test -f "${dest}/SKILL.md"
  echo "installed: ${dest}"
}

mkdir -p "$DEST_ROOT"
echo "dest: ${DEST_ROOT}"

# 1) AgreeYa accuracy + review pack
if [[ -d "$AGREEYA_SKILLS" ]]; then
  for d in "$AGREEYA_SKILLS"/*/; do
    [[ -d "$d" ]] || continue
    copy_skill "${d%/}"
  done
else
  echo "warn: missing ${AGREEYA_SKILLS}" >&2
fi

# 2) Library-native skills
for d in "$LIB_SKILLS"/*/; do
  [[ -d "$d" ]] || continue
  copy_skill "${d%/}"
done

echo "done. Refresh Copilot Cowork Skills after OneDrive sync."
echo "catalog: ${LIB_ROOT}/CATALOG.md"
