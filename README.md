<div align="center">

# iv31

**A fast, offline Pokémon IV calculator for the whole National Pokédex.**

Pick a Pokémon, enter its level and stats, and iv31 tells you its individual values, the nature that suits it best, and which stats matter most, even after it has battled. It also tracks EVs, shows what each Pokémon gives and where to find it, and has a data page for every Pokémon, type matchups, and Hidden Power, Secret Power and Nature Power charts. It covers every main game from Red, Blue and Yellow to Scarlet and Violet.

[![Latest release](https://img.shields.io/github/v/release/scooby5328-design/iV31?label=latest&color=f5c2e7)](https://github.com/scooby5328-design/iV31/releases/latest)
[![Platform](https://img.shields.io/badge/platform-Web%20%7C%20Windows%20%7C%20macOS%20%7C%20Linux-89b4fa)](#install)
[![License: MIT](https://img.shields.io/badge/license-MIT-a6e3a1)](LICENSE)
[![Offline](https://img.shields.io/badge/works-offline-cba6f7)](#privacy)

[Use it online](https://scooby5328-design.github.io/iV31/) · [Download the latest version](https://github.com/scooby5328-design/iV31/releases/latest) · [Report a bug](../../issues/new?template=bug_report.yml) · [Request a feature](../../issues/new?template=feature_request.yml)

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

- **Full National Pokédex** in Pokédex-number order, for every main game from Red to Scarlet and Violet. One game picker sets the game everywhere.
- **IV calculation** from level, nature and current stats, with the possible range when a single value can't be pinned down.
- **Pokémon that have battled:** when EVs have raised a stat, iv31 shows the IV and EV ranges that fit instead of failing. Gen I and II do the same for Stat Exp.
- **Gen I and II rules:** DVs from 0 to 15 (the HP DV worked out from the others), Stat Experience, no natures, one Special stat in Gen I, and Gen II Hidden Power and shiny checks.
- **Data page for every Pokémon:** base stats, the 2 stats to focus, the proper nature, the EVs it gives, where to find it, its evolutions and its type matchups. Click any name or number to open it.
- **EV calculator:** add EVs by Pokémon defeated (with Macho Brace, Power items and Pokérus) or vitamins, within the 510 and per-stat limits, and see the stat points they give.
- **EVs gained:** compare a Pokémon's stats before and after training to see the EVs it earned (under the EV calculator, with the EV-lowering berries).
- **Poké Data:** every Pokémon's fixed data in one table in Pokédex order: types, weaknesses, what it's strong against, the EVs it gives and where it lives in your version. Filter by EV stat, type or matchup against any attacking type, search by name, number, type or place, sort by any column or story order, and click a type to filter. Your filters are remembered. A matchup checker for any one or two types sits on top.
- **Party comparison** of up to 30 Pokémon side by side.
- **Types:** a weakness and resistance chart for the selected generation where you can highlight any types, plus notes on how types work in your game.
- **Powers:** a Hidden Power calculator and chart, and Secret Power and Nature Power charts for every area of the Gen III games (terrain tables for later games).
- **Favorites:** a short list of the Pokémon you care about, each linking to its data page.
- **Help built in:** every section has a **?** that explains what it does and how it works with the others.
- **Handheld device design** with blue screens, a D-pad and A/B buttons for moving around, a day and night screen, and optional click sounds.
- **Online, desktop or phone:** use it in a browser (it works offline once loaded and can be installed like an app), or install the desktop app for Windows, macOS or Linux.
- **Updates itself.** The desktop app checks GitHub for a new version and installs it with one click after verifying it; the website updates when you reload.
- **Private.** No account, no ads, no tracking.

## Install

### Online

Open **[scooby5328-design.github.io/iV31](https://scooby5328-design.github.io/iV31/)** in any modern browser. After the first visit it works offline. To keep it like an app, use your browser's **Install** or **Add to Home Screen** option.

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

1. Pick your game in the game picker (top left on the device). Every tab follows it.
2. Choose a Pokémon from the list, or search by name or Pokédex number.
3. Enter its **level** and **nature**.
4. Enter the six stats shown on its summary screen (HP, Attack, Defense, Sp. Atk, Sp. Def, Speed).
5. Set **EVs** to **None yet** for a freshly caught or hatched Pokémon, **Has battled** if it has fought and you don't know its EVs, or leave **Not sure**. If you know its EVs, type them under **Known EVs**. When EVs are raising a stat, the readout shows the IV range and EV range that fit.
6. Read the IV for each stat. A range like `24–27` means more data is needed; level the Pokémon up once and enter the new stats to narrow it down.
7. Use the **EV calculator** panel to plan or track EV training. Add each Pokémon you defeat and it tallies the EVs and stat points for you. Click **Send EVs to Summary** so the IV readout accounts for them.
8. To compare several Pokémon, press **+ Add party member** in the **Party comparison** panel and fill in each one, or click **Copy from Summary screen**. The table lines up their IVs side by side (up to 30; on phones this is part of iv31 Full).
9. Open **Poké Data** to see which Pokémon to battle to train a stat, where to find them, their types and weaknesses, or which Pokémon are weak to a type. Press **/** to search. **EVs gained** and **EV-lowering berries** are under the EV calculator in the IV Calculator tab.
10. Open **Types** for the weakness chart. Click types to highlight their rows and columns.
11. Click any Pokémon's name or number to open its **data page**. On the device, **B** goes back and **A** goes forward; the D-pad switches tabs and scrolls the screen. On phones, use **◂ ▸** at the top.
12. Open **Powers** for **Hidden Power** (a calculator plus the IVs that give each type), **Secret Power** and **Nature Power** (what each move turns into in every area).
13. Tap ☆ next to any Pokémon to keep it in **Favorites**, a short list that links to each data page.
14. Stuck? Press the **?** next to any section's title.

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

- Everything runs on your own device, in the desktop app or in your browser.
- Saved entries (favorites, party, EVs, settings) stay in local storage on your device.
- The desktop app's internal web server listens only on your own computer (`127.0.0.1`), never on your network.
- There are no analytics, telemetry, cookies or ads.
- The desktop app's only internet connection is the update check, which downloads a small version file from this repository. You can turn it off. The website loads only its own files from GitHub Pages.

## What's in this repository

```
.
├── src/                       The app's page (src/index.html), its data and the update summary
├── app/                       App settings, bundled files (fonts, icon, runtime client) and web/ (website manifest, icons, offline worker)
├── tools/                     build.py packs the desktop app into updates/; build_web.py builds the website into dist/web
├── android/                   The Android app (a WebView around the same page)
├── updates/                   Update information and files the app downloads
├── release-notes/             Notes for each release
├── packaging/                 Files used to build the installer and publish releases
├── .github/                   Release, website and Android workflows, issue forms and pull request template
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

To build the website, run `python tools/build_web.py`. It writes a ready-to-serve folder to `dist/web`. The **Website** workflow builds and publishes it to GitHub Pages whenever a release is pushed.

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
- [x] Party comparison
- [x] IVs for Pokémon that have battled, and EVs gained
- [x] Data page for every Pokémon
- [x] Handheld device design
- [x] Online version (GitHub Pages, works offline)
- [ ] iv31 Full: paid unlock on phones
- [ ] Android app on Google Play
- [ ] Signed Windows installer

Have an idea? [Open a feature request](../../issues/new?template=feature_request.yml).

## Contributing

Bug reports, data corrections and ideas are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) first, and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

Spotted a wrong base stat or EV yield? That's one of the most helpful reports you can make. Use the **Data correction** issue form.

## Security

Please don't report security problems in public issues. See [SECURITY.md](SECURITY.md) for how to report them privately.

## License and credits

iv31 is released under the [MIT License](LICENSE).

- Fonts: [Silkscreen](https://fonts.google.com/specimen/Silkscreen), [VT323](https://fonts.google.com/specimen/VT323), [JetBrains Mono](https://www.jetbrains.com/lp/mono/) and [Fira Sans](https://fonts.google.com/specimen/Fira+Sans), all under the SIL Open Font License.
- Desktop runtime: [Neutralinojs](https://neutralino.js.org) (MIT).
- Installer: [NSIS](https://nsis.sourceforge.io) (zlib).

Pokémon and all related names are trademarks of Nintendo, Game Freak and Creatures Inc. iv31 is an unofficial fan-made tool and is not affiliated with, endorsed by, or sponsored by Nintendo, Game Freak, Creatures Inc. or The Pokémon Company. No game assets are included.
