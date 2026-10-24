# Maintaining iv31

This is the working guide for iv31: how the project is laid out, how a release happens, and the rules that keep it working. It is written for the owner and for Claude when the repository is attached to a Claude Project.

## What iv31 is

An offline Pokémon IV calculator. The whole app is one web page (`src/index.html`) with its data injected at build time, running inside [Neutralino](https://neutralino.js.org) 6.10.0, which uses the system's own web engine:

| Platform | Web engine | Package |
| --- | --- | --- |
| Windows 10/11 | Edge WebView2 | NSIS installer `iv31-Setup-<v>.exe.zip` |
| macOS 10.15+ (Intel, Apple Silicon) | Safari WebKit | `iv31-<v>-mac.zip` containing `iv31.app` |
| Linux x64 / arm64 | WebKitGTK 4.0 or 4.1 | `.deb`, AppImage, `.tar.gz`, plus an apt repository |

It covers every main-series game from Red/Blue/Yellow to Scarlet/Violet. Gen I–II use DVs (0–15), Stat Experience and no natures; Gen III+ use IVs, EVs and natures.

## Repository layout

| Path | What it is |
| --- | --- |
| `src/index.html` | The app: HTML, CSS and JavaScript in one file. Has placeholders `__LOC__`, `__DEX__`, `__SP__`, `__PROG__` for data. |
| `src/data/pokedex.json` | Every Pokémon: stats, evolutions, EV yields, types, older-generation stats (`eras`, `pre6`, `gen1`, `gen1types`). |
| `src/data/locations.json` | Wild locations per game version. |
| `src/data/secret-power.json` | Secret Power ground types for every Gen III area. |
| `src/data/progression.json` | The order places are reached in each game group (Red/Blue/Yellow, Gold/Silver/Crystal, … Sword/Shield), used to sort Found in. Add new place names here when location data changes. |
| `src/release.json` | One-line summary shown in the in-app update bar. |
| `app/neutralino.config.json` | App id, version, window settings and the native-API allow list. |
| `app/resources/` | Fonts, icon and the Neutralino client library `js/neutralino.js`. |
| `tools/build.py` | Builds `updates/iv31-<v>.neu`, deletes older packages and rewrites `updates/manifest.json`. |
| `updates/` | The update channel every installed copy reads. |
| `updates/runtime/<id>/` | The program file for each system (Windows, Mac, Linux x64/arm64). `updates/runtime/current` names the one every package and update uses. |
| `release-notes/<v>.md` | The GitHub release text for each version. |
| `packaging/` | Scripts that build each platform's download, and `release.sh` that publishes them. |
| `.github/workflows/release.yml` | Publishes releases and the apt repository. |
| `.github/workflows/runtime.yml` | Builds the Catalina-compatible Mac runtime. |
| `apt` branch | The apt repository. Generated; never edit by hand. |
| `app/web/` | Website-only files: `manifest.webmanifest`, icons, and `sw.js` (offline cache; `__VERSION__` and `__FILES__` are filled in by the build). |
| `tools/build_web.py` | Builds the website into `dist/web`. |
| `.github/workflows/pages.yml` | Publishes `dist/web` to GitHub Pages when a release is pushed. |

## Releasing a new version (order of work)

1. **Make the change** in `src/index.html` or `src/data/`.
2. **Bump the version in two places** so they match:
   - `app/neutralino.config.json` → `"version"`
   - `src/index.html` → `const APP_VERSION = "…";`
3. **Write `release-notes/<v>.md`** (what's new, then install steps for each platform) and update the one-line `src/release.json`.
4. **Build** (Terminal, in the repository folder):
   ```bash
   python3 tools/build.py
   ```
   It refuses to run if the two versions differ or the release notes are missing. It produces `updates/iv31-<v>.neu` and a new `updates/manifest.json`.
5. **Test** the page: open `dist/stage/resources/index.html` through a local web server, or run the Playwright tests (see Testing).
6. **Update `CHANGELOG.md`**, and `README.md` / `SECURITY.md` if instructions or file names changed.
7. **Commit and push to `main`.** The Release workflow then, by itself:
   - builds the Windows installer, Mac zip and all Linux packages from `updates/iv31-<v>.neu`,
   - creates the GitHub release with all files and their SHA-256 checksums,
   - updates the apt repository (needs the `APT_SIGNING_KEY` secret).
8. **After the workflow finishes**, copy the checksums from the release page into `CHANGELOG.md` and push again.

Pushing the new `updates/manifest.json` is what makes installed copies offer the update, so only push it when the release is ready.

## How updates reach people

**Website** (https://scooby5328-design.github.io/iV31/): the **Website** workflow rebuilds and deploys it whenever `updates/manifest.json` changes, so it always matches the latest release. Browsers load the page from the network first and fall back to the offline cache; a new deployment changes `sw.js`, and open pages show "A new version of iv31 is ready". GitHub Pages must be turned on once: repository **Settings → Pages → Build and deployment → Source: GitHub Actions**.


| Install | How it updates |
| --- | --- |
| Windows installer, Mac app, Linux tarball | In-app: downloads `updates/iv31-<v>.neu` and, when `runtime.txt` in the install folder doesn't match the manifest's runtime id, the program file for that system too. Every file is checked against its SHA-256, written as `*.new`, size-checked, then renamed into place (the old program is kept as `*.old` until the next start). Writes `runtime.txt`, restarts, and deletes the leftovers. Never write `resources.neu` or the program directly. |
| Linux `.deb` | `sudo apt update && sudo apt upgrade`. The app tells the user this instead of self-updating (it lives in read-only `/opt/iv31`). |
| AppImage | The app tells the user to download the new AppImage. |
| Windows 1.3.0 | Can't self-update (token bug). Needs the installer once. |

A manifest can set `"installer": true` in `data` when a release changes the runtime itself, so every copy is told to download the full package instead.

## Rules that keep it working

- **Update URL.** `UPDATE_BASE` in `src/index.html` and in `tools/build.py` must stay `https://raw.githubusercontent.com/scooby5328-design/iv31/main/updates/`. Installed copies only accept updates whose URL starts with it.
- **Never load `__neutralino_globals.js`.** The runtime injects it; loading it twice breaks the one-time token (`NE_CL_IVCTOKN`, the 1.3.0 bug).
- **Native API allow list.** New Neutralino calls must be added to `nativeAllowList` in the config, or they fail silently. Currently: `filesystem.writeBinaryFile`, `filesystem.writeFile`, `filesystem.readFile`, `filesystem.getStats`, `filesystem.move`, `filesystem.remove`, `filesystem.setPermissions`, `os.execCommand`, `app.exit`, `window.setMainMenu`. File access is limited to the exact files an update swaps.
- **Older web engines.** The page must work in Safari 15 (Catalina) and older WebKitGTK. `tools/build.py` adds `rgba()` fallbacks for every `color-mix()` automatically. Avoid CSS nesting, `@container`, `:has()` and other features newer than Safari 15.4.
- **Mac menu bar.** The app sets its own menu on macOS (Quit, Edit with Copy/Paste, Window). Without it, ⌘Q and ⌘C/⌘V do nothing.
- **App stays offline** apart from the update check. No analytics, ads or outside requests.
- **No code comments** in files written for the owner; explanations go in docs and chat.

## Platform details

**Windows.** `packaging/iv31.exe` is the Neutralino Windows runtime; `stamp.mjs` writes the version into it and `iv31.nsi` builds the installer. Installs per user, no admin rights.

**Changing the runtime.** Put the new program files in `updates/runtime/<new id>/` with the same four names, write the new id into `updates/runtime/current`, and release. Installed copies replace their program on the next update.

**macOS.** Official Neutralino builds need macOS 14, so `runtime.yml` compiles Neutralino 6.10.0 for 10.15 (Intel) and 11 (Apple Silicon), with ScreenCaptureKit weak-linked. It publishes to the `runtime-6.10.0-mac10.15` release; `build-mac.sh` downloads it and checks a pinned SHA-256. To change Neutralino versions, edit `runtime.yml`, run it, then update the URL and checksum in `build-mac.sh`. The app isn't signed with an Apple developer certificate, so users run `xattr -dr com.apple.quarantine /Applications/iv31.app` once. It must live in Applications for updates to install.

**Linux.** Uses the official Neutralino Linux binaries (glibc 2.25+, loads WebKitGTK 4.1 or 4.0 at run time). `build-linux.sh` makes the tarball, `.deb` and AppImage for x64 and arm64. The `.deb` installs to `/opt/iv31`, adds `/usr/bin/iv31`, a desktop entry and icons, and drops the apt key and `/etc/apt/sources.list.d/iv31.sources` so updates come through apt.

**apt repository.** Served from the `apt` branch at `https://raw.githubusercontent.com/scooby5328-design/iV31/apt`, suite `stable`, component `main`, architectures `amd64 arm64`. `publish-apt.sh` rebuilds it with the last three versions' `.deb` files and force-pushes the branch. Signed with key `85840C540F38B42EAECBC17A6DB7B8ABE65CE7B9`; the private key is the `APT_SIGNING_KEY` Actions secret. Losing it means every Linux user has to install a new key.

**Android (the base for iv31 mobile).** `android/` is a Kotlin app (package `com.chili.iv31`, min Android 7, target API 36) that shows the same page from its assets in a WebView. `tools/build_android.py` copies the built page in. The page sees `window.iv31Android` and switches tiers: free = one IV calculation, EV table and Favorites without locations; Full = everything plus party comparison (30) saved in the app. Full is the one-time Google Play product `iv31_full` (Play Billing 8, `Billing.kt`). The desktop app is never limited; the web page opened on a phone gets the free tier, with a note pointing to the Android app. The **Android** workflow builds a test APK and a Play bundle on every push, runs both tiers on an emulator and posts screenshots to the `android-ci` pre-release. Debug builds accept `--es tier free|pro` to force a tier. Play bundles are signed only when the `ANDROID_*` secrets are set. Android updates come from Google Play, so the in-app updater is off there. Inside the app the page sets `IS_STORE` and the `store` class on the page: a bottom tab bar on narrow screens, the neutral title "iv31 · IV Checker", "Saved on this device" wording and a Google Play update message. Any future phone platform should plug into this same bridge (`window.iv31Android`-style object with `isPro`, `price`, `buy`, `restore`) rather than a second app framework.

## Testing

- **Build check:** `python3 tools/build.py`
- **Page tests:** Playwright scripts that load `dist/stage/resources/index.html`, fake the Neutralino globals and check the calculator, the tabs and every updater path (Windows, Mac, apt, AppImage, web page).
- **Linux:** install the `.deb` with `sudo apt install ./iv31_<v>_amd64.deb` and run `iv31`; on a headless machine use `xvfb-run`.
- **Mac:** unzip into Applications and open it; check the version chip, the update check and the menu bar.
- **Android:** check the screenshots on the `android-ci` pre-release after each push, or install `iv31-x.y.z-android-test.apk` on a phone (purchases only work in a Play-installed build).
- **Calculations:** check a known case per generation, for example a Gen I Pikachu at level 50 with DVs 7/10/13/4 should show HP DV 10.

## Secrets and keys

| Name | Where | Used for |
| --- | --- | --- |
| `APT_SIGNING_KEY` | GitHub → Settings → Secrets and variables → Actions | Signing the apt repository |
| `ANDROID_KEYSTORE_BASE64`, `ANDROID_KEYSTORE_PASSWORD`, `ANDROID_KEY_ALIAS`, `ANDROID_KEY_PASSWORD` | Same place (not set yet) | Signing the Google Play bundle with the upload key |
| `GITHUB_TOKEN` | Automatic | Creating releases, pushing the `apt` branch |

## Version history in short

- 1.1.0 Desktop app. 1.2.0 Auto-updater. 1.3.0 Game picker, Types, berries, favorites (token bug). 1.3.1 Token fix.
- 1.4.0 Gen I–II, single game list, Nature Power, Secret Power fix.
- 1.4.1 First Mac release, Mac menu bar.
- 1.4.2 Linux packages and apt repository, macOS back to 10.15, color fallbacks.
- 1.4.3 Party comparison (30 on desktop; `PARTY_DESKTOP_MAX` in `src/index.html`). Since then the web page on phones uses the Android free tier.
- 1.5.0 Updates replace the program too, in place, then restart; phone web page uses the free tier.
- 1.5.1–1.5.2 Sort the EV table by Found in, in story order; fixed Farfetch'd, Sirfetch'd, Flabébé names.
- 1.5.3 Story orders checked against walkthroughs.
- 1.5.4 Story order is an on/off toggle that stays on while filtering by EV or sorting by a stat.
- 1.6.0 Unknown EVs: `solveIvs` / `solveDvs` in `src/index.html` find IV and EV (or Stat Exp) ranges together; EVs gained panel in EV Training.
- 1.6.1 A "?" tip on every section (`TIPS` in `src/index.html`). New sections need an entry there.
- 1.6.2 Powers tab (view id still `secret`): `renderSecret` draws Secret or Nature Power by `state.pwSub`, `renderPowerHp` draws the Hidden Power chart.
- 1.6.8 Field-guide redesign (theme tokens and the layer at the end of the main `<style>`; `--pixel` and `--lcd` fonts), data page view `dex` (`renderDex`), app history `navHist`/`navGo` behind Back/Forward and `window.iv31NavBack` for Android.
- 1.7.0 Device frame: markup `.device` > `#screen` (the scrolling main screen; use `getY`/`setY`, not `window.scrollY`), `.dev-side.left` (game picker, D-pad, SOUND) and `.dev-side.right` (version, clock, A/B, DAY/NIGHT) since 1.7.1. Sounds are `sfx(...)` tones; the start-up screen is `runBoot`. Desktop scrolls inside `#screen` from 721px wide; below that the page scrolls normally.
- 1.8.0 Website on GitHub Pages (`tools/build_web.py`, `app/web/`, `pages.yml`); Favorites compact list (`favRow`); Hidden Power calculator in Powers; matchup checker opens data pages; style consolidation (overridden declarations removed; verify with before/after screenshots); accessibility and contrast fixes.
- 1.8.1 Poké Data tab (view id still `evs`, hash `#pokedata`): `renderSheet` with type, weakness and matchup columns and filters kept in `pd` (localStorage `iv31-pokedata`); matchup checker in `#mcwin`; EVs gained and berries in the IV Calculator tab.
- 1.8.5 Foldable sections (`setFold`, `iv31-folded`), SIZE control (`--ui` zoom on `#screen` content, `iv31-size`, `#screen.narrow` stacks tiles), D-pad half-screen scroll.
- 1.8.6 Phone fixes: data page header stacks, floating ? buttons measure wrapped titles.
- 1.8.7 Folder tabs: `#screen` is a grid at ≥721px (tab column + `.desk` panel); phones get top tabs labelled from `data-short`; Android keeps bottom tabs. Table wrappers use `overflow-x:clip` (no inner scroller, sticky headers follow `#screen`); `fitWide` adds `.xscroll` when a table still overflows at its minimum zoom. `.win-body` uses `overflow:clip` so sticky headers work.
- 1.8.8 Sliding side tabs: collapsed `.bar-top` is 58px wide and tabs widen over the page on `:hover` / `:has(:focus-visible)`; `#tabToggle` sets `#screen.tabs-open` (saved in `iv31-tabs`) via `setTabsOpen`. Tab symbols are inline `svg.ti`.
- 1.8.9 Hover/focus expansion removed: collapsed tabs are 46px icon squares (active one outlined), full tabs only with `#screen.tabs-open`.
- 1.8.10 Cleanup: all tab bar CSS lives in one block (base, `min-width:721px`, `max-width:720px`, store `max-width:640px`); `build.py` prunes older `.neu` files.
