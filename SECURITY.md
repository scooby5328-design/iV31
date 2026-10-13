# Security Policy

## Supported versions

Only the latest release receives security fixes. Please update before reporting.

| Version | Supported |
| ------- | --------- |
| 1.0.x   | ✅        |
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
- The installer published in this repository

**Out of scope**

- Copies of iv31 downloaded from anywhere other than this repository
- Problems in Windows, WebView2, Neutralinojs or NSIS themselves (please report those to their maintainers)
- The Windows SmartScreen warning on first install (this happens because the installer is unsigned and is expected)
- Attacks that need someone to already have full control of your computer
- Social engineering

## How iv31 is built to stay safe

- **No network access.** The app makes no outside connections: no analytics, no telemetry, no update checks.
- **Local only.** The internal web server listens on `127.0.0.1` only, so other devices on your network can't reach it.
- **Native access turned off.** The Neutralino native API is disabled, so the page can't run programs or read files on your computer.
- **One-time access token.** The runtime uses one-time token security for its local connection.
- **Per-user install.** The installer doesn't ask for administrator rights and only writes to your user folder and your user's registry keys.
- **Clean uninstall.** The uninstaller removes the app files, shortcuts and registry entries it created.

## Verifying your download

The SHA-256 checksum for each installer is listed in [CHANGELOG.md](CHANGELOG.md). To check yours, open **PowerShell** in the folder with the installer and run:

```powershell
Get-FileHash .\iv31-Setup-1.0.0.exe -Algorithm SHA256
```

The result should match the checksum exactly. If it doesn't, delete the file and download it again from this repository.
