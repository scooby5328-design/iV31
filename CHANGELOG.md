# Changelog

All notable changes to iv31 are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Planned
- macOS and Linux builds
- Side-by-side comparison of saved Pokémon

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

[Unreleased]: ../../compare/v1.3.0...HEAD
[1.3.0]: ../../releases/tag/v1.3.0
[1.2.0]: ../../releases/tag/v1.2.0
[1.1.0]: ../../releases/tag/v1.1.0
[1.0.0]: ../../releases/tag/v1.0.0
