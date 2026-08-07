#!/usr/bin/env bash
# Drop the pymath pack into a Copilot-compatible skills root.
# Canonical source: <pack>/skills/<name>/
# Usage:
#   ./agreeya-skills/scripts/drop-pymath-pack.sh personal
#   ./agreeya-skills/scripts/drop-pymath-pack.sh project /path/to/repo
#   ./agreeya-skills/scripts/drop-pymath-pack.sh personal pymath
#   ./agreeya-skills/scripts/drop-pymath-pack.sh project /path/to/repo pymath pystats

set -euo pipefail

PACK_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE_ROOT="${PACK_ROOT}/skills"
SKILLS=(pymath pystats pycheck)

usage() {
  cat <<'EOF'
Usage:
  drop-pymath-pack.sh personal [skill...]
  drop-pymath-pack.sh project <repo-root> [skill...]

Skills default to: pymath pystats pycheck
Canonical source: agreeya-skills/skills/<name>/
EOF
  exit 1
}

[[ $# -ge 1 ]] || usage
SCOPE="$1"
shift

case "$SCOPE" in
  personal)
    DEST_ROOT="${HOME}/.copilot/skills"
    ;;
  project)
    [[ $# -ge 1 ]] || usage
    REPO_ROOT="$1"
    shift
    DEST_ROOT="${REPO_ROOT}/.github/skills"
    ;;
  *)
    usage
    ;;
esac

if [[ $# -gt 0 ]]; then
  SKILLS=("$@")
fi

mkdir -p "$DEST_ROOT"

for name in "${SKILLS[@]}"; do
  src="${SOURCE_ROOT}/${name}"
  if [[ ! -f "${src}/SKILL.md" ]]; then
    echo "error: missing skill source: ${src}/SKILL.md" >&2
    exit 1
  fi
  dest="${DEST_ROOT}/${name}"
  rm -rf "$dest"
  mkdir -p "$dest"
  rsync -a \
    --exclude '.DS_Store' \
    --exclude 'state/' \
    --exclude '.skill-me-*' \
    --exclude '__pycache__/' \
    "${src}/" "${dest}/"
  if [[ ! -f "${dest}/SKILL.md" ]]; then
    echo "error: install failed for ${name}" >&2
    exit 1
  fi
  echo "installed: ${dest}"
done

echo "done. scope=${SCOPE} dest_root=${DEST_ROOT}"
echo "reload skills in your Copilot surface, then try: /pymath"
