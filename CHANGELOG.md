# Changelog

All notable changes to iv31 are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Planned
- Side-by-side comparison of saved Pokémon

## [1.5.0] - 2026-10-16

### Added
- In-place program updates: the manifest lists the program file for each system (`updates/runtime/<id>/`), and installed copies replace their program in the install folder when its id changes, then restart. `runtime.txt` next to the program records which one is installed.

### Changed
- The web page opened on a phone uses the same free tier as the Android app (one IV calculation, EV table without locations).
- All packages take their program file from `updates/runtime/` instead of downloading it at build time.

## [1.4.4] - 2026-10-16

### Fixed
- Updates are written to `resources.neu.new`, size-checked, then renamed over `resources.neu`, so an interrupted update can't leave an empty file (which made the Mac app open the Neutralino website).
- Relaunch after an update works on Mac and Linux (the command allow list only matched `iv31.exe`), and on Windows paths with backslashes.

### Checksums (SHA-256)

```
b0ff3eb6c56aa1fab29f50196f6bffc461b22b118672c0d4f4d60b4b8279c3b1  iv31-Setup-1.4.4.exe
d86aec13e3ab49c9ad1a940ed1ccbc20c9380a77c026c836ad942a74c52f7f2b  iv31-1.4.4-mac.zip
a61aa675f83f86d688916b4c95611214709b698936b234b9d8e7394845482d9f  iv31-1.4.4-linux-x64.tar.gz
e7fdf78feb9389377e3d3e99a0160ceaf8ace0c2ddfb66f85a80554b2a35885d  iv31-1.4.4-linux-arm64.tar.gz
8a6bb8bdb4d391e0db946fc22df121e5e92959966ae1b4fd36f167ca1f8ceeb8  iv31_1.4.4_amd64.deb
9bbde78ba6eef4ab2da3f8f9a0a7c84447cd6c15bfcd7b6b36915c23320a5537  iv31_1.4.4_arm64.deb
82be61dc71f7cb474d0ecfa003d0c0a4054a926b291d8d42cd29465df1c81be6  iv31-1.4.4-x86_64.AppImage
1482d1423e14d7593c3b5ee9895152385b457cb8cbaa4a02b832a96a461681b8  iv31-1.4.4-aarch64.AppImage
```

## [1.4.3] - 2026-10-16

### Added
- Party comparison panel in the IV Calculator: add party members with **+**, enter each one's Summary screen, and compare their IVs, totals and Hidden Power in one table. Best value per stat is underlined; key stats are highlighted. Works with Gen I–II DVs too.
- Up to 30 party members in the desktop app; up to 3 on the web page on a phone.

### Checksums (SHA-256)

```
a175696910e1676392b6a8fd9d1e5bd2148284ed3165cbdcb1acae40e2605559  iv31-Setup-1.4.3.exe
80030747211bb745cedfed25cfc30353a9128c72329382a78ab56e4fbd58aafc  iv31-1.4.3-mac.zip
670748db61850026779e2ccccae08ac355479fb919508e4793c7fd0fba23c034  iv31-1.4.3-linux-x64.tar.gz
537fa79ace18571c9f82bce00162847551c4a56254825eb6d20064a5ed68f64a  iv31-1.4.3-linux-arm64.tar.gz
034fd562ed16cf39f3a660af08e28f759e2577399f8699b93d9172bb7a666c90  iv31_1.4.3_amd64.deb
f2e7d784c4dfa7f6d8b8ddd15fb35536685e2655355c2cf413935c74c4d4a6e2  iv31_1.4.3_arm64.deb
f7d52cda86eff3357a36f188bf96f4b98325841f97b17f134e1945a3d1d7b691  iv31-1.4.3-x86_64.AppImage
dfbc4772b5ce51ef1159647115f4b93c55b7992a582b4404cdff6349d66aba17  iv31-1.4.3-aarch64.AppImage
```

## [1.4.2] - 2026-10-16

### Added
- Linux builds for x64 and arm64: `.deb`, AppImage and `.tar.gz`.
- A signed apt repository. Installing the `.deb` adds it, so updates come through `apt upgrade`.
- On Linux, the update bar tells apt and AppImage users how to update instead of offering to install over a read-only copy.

### Changed
- The Mac app runs on macOS 10.15 Catalina and newer. It uses Neutralino 6.10.0 built from source for older macOS (see the `Mac runtime` workflow).
- Colors that used `color-mix()` now have fallbacks for older Safari and WebKitGTK.

### Checksums (SHA-256)

```
947a6a67e8c922d7f3020ccd8f523047f39e423ee3a839565e57b0942db5de34  iv31-Setup-1.4.2.exe
ac03a6598374eb6842918af2d906e948fba9e710224e09817d4a536367144865  iv31-1.4.2-mac.zip
263719ba4c58e503cf8dcf54ea1269e6337a1073c3e65d90ed4a787c5a5e635e  iv31-1.4.2-linux-x64.tar.gz
9b75a93286e0ee00397be8e931c95a2af69bf8fcd89571fee30490fc90fd844d  iv31-1.4.2-linux-arm64.tar.gz
d5dfa543e7bcda434e67fdd74956c9b48c8d4389cf848c6af300da26610a4844  iv31_1.4.2_amd64.deb
7889e9d349874a095fe2c0f73cda557211129b44ee54aa972264b6ce27d24ede  iv31_1.4.2_arm64.deb
e70cececed39bda2dfa91319f4244e1b9aaa2168e7f05d9b6632e6f37a8679c1  iv31-1.4.2-x86_64.AppImage
95a092c4deddcf8a589c5382eb67d90005dc8d88d2ca02edd4a9dc8beb0f44c9  iv31-1.4.2-aarch64.AppImage
```

## [1.4.1] - 2026-10-16

### Added
- macOS app for macOS 14 or newer (Intel and Apple Silicon), published as `iv31-<version>-mac.zip` on each release. It uses the same update channel as Windows.
- Standard Mac menu bar (Quit, Hide, Edit with Copy and Paste, Window).

### Changed
- Update messages no longer mention a Windows installer on a Mac, and a failed update on a Mac explains that iv31 needs to be in the Applications folder.

### Checksums

`iv31-Setup-1.4.1.exe` SHA-256:

```
7fcb792bbbb595643c9fa2bf7cd35d273d9a77506fa541a8ac032693672e1438
```

`iv31-1.4.1-mac.zip` SHA-256:

```
b1aa40bfd4f8b8521c545b31144d020676ba28d125e22e1b5fd7085d40f64809
```

## [1.4.0] - 2026-10-16

### Added
- Gen I and Gen II: Red, Blue, Yellow, Gold, Silver and Crystal. The calculator uses DVs (0–15) with the HP DV derived from the other four, Stat Experience instead of EVs, no natures, one Special stat in Gen I and a shared Special DV in Gen II. Gen II shows Hidden Power and whether the DVs are shiny.
- Gen I type chart (no Dark or Steel; Ghost doesn't affect Psychic; Bug and Poison are super effective against each other; Ice is neutral against Fire).
- Gen I and II base stats, types and wild locations in every tab. The EV Training table shows Stat Exp yields for these games.
- Nature Power in the Secret Power tab for Gen III to VII.

### Changed
- The generation and version dropdowns are one list grouped by generation, so every game is visible at once.

### Fixed
- Gen III Secret Power on plain ground (Slam) has no extra effect. It was listed as "may paralyze".

### Installer checksum

`iv31-Setup-1.4.0.exe` SHA-256:

```
5d650e7c0aea9932543290de81e41002540d7676fac00faccddc2cd7c23c9e9c
```

## [1.3.1] - 2026-10-16

### Fixed
- 1.3.0 showed `NE_CL_IVCTOKN: Neutralinojs application cannot connect with the framework core` and couldn't install updates, because the page loaded the app's connection token a second time. The extra load is removed.

### Note
- If you have 1.3.0, it can't install this update by itself. Download the 1.3.1 installer from the Releases page and run it once; it installs over 1.3.0 and keeps your saved data. People on 1.2.0 update straight to 1.3.1 from inside the app.

### Installer checksum

`iv31-Setup-1.3.1.exe` SHA-256:

```
75336b4776bbf7f4e7574cf284bd3e7241536fa03cc56016e72babfbb0644b35
```

## [1.3.0] - 2026-10-16

### Added
- One game picker in the top bar that sets the generation and version for every tab.
- Types tab: weakness and resistance chart for the selected generation (with Gen III physical/special marks and no Fairy before Gen VI), and a matchup checker for any Pokémon or pair of types.
- EV-lowering berries table in EV Training: the stat each berry lowers, how it works in the selected game (not usable in Ruby, Sapphire, FireRed or LeafGreen), the matching vitamin, and where to get them.
- "Found in" column in the EV yield table with wild locations for the selected version, search by place, and a filter for Pokémon found in that version.
- Favorites: tap ☆ to save a Pokémon and see all its details on one card.
- Pokémon types and weaknesses in the IV readout.
- The app's source code and build script (`src/`, `app/`, `tools/`).

### Changed
- Five tabs: IV Calculator (with the EV and Hidden Power calculators and a fold-away guide), EV Training, Types, Secret Power and Favorites. The separate generation pickers on each tab are gone.
- The IV calculator starts empty.

### Installer checksum

`iv31-Setup-1.3.0.exe` SHA-256:

```
aa445edac2b194619f2d0c86165bb2bf0b6138ef318a5cbd12882ef2be922e60
```

## [1.2.0] - 2026-10-15

### Added
- Auto-updater:
  - Checks GitHub for a newer version a few seconds after iv31 starts. This can be turned off in the Guide.
  - Shows a bar with the new version and its notes, with **Update now**, **Skip this version** and **Later**.
  - Downloads the update, checks its SHA-256 fingerprint, installs it and restarts iv31. Saved favorites and EVs are kept.
  - Click the version number in the top bar to check for updates any time.
- `updates/` folder in the repository with the update information (`manifest.json`) and update files.
- Complete uninstall: removing iv31 now also deletes its saved favorites, EVs, settings and browser cache, leaving nothing behind.

### Changed
- The app can now use three native functions (write its own app file, relaunch itself, exit). Everything else stays blocked.
- The page's Content Security Policy is now applied (it was being ignored before) and allows connecting to GitHub for updates.

### Note
- Version 1.1.0 can't update itself. Install 1.2.0 once with the installer; updates after that happen inside the app.

### Installer checksum

`iv31-Setup-1.2.0.exe` SHA-256:

```
daae35810434ab15252ecccdd61736a567692c77978b382b83a79bd1ab68e40e
```

## [1.1.0] - 2026-10-13

### Added
- EV calculator next to the IV readout:
  - Track EVs per stat, with the 510 total and per-stat limits (255 in Gen III to V, 252 from Gen VI).
  - Shows the stat points the EVs give at the Pokémon's level and at level 100, the EVs needed for the next point, and any wasted EVs.
  - Add EVs by Pokémon defeated, with Macho Brace, Power items and Pokérus, or by vitamins.
  - Load EVs from, or send them to, the Summary screen.
  - A table showing how many stat points a number of EVs gives at different levels.
- Hidden Power calculator:
  - Type, power, and (in Gen III) physical or special category for any six IVs.
  - Can load IVs from the IV readout.
  - Table of the highest IVs that give each type.
- Secret Power tab:
  - Every area in Ruby/Sapphire, Emerald and FireRed/LeafGreen, with the ground types it has and the move Secret Power turns into there, worked out from the games' map data.
  - Terrain tables for Gen IV to VII.
- New guide sections for the EV calculator, Hidden Power and Secret Power.

### Changed
- The "EVs" tab is now called "EV yield".

### Installer checksum

`iv31-Setup-1.1.0.exe` SHA-256:

```
b61a5022c4b213000bb7940ee3b56d3b22eaf8bfe7e1be721102c2fcb42b3c03
```

## [1.0.0] - 2026-10-12

### Added
- IV calculator covering the full National Pokédex, listed in Pokédex-number order
- Possible IV ranges when a single value can't be determined
- Suggested natures for each Pokémon
- Highlighting of each Pokémon's key stats
- EV yield tab with a table of effort values for every Pokémon
- Local saving of entries between sessions
- Catppuccin-based desktop theme
- Lightweight Windows desktop app built on Neutralinojs
- Windows installer with Start menu and optional desktop shortcuts, per-user install and a full uninstaller
- WebView2 check during install

### Installer checksum

`iv31-Setup-1.0.0.exe` SHA-256:

```
aef35b57155124b152c1d4c0558ec121ae7dd1b68b1f11e2d5181897a34cc4b8
```

### Changed
- Expanded from the original Gen III (Hoenn) Pokédex to the full National Pokédex
- Renamed from "Pokédex IV Checker" to iv31

[Unreleased]: ../../compare/v1.3.1...HEAD
[1.3.1]: ../../releases/tag/v1.3.1
[1.3.0]: ../../releases/tag/v1.3.0
[1.2.0]: ../../releases/tag/v1.2.0
[1.1.0]: ../../releases/tag/v1.1.0
[1.0.0]: ../../releases/tag/v1.0.0
