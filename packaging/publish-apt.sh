#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
if [ -z "${APT_SIGNING_KEY:-}" ]; then
  echo "::notice::APT_SIGNING_KEY secret is not set, so the apt repository was not updated."
  exit 0
fi

check="$(mktemp -d)"
chmod 700 "$check"
printf '%s\n' "$APT_SIGNING_KEY" | GNUPGHOME="$check" gpg --batch --quiet --import
fpr=$(GNUPGHOME="$check" gpg --list-secret-keys --with-colons | awk -F: '/^fpr/ {print $10; exit}')
rm -rf "$check"
want_fpr=$(gpg --show-keys --with-colons packaging/linux/iv31-archive-keyring.asc | awk -F: '/^fpr/ {print $10; exit}')
[ -n "$fpr" ] && [ "$fpr" = "$want_fpr" ] || { echo "::error::APT_SIGNING_KEY doesn't match packaging/linux/iv31-archive-keyring.asc"; exit 1; }
echo "Signing key OK ($fpr)"

latest=$(jq -r .version updates/manifest.json)
current=$(curl -fsSL "https://raw.githubusercontent.com/$GITHUB_REPOSITORY/apt/version" 2>/dev/null || true)
if [ "$current" = "$latest" ]; then
  echo "The apt repository already has $latest"
  exit 0
fi

work="$(mktemp -d)"
mkdir -p "$work/debs"
n=0
for v in $(ls release-notes/*.md | xargs -n1 basename | sed 's/\.md$//' | sort -rV); do
  if gh release download "v$v" -p '*.deb' -D "$work/debs" 2>/dev/null; then
    n=$((n + 1))
    [ "$n" -ge 3 ] && break
  fi
done
ls "$work/debs"/iv31_"$latest"_*.deb >/dev/null || { echo "No .deb files for $latest"; exit 1; }

bash packaging/build-apt.sh "$work/debs" "$work/repo"
echo "$latest" > "$work/repo/version"
cd "$work/repo"
git init -q
git checkout -q -b apt
git add -A
git -c user.name="github-actions[bot]" -c user.email="41898282+github-actions[bot]@users.noreply.github.com" commit -qm "apt repository for iv31 $latest"
git push -q -f "https://x-access-token:${GH_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" apt
echo "Published the apt repository for $latest"
