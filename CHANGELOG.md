# Changelog

All notable changes to iv31 are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Planned
- Side-by-side comparison of saved Pokémon

## [1.5.3] - 2026-10-16

### Changed
- `src/data/progression.json` checked against Bulbapedia's walkthrough appendix for each game and corrected (Kanto post-game order in Gen II/IV, Sinnoh mid- and post-game, early Hoenn sea routes, Unova Routes 17–18, Kalos Route 22, Alola and Galar post-game areas).

### Checksums (SHA-256)

```
458cdecd89ccf1e60c67741f8d287a777fdf6c66d4e6dc2734dce55cb0dfa560  iv31-Setup-1.5.3.exe
fb50a752687eb4864750b12726a0131e5369d29230961af7cc183fcbb85547f6  iv31-1.5.3-mac.zip
ed6cc93fb2ad0545042b97222add306bdf0057cdbe082932469e8d88fcf61bac  iv31-1.5.3-linux-x64.tar.gz
27192d128661a6a8ab12814365bfa9518b3f64a5276c0f980a66604bdc9dad25  iv31-1.5.3-linux-arm64.tar.gz
98c81f8c39249677277b6bfc525b768f7261961d02822e0d7ef8a961c51d46a7  iv31_1.5.3_amd64.deb
537d23f3d71fa07ce6290425d6b70fd687e8875a6cb20ef948ecfd98685e811a  iv31_1.5.3_arm64.deb
8e6458e3b53f24bdffa3bf5d1201dfe8a1715155cc0fcf0017019acea1ee0379  iv31-1.5.3-x86_64.AppImage
46f98537fbed4912a3977f09431592e0f81491fd74f270ed5428366e1474ef6f  iv31-1.5.3-aarch64.AppImage
```

## [1.5.2] - 2026-10-16

### Changed
- Sorting by **Found in** and each Pokémon's list of places follow the order areas are reached in each game (`src/data/progression.json`, one list per game group). Places missing from a list go after it: numbered routes in number order, then the rest alphabetically.

### Checksums (SHA-256)

```
c04e5370ec20261cc7a8922dac97449c8223cdd47349647fadfa5dce6f1fc435  iv31-Setup-1.5.2.exe
61d49346805cb45c436c6861b3a774f296b51702e6fdae1305cd3371e1070d2b  iv31-1.5.2-mac.zip
fae8eda6f1d47c8c112c8a07b0b5c97211ebbb8bf0b981f2ed0eb597ef794375  iv31-1.5.2-linux-x64.tar.gz
f91d3c1d6b22865592e6bd4dd1772ee147602e05420541b5ebd459cf31f81698  iv31-1.5.2-linux-arm64.tar.gz
bc7ec0a82228d8fb733719649b4e7d5cddb176de5207a9f7e165afe3e2f524c4  iv31_1.5.2_amd64.deb
e3a148482dcea9b504ee6fb6c0e4f50684077b18a481c9a925bbae0df535e77a  iv31_1.5.2_arm64.deb
75b5906796874cb86a2589969ffad25dfcce24e79a5ddaab1e0ebe071f924710  iv31-1.5.2-x86_64.AppImage
3e76a585e02f9494cc3e9e3f881814968ed7f6e3c20db2f71d377fb80496db5a  iv31-1.5.2-aarch64.AppImage
```

## [1.5.1] - 2026-10-16

### Added
- The EV Training table can be sorted by the **Found in** column: route number order first, then other areas alphabetically, Pokémon not found in the wild last.

### Fixed
- Farfetch'd, Sirfetch'd and Flabébé showed escaped characters (`\u2019`, `\u0301`) in their names.
- Name searches ignore accents and treat curly and straight apostrophes the same.

### Checksums (SHA-256)

```
775e2c8390b1c4a065b0beaca3b2baa93515e78ac357c5f954d6421b6f2c078f  iv31-Setup-1.5.1.exe
a541097e7317ee18faae7b92a5aeeb625de913b859e8240dea75f892a5bc0d5e  iv31-1.5.1-mac.zip
88b82fc91a328c0b2de6781141136f1c3761f82156c5f0c11f520126c70a6471  iv31-1.5.1-linux-x64.tar.gz
bdea9f9be447c99c1f613d3387db127c6d6304a5f5ac92bb99d9fb0ca468c7ce  iv31-1.5.1-linux-arm64.tar.gz
920386ec79056fc80b4e0aacb2d1b0fe261261fb9434083385aca26e184acde7  iv31_1.5.1_amd64.deb
5e1d3859206f02d2d60717db0e771d44953ce98cba7b02d453c6741b85e9715b  iv31_1.5.1_arm64.deb
a106d7eb3abcf06ce23577d117145dd392abbc66b3494bba61c9b4d2cef68bdf  iv31-1.5.1-x86_64.AppImage
9ced38ad4d2e44407357a65f3532b0d9f92ecbd9e309e4dee7eef17575c0a5e2  iv31-1.5.1-aarch64.AppImage
```

## [1.5.0] - 2026-10-16

### Added
- In-place program updates: the manifest lists the program file for each system (`updates/runtime/<id>/`), and installed copies replace their program in the install folder when its id changes, then restart. `runtime.txt` next to the program records which one is installed.

### Changed
- The web page opened on a phone uses the same free tier as the Android app (one IV calculation, EV table without locations).
- All packages take their program file from `updates/runtime/` instead of downloading it at build time.

### Checksums (SHA-256)

```
a7e6a69c3ee53f8ad4c756772dcae5b4d22c8ab9c61c74df7e99986c96d55d60  iv31-Setup-1.5.0.exe
e23f549a956f0d628d67cbb5a4f651e3546a5f3d4083c715772316b834df735d  iv31-1.5.0-mac.zip
d5e9f391360dd7ed94934ab7b98daa7c4ffdbc8263bced82ada38aecd851807f  iv31-1.5.0-linux-x64.tar.gz
497d52137de2df68009edf9fb697f42a2419b7aac9dc2796fc4177e3afe370c3  iv31-1.5.0-linux-arm64.tar.gz
1c1bdb87590f1763712a78dcfb90e3af562af4f2b70b9f5e47228e9410f44110  iv31_1.5.0_amd64.deb
4e14415f1fd5d15adc34bd8d1e26040922638ab0be5cda23555aa9ce02563fe1  iv31_1.5.0_arm64.deb
7c2bec85cce29ff46c48a461ef936bd2619b7403354aae35cc9698b3eede8077  iv31-1.5.0-x86_64.AppImage
c64fce63264a8459118fe8c4dc79b91a74b5d9717b765e03c60d2107a4f055b0  iv31-1.5.0-aarch64.AppImage
```

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
