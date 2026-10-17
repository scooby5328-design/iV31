<div align="center">

# iv31

**A fast, offline Pokémon IV calculator for the whole National Pokédex.**

Pick a Pokémon, enter its level and stats, and iv31 tells you its individual values, the nature that suits it best, and which stats matter most. It also has an EV calculator, a Hidden Power calculator, an EV yield table with wild locations, EV-lowering berries, a type matchup chart, a Secret Power and Nature Power guide for every area in the Gen 3 games, and favorites. It covers every main game from Red, Blue and Yellow to Scarlet and Violet.

[![Latest release](https://img.shields.io/github/v/release/scooby5328-design/iV31?label=latest&color=f5c2e7)](https://github.com/scooby5328-design/iV31/releases/latest)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-89b4fa)](#install)
[![License: MIT](https://img.shields.io/badge/license-MIT-a6e3a1)](LICENSE)
[![Offline](https://img.shields.io/badge/works-offline-cba6f7)](#privacy)

[Download the latest version](https://github.com/scooby5328-design/iV31/releases/latest) · [Report a bug](../../issues/new?template=bug_report.yml) · [Request a feature](../../issues/new?template=feature_request.yml)

</div>

---

## Contents

- [Features](#features)
- [Install](#install)
- [How to use](#how-to-use)
- [How the math works](#how-the-math-works)
- [Privacy](#privacy)
- [What's in this repository](#whats-in-this-repository)
- [Building from source](#building-from-source)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Security](#security)
- [License and credits](#license-and-credits)

## Features

- **Full National Pokédex** listed in Pokédex-number order, from Bulbasaur onward.
- **IV calculation** from level, nature and current stats, with the possible IV range shown when a single value can't be pinned down.
- **Gen I and II support** for Red, Blue, Yellow, Gold, Silver and Crystal, using their own rules: DVs from 0 to 15 (with the HP DV worked out from the others), Stat Experience, no natures, Gen I's single Special stat, and Gen II Hidden Power and shiny checks.
- **Suggested natures** for each Pokémon, based on its strongest stats.
- **Key stat highlighting** so you can see at a glance which stats a Pokémon is built around.
- **EV calculator** right next to the IV readout. Track EVs per stat, add them by Pokémon defeated (with Macho Brace, Power items and Pokérus) or by vitamins, and see how many stat points they give at your level and at level 100. It keeps you inside the 510 total and per-stat limits and warns about wasted EVs.
- **Hidden Power calculator** that shows the type, power and (in Gen III) physical/special category for any six IVs, plus a table of the best IVs for every type.
- **One game picker** in the top bar, grouped by generation, that sets the game for every tab.
- **EV Training tab** with a sortable table of the effort values every Pokémon gives when defeated and where to find it in the wild in your version, plus a table of the berries that lower EVs and where to get them.
- **Types tab** with a weakness and resistance chart for the selected generation (with or without Fairy) and a matchup checker for any Pokémon or pair of types.
- **Favorites** that collect everything about a Pokémon on one card: base stats, key stats, natures, weaknesses, EV yield, evolution line and locations.
- **Powers tab** with a Hidden Power chart (the IVs for every type, or the DV table in Gold, Silver and Crystal) and separate Secret Power and Nature Power charts listing every area in Ruby, Sapphire, Emerald, FireRed and LeafGreen with the ground types it has and what both moves turn into there, worked out from the games' map data. Gen IV to VII show the terrain table.
- **Saves your work** between sessions on your own computer.
- **Updates itself.** iv31 checks GitHub for a new version when it starts and can install it with one click. Updates are verified before they're installed, and you can turn the check off.
- **Works offline.** No account, no ads, no tracking. The only time it goes online is to check for updates.
- **Tiny.** Downloads are 1–3 MB because iv31 uses the web engine already built into the system.
- **Clean desktop look** inspired by modern Linux desktop setups, using the Catppuccin colour palette.

## Install

### Windows 10 / 11 (64-bit)

1. Open the **[latest release](https://github.com/scooby5328-design/iV31/releases/latest)** and, under **Assets**, download **iv31-Setup-x.y.z.exe.zip** (x.y.z is the version number).
2. Right-click the downloaded zip → **Extract All** → **Extract**, then double-click the **iv31-Setup** file inside.
3. Windows may show **"Windows protected your PC"**. This appears because the installer isn't signed with a paid code-signing certificate. Click **More info → Run anyway**.
4. Follow the setup screens. No administrator password is needed; iv31 installs for your user account only.
5. Launch iv31 from the Start menu or the desktop shortcut.

**Requirement:** Microsoft Edge WebView2 Runtime. Almost every Windows 10/11 PC already has it. If yours doesn't, the installer offers to open Microsoft's download page.

**Uninstall:** Settings → Apps → Installed apps → iv31 → Uninstall. It closes iv31 and removes it completely in a second, including your saved favorites, EVs and settings. Nothing is left behind.

### Updating

From version 1.2.0 on, iv31 updates itself:

1. A few seconds after it starts, iv31 checks GitHub for a newer version.
2. If there is one, a bar appears at the top with what's new. Click **Update now**.
3. iv31 downloads the update, checks its fingerprint, installs it and restarts. Your saved favorites and EVs are kept.

Click the version number in the top bar to check any time. To stop the automatic check, untick **Check for updates when iv31 starts** in the Guide.

If you have **1.1.0 or older**, install the latest version once with the installer above. It installs over the old version and keeps your saved data.

Older versions are kept on the **[Releases](https://github.com/scooby5328-design/iV31/releases)** page.

### macOS 10.15 (Catalina) or newer, Intel or Apple Silicon

1. Open the **[latest release](https://github.com/scooby5328-design/iV31/releases/latest)** and, under **Assets**, download **iv31-x.y.z-mac.zip**.
2. Double-click the zip in your Downloads folder. You get **iv31.app**.
3. Drag **iv31.app** into your **Applications** folder. It has to be there for updates to install.
4. iv31 isn't signed with a paid Apple developer certificate, so macOS blocks it the first time. Open **Terminal** (Applications → Utilities → Terminal) and paste this line, then press Return:

   ```bash
   xattr -dr com.apple.quarantine /Applications/iv31.app
   ```

   This removes the "downloaded from the internet" flag from iv31 only. If you'd rather not use Terminal: try to open iv31 once, then go to **System Settings → Privacy & Security**, scroll down and click **Open Anyway**.
5. Open iv31 from Applications or Launchpad.

**Uninstall:** quit iv31 and drag **iv31.app** from Applications to the Trash.

The Mac version updates itself the same way as the Windows version. On Catalina, install the latest Catalina and Safari updates first (Apple menu → System Preferences → Software Update), because iv31 uses Safari's engine.

### Linux (64-bit Intel/AMD or ARM)

iv31 needs GTK 3 and WebKitGTK, which most desktop distributions already have. There are three ways to install it.

**Ubuntu, Debian, Linux Mint, Pop!_OS and other apt-based systems (recommended).** Open **Terminal** and run these three lines one at a time:

```bash
curl -fsSL https://raw.githubusercontent.com/scooby5328-design/iV31/apt/iv31-archive-keyring.gpg | sudo tee /usr/share/keyrings/iv31-archive-keyring.gpg > /dev/null
curl -fsSL https://raw.githubusercontent.com/scooby5328-design/iV31/apt/iv31.sources | sudo tee /etc/apt/sources.list.d/iv31.sources > /dev/null
sudo apt update && sudo apt install iv31
```

The first line saves iv31's signing key, so apt can check that packages really come from this project. The second adds the iv31 repository. The third installs iv31. From then on, new versions arrive with your normal updates (`sudo apt update && sudo apt upgrade`). You can also download the **.deb** file from the [latest release](https://github.com/scooby5328-design/iV31/releases/latest) and open it with your software installer; it adds the same repository.

Uninstall with `sudo apt remove iv31`.

**AppImage (any distribution).** Download **iv31-x.y.z-x86_64.AppImage** (or **aarch64** for ARM), then in Terminal:

```bash
chmod +x iv31-*.AppImage
./iv31-*.AppImage
```

To update, download the new AppImage and delete the old one.

**Tarball (any distribution).** Download **iv31-x.y.z-linux-x64.tar.gz** (or **arm64**), extract it anywhere you can write to, such as your home folder, and run the **iv31** file inside. This version updates itself like the Windows and Mac versions.

If iv31 doesn't open, install WebKitGTK: `sudo apt install libwebkit2gtk-4.1-0` on Ubuntu/Debian, `sudo dnf install webkit2gtk4.1` on Fedora, or `sudo pacman -S webkit2gtk-4.1` on Arch.

## How to use

1. Choose a Pokémon from the list, or search by name or Pokédex number.
2. Enter its **level** and **nature**.
3. Enter the six stats shown on its summary screen (HP, Attack, Defense, Sp. Atk, Sp. Def, Speed).
4. Set **EVs** to **None yet** for a freshly caught or hatched Pokémon, **Has battled** if it has fought and you don't know its EVs, or leave **Not sure**. If you know its EVs, type them under **Known EVs**. When EVs are raising a stat, the readout shows the IV range and EV range that fit.
5. Read the IV for each stat. A range like `24–27` means more data is needed; level the Pokémon up once and enter the new stats to narrow it down.
6. Use the **EV calculator** panel to plan or track EV training. Add each Pokémon you defeat and it tallies the EVs and stat points for you. Click **Send EVs to Summary** so the IV readout accounts for them.
7. To compare several Pokémon, press **+ Add party member** in the **Party comparison** panel and fill in each one, or click **Copy from Summary screen**. The table lines up their IVs side by side (up to 30 in the desktop app, 3 on a phone).
8. Use the **Hidden Power** panel to check a Pokémon's Hidden Power, or load the IVs you need for a type.
9. Pick your game in the top bar. Every tab follows it.
10. Open **EV Training** to see which Pokémon to battle to train a stat and where to find them, or switch to **EV-lowering berries** to undo EVs. **EVs gained** at the top compares a Pokémon's stats before and after training and shows the EVs it earned.
11. Open **Types** to check what a Pokémon is weak to.
12. Open **Powers** for three charts: **Hidden Power** (the IVs that give each type), **Secret Power** and **Nature Power** (what each move turns into in every area).
13. Tap ☆ next to any Pokémon to keep it in **Favorites**.

## How the math works

iv31 uses the stat formulas from Generation III onward.

**HP**

```
HP = floor((2 × Base + IV + floor(EV / 4)) × Level / 100) + Level + 10
```

**Other stats**

```
Stat = floor((floor((2 × Base + IV + floor(EV / 4)) × Level / 100) + 5) × Nature)
```

`Nature` is 1.1 for a boosted stat, 0.9 for a lowered stat, and 1.0 otherwise. iv31 tests every IV from 0 to 31 against your numbers and shows each value that fits. Shedinja's HP is always 1 and is handled as a special case.

### Hidden Power

Each IV's lowest bit (odd or even) sets the type, and in Gen III to V each IV's second-lowest bit sets the power:

```
Type  = floor((a + 2b + 4c + 8d + 16e + 32f) × 15 / 63)
Power = floor((u + 2v + 4w + 8x + 16y + 32z) × 40 / 63) + 30
```

The letters go in the order HP, Attack, Defense, Speed, Sp. Atk, Sp. Def. From Gen VI on, the power is always 60.

## Privacy

iv31 does not collect, send or share any data about you.

- Everything runs locally on your computer.
- Saved entries are stored in the app's local browser storage on your machine only.
- The app's internal web server listens only on your own computer (`127.0.0.1`), never on your network.
- There are no analytics, telemetry or ads.
- The only internet connection is the update check, which downloads a small version file from this repository. Nothing about you is sent. You can turn it off in the Guide.

## What's in this repository

```
.
├── src/                       The app's page (src/index.html), its data and the update summary
├── app/                       App settings and bundled files (fonts, icon, runtime client)
├── tools/                     Build script that packs the app into updates/
├── updates/                   Update information and files the app downloads
├── release-notes/             Notes for each release
├── packaging/                 Files used to build the installer and publish releases
├── .github/                   Release workflow, issue forms and pull request template
├── CHANGELOG.md               Version history
├── CODE_OF_CONDUCT.md         Community rules
├── CONTRIBUTING.md            How to help
├── SECURITY.md                How to report security problems
└── LICENSE                    MIT license
```

## Building from source

You need [Python 3](https://www.python.org/downloads/) and [Node.js](https://nodejs.org/). In **PowerShell**, from the repository folder:

```
npm install
python tools/build.py
```

The build puts the data from `src/data/` into `src/index.html`, packs the app into `updates/iv31-<version>.neu` and rewrites `updates/manifest.json` with its size and SHA-256 fingerprint. The version comes from `app/neutralino.config.json` and has to match `APP_VERSION` in `src/index.html`. The installer itself is built by the release workflow from `packaging/`.

## Roadmap

- [x] Gen III (Hoenn) IV calculator
- [x] Full National Pokédex in Pokédex-number order
- [x] Suggested natures and key stat highlighting
- [x] EV yield tab
- [x] Windows installer
- [x] Auto-updater
- [x] EV calculator
- [x] Hidden Power type and power calculator
- [x] Secret Power area guide for the Gen 3 games
- [x] Type matchup chart and EV-lowering berries
- [x] Favorites and wild locations
- [x] Gen I and II (DVs and Stat Exp)
- [x] Nature Power
- [x] Publish the full source code
- [x] GitHub Releases with checksums
- [x] macOS build (Intel and Apple Silicon)
- [x] Linux packages (.deb with apt repository, AppImage, tarball)
- [ ] Save and compare multiple Pokémon side by side
- [ ] Optional Catppuccin flavour switcher (Latte, Frappé, Macchiato, Mocha)
- [ ] Signed Windows installer

Have an idea? [Open a feature request](../../issues/new?template=feature_request.yml).

## Contributing

Bug reports, data corrections and ideas are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) first, and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

Spotted a wrong base stat or EV yield? That's one of the most helpful reports you can make. Use the **Data correction** issue form.

## Security

Please don't report security problems in public issues. See [SECURITY.md](SECURITY.md) for how to report them privately.

## License and credits

iv31 is released under the [MIT License](LICENSE).

- Colour palette: [Catppuccin](https://github.com/catppuccin/catppuccin) (MIT).
- Desktop runtime: [Neutralinojs](https://neutralino.js.org) (MIT).
- Installer: [NSIS](https://nsis.sourceforge.io) (zlib).

Pokémon and all related names are trademarks of Nintendo, Game Freak and Creatures Inc. iv31 is an unofficial fan-made tool and is not affiliated with, endorsed by, or sponsored by Nintendo, Game Freak, Creatures Inc. or The Pokémon Company. No game assets are included.
