#!/usr/bin/env bash
# Drop AgreeYa pymath pack into Copilot Cowork skills root from a cloned repo.
# Usage (from any cwd):
#   ./agreeya-skills/scripts/drop-to-cowork.sh
#   ./agreeya-skills/scripts/drop-to-cowork.sh pymath
#   COWORK_SKILLS_ROOT=/custom/path/skills ./agreeya-skills/scripts/drop-to-cowork.sh
#
# Default destination: ~/Documents/Cowork/skills/<skill-name>/

set -euo pipefail

PACK_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE_ROOT="${PACK_ROOT}/skills"
DEST_ROOT="${COWORK_SKILLS_ROOT:-${HOME}/Documents/Cowork/skills}"
SKILLS=(pymath pystats pycheck)

if [[ $# -gt 0 ]]; then
  SKILLS=("$@")
fi

if [[ ! -d "$SOURCE_ROOT" ]]; then
  echo "error: canonical skills not found at ${SOURCE_ROOT}" >&2
  echo "run this script from a clone of researchengineeringreports that contains agreeya-skills/skills/" >&2
  exit 1
fi

mkdir -p "$DEST_ROOT"

echo "source: ${SOURCE_ROOT}"
echo "dest:   ${DEST_ROOT}"

for name in "${SKILLS[@]}"; do
  src="${SOURCE_ROOT}/${name}"
  if [[ ! -f "${src}/SKILL.md" ]]; then
    echo "error: missing skill source: ${src}/SKILL.md" >&2
    exit 1
  fi
  dest="${DEST_ROOT}/${name}"
  rm -rf "$dest"
  mkdir -p "$dest"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a \
      --exclude '.DS_Store' \
      --exclude 'state/' \
      --exclude '.skill-me-*' \
      --exclude '__pycache__/' \
      "${src}/" "${dest}/"
  else
    # portable fallback
    tar -C "${src}" -cf - . | tar -C "${dest}" -xf -
  fi
  if [[ ! -f "${dest}/SKILL.md" ]]; then
    echo "error: install failed for ${name}" >&2
    exit 1
  fi
  echo "installed: ${dest}"
done

echo "done. Wait for OneDrive sync, refresh Copilot Cowork Skills, then smoke-test pymath."
echo "Guide: agreeya-skills/docs/install/COPILOT-COWORK-CLONE-DROP.md"
