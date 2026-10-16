# Security Policy

## Supported versions

Only the latest release receives security fixes. Please update before reporting.

| Version | Supported |
| ------- | --------- |
| 1.2.x   | ✅        |
| 1.1.x   | ❌        |
| 1.0.x   | ❌        |
| < 1.0   | ❌        |

## Reporting a vulnerability

**Please do not open a public issue for security problems.**

Report privately through GitHub:

1. Go to the [Security tab](../../security) of this repository.
2. Click **Report a vulnerability**.
3. Fill in the form and submit.

Only the maintainer can see the report.

### Please include

- The iv31 version (shown in Settings → Apps, or the installer file name)
- Your Windows version
- What the problem is and what an attacker could do with it
- Step-by-step instructions to reproduce it
- A proof of concept, screenshots or logs, if you have them

### What to expect

| Step | Target time |
| --- | --- |
| Acknowledge your report | Within 3 days |
| Confirm whether it's a real issue | Within 7 days |
| Release a fix for confirmed issues | Within 30 days, depending on severity |

You'll be kept updated as the report moves along. With your permission, you'll be credited in the release notes once the fix is out. iv31 is a free hobby project, so there is no bug bounty.

## Scope

**In scope**

- The iv31 application and its bundled files
- The Windows installer and uninstaller
- The app's local web server and its configuration
- The installers published on this repository's Releases page
- The built-in updater and the update files in the `updates/` folder

**Out of scope**

- Copies of iv31 downloaded from anywhere other than this repository's Releases page
- Problems in Windows, WebView2, Neutralinojs or NSIS themselves (please report those to their maintainers)
- The Windows SmartScreen warning on first install (this happens because the installer is unsigned and is expected)
- Attacks that need someone to already have full control of your computer
- Social engineering

## How iv31 is built to stay safe

- **One outside connection: update checks.** The only thing iv31 downloads is its own update information from `raw.githubusercontent.com/scooby5328-design/iv31`. It sends nothing about you: no analytics, no telemetry, no accounts. You can turn automatic checks off in the Guide.
- **Updates are verified before they're installed.** An update is only accepted from this repository's `updates/` folder, and the downloaded file's SHA-256 fingerprint must match the one published in `updates/manifest.json`. If it doesn't match, nothing is changed.
- **Tight native permissions.** The app can use only three native functions: write its own `resources.neu` file (writing anywhere else is blocked), relaunch itself after an update (the only program it's allowed to start is one named `iv31.exe`), and exit. Every other native function, including reading files, is blocked.
- **Locked-down page.** A Content Security Policy only lets the page load its own files and connect to the local app server and GitHub's raw file host.
- **Local only.** The internal web server listens on `127.0.0.1` only, so other devices on your network can't reach it.
- **One-time access token.** The runtime uses one-time token security for its local connection.
- **Per-user install.** The installer doesn't ask for administrator rights and only writes to your user folder and your user's registry keys.
- **Clean uninstall.** The uninstaller removes the app files, shortcuts and registry entries it created.

## Verifying your download

The SHA-256 checksum for each installer is listed in its release notes and in [CHANGELOG.md](CHANGELOG.md). To check yours, open **PowerShell** in the folder with the installer and run:

```powershell
Get-FileHash .\iv31-Setup-1.2.0.exe -Algorithm SHA256
```

The result should match the checksum exactly. If it doesn't, delete the file and download it again from the Releases page.
