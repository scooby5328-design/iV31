#!/usr/bin/env bash
set -euo pipefail

v="$1"
out="$2"
root="$(cd "$(dirname "$0")/.." && pwd)"
neu="$root/updates/iv31-$v.neu"
runtime_url="https://github.com/scooby5328-design/iV31/releases/download/runtime-6.10.0-mac10.15/neutralino-mac_universal"
runtime_sha="e849d345e828d20f4aee1409a6e9e7779cd0e0a19fb2403df19a38bb39cfd54f"

[ -f "$neu" ] || { echo "Missing $neu"; exit 1; }
want=$(jq -r .data.sha256 "$root/updates/manifest.json")
have=$(sha256sum "$neu" | cut -d' ' -f1)
[ "$want" = "$have" ] || { echo "updates/iv31-$v.neu does not match the manifest fingerprint"; exit 1; }

b="$(mktemp -d)"
curl -fsSL -o "$b/neutralino-mac_universal" "$runtime_url"
echo "$runtime_sha  $b/neutralino-mac_universal" | sha256sum -c --quiet

app="$b/dist/iv31.app/Contents"
mkdir -p "$app/MacOS" "$app/Resources"
cp "$b/neutralino-mac_universal" "$app/MacOS/iv31"
chmod 755 "$app/MacOS/iv31"
cp "$neu" "$app/MacOS/resources.neu"
cp "$root/packaging/icon.icns" "$app/Resources/iv31.icns"
sed "s/__VERSION__/$v/g" "$root/packaging/macos/Info.plist" > "$app/Info.plist"
printf 'APPL????' > "$app/PkgInfo"
touch -d "@$(git -C "$root" log -1 --format=%ct)" $(find "$b/dist") 2>/dev/null || true

(cd "$b/dist" && zip -q -r -y -X "$out/iv31-$v-mac.zip" iv31.app)
sha256sum "$out/iv31-$v-mac.zip" | cut -d' ' -f1 > "$out/iv31-$v-mac.sha256"
