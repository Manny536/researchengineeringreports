#!/usr/bin/env bash
# Package full Cowork library (library skills + agreeya skills snapshot).
# Usage: ./cowork-skills-library/scripts/package-library.sh [version]
set -euo pipefail

VERSION="${1:-1.0.0}"
LIB_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPO_ROOT="$(cd "${LIB_ROOT}/.." && pwd)"
DIST="${LIB_ROOT}/dist"
STAGE="${DIST}/cowork-skills-library_v${VERSION}"
OUT="${DIST}/cowork-skills-library_v${VERSION}.zip"

rm -rf "$STAGE"
mkdir -p "${STAGE}/skills"

copy_tree() {
  local src="$1" dest="$2"
  mkdir -p "$dest"
  rsync -a --exclude '.DS_Store' --exclude '__pycache__/' --exclude 'state/' "${src}/" "${dest}/"
}

# library skills
for d in "${LIB_ROOT}/skills"/*/; do
  [[ -f "${d}SKILL.md" ]] || continue
  name="$(basename "$d")"
  copy_tree "$d" "${STAGE}/skills/${name}"
done

# agreeya skills
if [[ -d "${REPO_ROOT}/agreeya-skills/skills" ]]; then
  for d in "${REPO_ROOT}/agreeya-skills/skills"/*/; do
    [[ -f "${d}SKILL.md" ]] || continue
    name="$(basename "$d")"
    copy_tree "$d" "${STAGE}/skills/${name}"
  done
fi

cp "${LIB_ROOT}/README.md" "${STAGE}/"
cp "${LIB_ROOT}/CATALOG.md" "${STAGE}/"
cp "${LIB_ROOT}/GOVERNANCE.md" "${STAGE}/"
mkdir -p "${STAGE}/docs"
cp "${LIB_ROOT}/docs/COWORK-LIBRARY-INSTALL.md" "${STAGE}/docs/" 2>/dev/null || true

rm -f "$OUT"
( cd "$DIST" && zip -r "cowork-skills-library_v${VERSION}.zip" "cowork-skills-library_v${VERSION}" >/dev/null )
echo "wrote ${OUT}"
