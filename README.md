<div align="center">

# iv31

**A fast, offline Pokémon IV calculator for the whole National Pokédex.**

Pick a Pokémon, enter its level and stats, and iv31 tells you its individual values, the nature that suits it best, and which stats matter most. A second tab holds a full EV yield table so you always know what to battle for training.

[![Version](https://img.shields.io/badge/version-1.0.0-f5c2e7)](CHANGELOG.md)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011-89b4fa)](#install)
[![License: MIT](https://img.shields.io/badge/license-MIT-a6e3a1)](LICENSE)
[![Offline](https://img.shields.io/badge/works-offline-cba6f7)](#privacy)

[Download](iv31-Setup-1.0.0.exe.zip?raw=true) · [Report a bug](../../issues/new?template=bug_report.yml) · [Request a feature](../../issues/new?template=feature_request.yml)

</div>

---

## Contents

- [Features](#features)
- [Install](#install)
- [How to use](#how-to-use)
- [How the math works](#how-the-math-works)
- [Privacy](#privacy)
- [What's in this repository](#whats-in-this-repository)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Security](#security)
- [License and credits](#license-and-credits)

## Features

- **Full National Pokédex** listed in Pokédex-number order, from Bulbasaur onward.
- **IV calculation** from level, nature and current stats, with the possible IV range shown when a single value can't be pinned down.
- **Suggested natures** for each Pokémon, based on its strongest stats.
- **Key stat highlighting** so you can see at a glance which stats a Pokémon is built around.
- **EV yield tab** with a sortable table of the effort values every Pokémon gives when defeated.
- **Saves your work** between sessions on your own computer.
- **Fully offline.** No account, no ads, no tracking, no internet connection needed after install.
- **Tiny.** The installer is about 1.3 MB because it uses the web engine already built into Windows.
- **Clean desktop look** inspired by modern Linux desktop setups, using the Catppuccin colour palette.

## Install

### Windows 10 / 11 (64-bit)

1. Download **[iv31-Setup-1.0.0.exe.zip](iv31-Setup-1.0.0.exe.zip?raw=true)**.
2. Right-click the downloaded zip → **Extract All** → **Extract**, then double-click **iv31-Setup-1.0.0.exe**.
3. Windows may show **"Windows protected your PC"**. This appears because the installer isn't signed with a paid code-signing certificate. Click **More info → Run anyway**.
4. Follow the setup screens. No administrator password is needed; iv31 installs for your user account only.
5. Launch iv31 from the Start menu or the desktop shortcut.

**Requirement:** Microsoft Edge WebView2 Runtime. Almost every Windows 10/11 PC already has it. If yours doesn't, the installer offers to open Microsoft's download page.

**Uninstall:** Settings → Apps → Installed apps → iv31 → Uninstall.

### macOS and Linux

Native builds are planned. See the [roadmap](#roadmap).

## How to use

1. Choose a Pokémon from the list, or search by name or Pokédex number.
2. Enter its **level** and **nature**.
3. Enter the six stats shown on its summary screen (HP, Attack, Defense, Sp. Atk, Sp. Def, Speed).
4. If it has received EVs, enter those too. For a freshly caught Pokémon, leave them at 0.
5. Read the IV for each stat. A range like `24–27` means more data is needed; level the Pokémon up once and enter the new stats to narrow it down.
6. Open the **EV Yield** tab to see which Pokémon to battle to train a specific stat.

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

## Privacy

iv31 does not collect, send or share any data.

- Everything runs locally on your computer.
- Saved entries are stored in the app's local browser storage on your machine only.
- The app's internal web server listens only on your own computer (`127.0.0.1`), never on your network.
- There are no analytics, telemetry, ads or update checks.

## What's in this repository

```
.
├── iv31-Setup-1.0.0.exe.zip   Windows installer
├── .github/                   Issue forms and pull request template
├── CHANGELOG.md               Version history
├── CODE_OF_CONDUCT.md         Community rules
├── CONTRIBUTING.md            How to help
├── SECURITY.md                How to report security problems
└── LICENSE                    MIT license
```

## Roadmap

- [x] Gen III (Hoenn) IV calculator
- [x] Full National Pokédex in Pokédex-number order
- [x] Suggested natures and key stat highlighting
- [x] EV yield tab
- [x] Windows installer
- [ ] Publish the full source code
- [ ] GitHub Releases with checksums
- [ ] macOS build (Intel and Apple Silicon)
- [ ] Linux AppImage
- [ ] Hidden Power type and power calculator
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
