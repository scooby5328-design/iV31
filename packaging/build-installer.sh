#!/usr/bin/env bash
set -euo pipefail

v="$1"
out="$2"
root="$(cd "$(dirname "$0")/.." && pwd)"
neu="$root/updates/iv31-$v.neu"

[ -f "$neu" ] || { echo "Missing $neu"; exit 1; }
want=$(jq -r .data.sha256 "$root/updates/manifest.json")
have=$(sha256sum "$neu" | cut -d' ' -f1)
[ "$want" = "$have" ] || { echo "updates/iv31-$v.neu does not match the manifest fingerprint"; exit 1; }

command -v makensis >/dev/null || { sudo apt-get update -qq && sudo apt-get install -y -qq nsis >/dev/null; }

b="$(mktemp -d)"
mkdir -p "$b/pkg" "$b/dist"
runtime_id="$(cat "$root/updates/runtime/current")"
cp "$root/updates/runtime/$runtime_id/iv31-windows-x64.exe" "$b/pkg/iv31.exe"
cp "$root/packaging/icon.ico" "$b/pkg/"
printf '%s\r\n' "$runtime_id" > "$b/pkg/runtime.txt"
cp "$neu" "$b/pkg/resources.neu"

(cd "$root/packaging" && npm install --no-save --silent resedit@2.0.3 pe-library@1.0.1 >/dev/null)
node "$root/packaging/stamp.mjs" "$b/pkg/iv31.exe" "$v"

sed "s/^!define VERSION .*/!define VERSION \"$v\"/" "$root/packaging/iv31.nsi" > "$b/iv31.nsi"
(cd "$b" && makensis -V2 iv31.nsi)
(cd "$b/dist" && zip -q -X "$out/iv31-Setup-$v.exe.zip" "iv31-Setup-$v.exe")
sha256sum "$b/dist/iv31-Setup-$v.exe" | cut -d' ' -f1 > "$out/iv31-Setup-$v.sha256"
