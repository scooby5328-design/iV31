#!/usr/bin/env bash
set -euo pipefail

v="$1"
out="$2"
root="$(cd "$(dirname "$0")/.." && pwd)"
neu="$root/updates/iv31-$v.neu"
nl_version="6.10.0"
nl_sha="e633f480737f229f582d8ec6165a52d789340950aef062560702122389f08329"
tool_version="1.9.0"

[ -f "$neu" ] || { echo "Missing $neu"; exit 1; }
want=$(jq -r .data.sha256 "$root/updates/manifest.json")
have=$(sha256sum "$neu" | cut -d' ' -f1)
[ "$want" = "$have" ] || { echo "updates/iv31-$v.neu does not match the manifest fingerprint"; exit 1; }

command -v desktop-file-validate >/dev/null || { sudo apt-get update -qq && sudo apt-get install -y -qq desktop-file-utils >/dev/null; }

b="$(mktemp -d)"
curl -fsSL -o "$b/nl.zip" "https://github.com/neutralinojs/neutralinojs/releases/download/v$nl_version/neutralinojs-v$nl_version.zip"
echo "$nl_sha  $b/nl.zip" | sha256sum -c --quiet
unzip -q -j "$b/nl.zip" neutralino-linux_x64 neutralino-linux_arm64 -d "$b"
cp "$root/packaging/linux/iv31-256.png" "$b/icon256.png"
cp "$root/packaging/linux/iv31-512.png" "$b/icon512.png"
stamp="$(git -C "$root" log -1 --format=%ct)"
export SOURCE_DATE_EPOCH="$stamp"

for arch in x64 arm64; do
  case $arch in
    x64) deb_arch=amd64; ai_arch=x86_64 ;;
    arm64) deb_arch=arm64; ai_arch=aarch64 ;;
  esac
  bin="$b/neutralino-linux_$arch"

  t="$b/tar-$arch/iv31"
  mkdir -p "$t"
  install -m 755 "$bin" "$t/iv31"
  install -m 644 "$neu" "$t/resources.neu"
  install -m 644 "$b/icon256.png" "$t/iv31.png"
  sed "s|__EXEC__|iv31|" "$root/packaging/linux/iv31.desktop" > "$t/iv31.desktop"
  tar --sort=name --mtime="@$stamp" --owner=0 --group=0 --numeric-owner -C "$b/tar-$arch" -czf "$out/iv31-$v-linux-$arch.tar.gz" iv31

  d="$b/deb-$arch"
  mkdir -p "$d/DEBIAN" "$d/opt/iv31" "$d/usr/bin" "$d/usr/share/applications" "$d/usr/share/icons/hicolor/256x256/apps" "$d/usr/share/icons/hicolor/512x512/apps"
  install -m 755 "$bin" "$d/opt/iv31/iv31"
  install -m 644 "$neu" "$d/opt/iv31/resources.neu"
  printf '#!/bin/sh\nexec /opt/iv31/iv31 "$@"\n' > "$d/usr/bin/iv31"
  chmod 755 "$d/usr/bin/iv31"
  sed "s|__EXEC__|/opt/iv31/iv31|" "$root/packaging/linux/iv31.desktop" > "$d/usr/share/applications/iv31.desktop"
  install -m 644 "$b/icon256.png" "$d/usr/share/icons/hicolor/256x256/apps/iv31.png"
  install -m 644 "$b/icon512.png" "$d/usr/share/icons/hicolor/512x512/apps/iv31.png"
  install -D -m 644 "$root/packaging/linux/iv31-archive-keyring.gpg" "$d/usr/share/keyrings/iv31-archive-keyring.gpg"
  install -D -m 644 "$root/packaging/linux/iv31.sources" "$d/etc/apt/sources.list.d/iv31.sources"
  size=$(du -sk --exclude=DEBIAN "$d" | cut -f1)
  sed -e "s/__VERSION__/$v/" -e "s/__ARCH__/$deb_arch/" -e "s/__SIZE__/$size/" "$root/packaging/linux/control" > "$d/DEBIAN/control"
  find "$d" -exec touch -h -d "@$stamp" {} +
  dpkg-deb --root-owner-group -Zxz --build "$d" "$out/iv31_${v}_${deb_arch}.deb" >/dev/null

  a="$b/appdir-$arch"
  mkdir -p "$a/usr/bin"
  install -m 755 "$bin" "$a/usr/bin/iv31"
  install -m 644 "$neu" "$a/usr/bin/resources.neu"
  install -m 644 "$b/icon256.png" "$a/iv31.png"
  sed "s|__EXEC__|iv31|" "$root/packaging/linux/iv31.desktop" > "$a/iv31.desktop"
  printf '#!/bin/sh\nhere="$(dirname "$(readlink -f "$0")")"\nexec "$here/usr/bin/iv31" "$@"\n' > "$a/AppRun"
  chmod 755 "$a/AppRun"
  if [ ! -x "$b/appimagetool" ]; then
    curl -fsSL -o "$b/appimagetool" "https://github.com/AppImage/appimagetool/releases/download/$tool_version/appimagetool-x86_64.AppImage"
    chmod +x "$b/appimagetool"
  fi
  if [ ! -f "$b/runtime-$ai_arch" ]; then
    curl -fsSL -o "$b/runtime-$ai_arch" "https://github.com/AppImage/type2-runtime/releases/download/continuous/runtime-$ai_arch"
  fi
  env -u SOURCE_DATE_EPOCH ARCH="$ai_arch" APPIMAGE_EXTRACT_AND_RUN=1 "$b/appimagetool" --no-appstream --runtime-file "$b/runtime-$ai_arch" "$a" "$out/iv31-$v-$ai_arch.AppImage" >"$b/appimagetool.log" 2>&1 || { cat "$b/appimagetool.log"; exit 1; }
done

(cd "$out" && sha256sum "iv31-$v-linux-x64.tar.gz" "iv31-$v-linux-arm64.tar.gz" "iv31_${v}_amd64.deb" "iv31_${v}_arm64.deb" "iv31-$v-x86_64.AppImage" "iv31-$v-aarch64.AppImage" > "iv31-$v-linux.sha256")
