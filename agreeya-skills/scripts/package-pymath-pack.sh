#!/usr/bin/env bash
# Package pymath pack for portable zip drop.
# Usage: ./agreeya-skills/scripts/package-pymath-pack.sh [version]
# Output: agreeya-skills/dist/pymath-pack_v<version>.zip

set -euo pipefail

VERSION="${1:-0.1.0}"
PACK_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE_ROOT="${PACK_ROOT}/skills"
DIST="${PACK_ROOT}/dist"
STAGE="${DIST}/pymath-pack_v${VERSION}"
OUT="${DIST}/pymath-pack_v${VERSION}.zip"
SKILLS=(pymath pystats pycheck)

rm -rf "$STAGE"
mkdir -p "$STAGE/skills"

for name in "${SKILLS[@]}"; do
  src="${SOURCE_ROOT}/${name}"
  [[ -f "${src}/SKILL.md" ]] || { echo "missing ${src}/SKILL.md" >&2; exit 1; }
  rsync -a \
    --exclude '.DS_Store' \
    --exclude 'state/' \
    --exclude '.skill-me-*' \
    --exclude '__pycache__/' \
    "${src}/" "${STAGE}/skills/${name}/"
done

mkdir -p "${STAGE}/docs/install"
rsync -a "${PACK_ROOT}/docs/install/" "${STAGE}/docs/install/"
cp "${PACK_ROOT}/README.md" "${STAGE}/README.md"
cp "${PACK_ROOT}/GOVERNANCE.md" "${STAGE}/GOVERNANCE.md"
cp "${PACK_ROOT}/ACCURACY.md" "${STAGE}/ACCURACY.md"
cp "${PACK_ROOT}/PROVENANCE.md" "${STAGE}/PROVENANCE.md"

rm -f "$OUT"
(
  cd "$DIST"
  zip -r "pymath-pack_v${VERSION}.zip" "pymath-pack_v${VERSION}" >/dev/null
)

echo "wrote ${OUT}"
echo "extract, then install each skills/<name>/ folder per docs/install/"
