#!/usr/bin/env bash
set -euo pipefail

v="$1"
out="$2"
root="$(cd "$(dirname "$0")/.." && pwd)"
neu="$root/updates/iv31-$v.neu"
runtime_id="$(cat "$root/updates/runtime/current")"
runtime_bin="$root/updates/runtime/$runtime_id/iv31-mac-universal"

[ -f "$neu" ] || { echo "Missing $neu"; exit 1; }
want=$(jq -r .data.sha256 "$root/updates/manifest.json")
have=$(sha256sum "$neu" | cut -d' ' -f1)
[ "$want" = "$have" ] || { echo "updates/iv31-$v.neu does not match the manifest fingerprint"; exit 1; }

b="$(mktemp -d)"

app="$b/dist/iv31.app/Contents"
mkdir -p "$app/MacOS" "$app/Resources"
cp "$runtime_bin" "$app/MacOS/iv31"
printf '%s\n' "$runtime_id" > "$app/MacOS/runtime.txt"
chmod 755 "$app/MacOS/iv31"
cp "$neu" "$app/MacOS/resources.neu"
cp "$root/packaging/icon.icns" "$app/Resources/iv31.icns"
sed "s/__VERSION__/$v/g" "$root/packaging/macos/Info.plist" > "$app/Info.plist"
printf 'APPL????' > "$app/PkgInfo"
touch -d "@$(git -C "$root" log -1 --format=%ct)" $(find "$b/dist") 2>/dev/null || true

(cd "$b/dist" && zip -q -r -y -X "$out/iv31-$v-mac.zip" iv31.app)
sha256sum "$out/iv31-$v-mac.zip" | cut -d' ' -f1 > "$out/iv31-$v-mac.sha256"
