#!/usr/bin/env bash
set -euo pipefail

debs="$1"
out="$2"
root="$(cd "$(dirname "$0")/.." && pwd)"
[ -n "${APT_SIGNING_KEY:-}" ] || { echo "APT_SIGNING_KEY is not set"; exit 1; }

export GNUPGHOME="$(mktemp -d)"
chmod 700 "$GNUPGHOME"
printf '%s\n' "$APT_SIGNING_KEY" | gpg --batch --quiet --import
key=$(gpg --list-secret-keys --with-colons | awk -F: '/^fpr/ {print $10; exit}')

command -v apt-ftparchive >/dev/null || { sudo apt-get update -qq && sudo apt-get install -y -qq apt-utils >/dev/null; }

rm -rf "$out"
mkdir -p "$out/pool/main/i/iv31"
cp "$debs"/*.deb "$out/pool/main/i/iv31/"
cd "$out"
for arch in amd64 arm64; do
  mkdir -p "dists/stable/main/binary-$arch"
  apt-ftparchive --arch "$arch" packages pool > "dists/stable/main/binary-$arch/Packages"
  gzip -9 -n -k "dists/stable/main/binary-$arch/Packages"
done
apt-ftparchive \
  -o APT::FTPArchive::Release::Origin=iv31 \
  -o APT::FTPArchive::Release::Label=iv31 \
  -o APT::FTPArchive::Release::Suite=stable \
  -o APT::FTPArchive::Release::Codename=stable \
  -o APT::FTPArchive::Release::Architectures="amd64 arm64" \
  -o APT::FTPArchive::Release::Components=main \
  -o APT::FTPArchive::Release::Description="iv31 Pokémon IV calculator" \
  release dists/stable > "$GNUPGHOME/Release"
mv "$GNUPGHOME/Release" dists/stable/Release
gpg --batch --yes --local-user "$key" --clearsign -o dists/stable/InRelease dists/stable/Release
gpg --batch --yes --local-user "$key" --armor --detach-sign -o dists/stable/Release.gpg dists/stable/Release
cp "$root/packaging/linux/iv31-archive-keyring.gpg" "$root/packaging/linux/iv31-archive-keyring.asc" "$root/packaging/linux/iv31.sources" .
rm -rf "$GNUPGHOME"
