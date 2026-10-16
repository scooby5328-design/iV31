#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
latest=$(jq -r .version updates/manifest.json)
work="$(mktemp -d)"
mac_since="1.4.1"

for notes in $(ls release-notes/*.md | sort -V); do
  v=$(basename "$notes" .md)
  if gh release view "v$v" >/dev/null 2>&1; then
    echo "v$v is already released"
    continue
  fi

  zip="iv31-Setup-$v.exe.zip"
  mac=""
  body="$work/notes-$v.md"
  cp "$notes" "$body"
  commit=$(git log --diff-filter=AM --format=%H -1 -- "$zip" || true)

  if [ -n "$commit" ]; then
    git show "$commit:$zip" > "$work/$zip"
    target="$commit"
  elif [ "$v" = "$latest" ]; then
    bash packaging/build-installer.sh "$v" "$work"
    printf '\n**SHA-256 of iv31-Setup-%s.exe:**\n\n```\n%s\n```\n' "$v" "$(cat "$work/iv31-Setup-$v.sha256")" >> "$body"
    if [ "$(printf '%s\n%s\n' "$mac_since" "$v" | sort -V | head -1)" = "$mac_since" ]; then
      bash packaging/build-mac.sh "$v" "$work"
      mac="$work/iv31-$v-mac.zip"
      printf '\n**SHA-256 of iv31-%s-mac.zip:**\n\n```\n%s\n```\n' "$v" "$(cat "$work/iv31-$v-mac.sha256")" >> "$body"
    fi
    target=$(git rev-parse HEAD)
  else
    echo "No installer found for $v, skipping"
    continue
  fi

  if [ "$v" = "$latest" ]; then latest_flag="--latest"; else latest_flag="--latest=false"; fi
  gh release create "v$v" "$work/$zip" ${mac:+"$mac"} --target "$target" --title "iv31 $v" --notes-file "$body" "$latest_flag"
  echo "Released v$v"
done
