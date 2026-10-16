#!/usr/bin/env bash
set -u
apk=android/app/build/outputs/apk/debug/app-debug.apk
mkdir -p shots
adb install -r "$apk"
adb shell settings put system screen_off_timeout 600000
for tier in free pro; do
  adb shell am force-stop com.chili.iv31.debug
  adb shell am start -W -n com.chili.iv31.debug/com.chili.iv31.MainActivity --es tier "$tier"
  sleep 20
  adb exec-out screencap -p > "shots/android-$tier-top.png"
  adb shell input swipe 540 1800 540 300 400
  sleep 2
  adb shell input swipe 540 1800 540 300 400
  sleep 3
  adb exec-out screencap -p > "shots/android-$tier-scrolled.png"
done
adb logcat -d | grep -iE "chromium|iv31|AndroidRuntime|FATAL" | tail -200 > shots/logcat.txt || true
ls -la shots
