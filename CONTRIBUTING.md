# Contributing to iv31

Thanks for wanting to help make iv31 better. Every bug report, data fix and idea counts.

## Ways to help

| You want to... | Do this |
| --- | --- |
| Report something broken | Open a [bug report](../../issues/new?template=bug_report.yml) |
| Fix a wrong base stat or EV yield | Open a [data correction](../../issues/new?template=data_correction.yml) |
| Suggest an idea | Open a [feature request](../../issues/new?template=feature_request.yml) |
| Report a security problem | Follow [SECURITY.md](SECURITY.md). Please don't post it publicly. |
| Change the code | Read the rest of this guide |

## Ground rules

- Be kind. Everyone here follows the [Code of Conduct](CODE_OF_CONDUCT.md).
- iv31 stays **offline**. Changes must not add analytics, tracking, ads or outside network requests.
- Don't add official game artwork, sprites or other copyrighted Pokémon assets.
- Pokémon data changes need a source, such as Bulbapedia or Serebii.

## Code changes

The app's page is `src/index.html`, and its Pokédex, location and Secret Power data are in `src/data/`. See [Building from source](README.md#building-from-source).

1. Fork the repository and create a branch for your change.
2. Make the change and run `python tools/build.py` to check it builds.
3. Open a pull request that says what changed and why. Don't commit the files the build changes in `updates/`; the maintainer updates those when releasing.

## Writing a good report

- One problem or idea per issue.
- For calculation problems, include the Pokémon, level, nature, stats and EVs you entered.
- For data corrections, link to where the correct value comes from.
- Screenshots help a lot.

## Releases (maintainer)

Releases are published automatically by the **Release** workflow in `.github/workflows/release.yml`. To ship a new version:

1. Raise the version in `app/neutralino.config.json` and `APP_VERSION` in `src/index.html`, write a one-line summary in `src/release.json`, and add a section to `CHANGELOG.md`.
2. Add `release-notes/<version>.md` with what's new.
3. Run `python tools/build.py`. It writes `updates/iv31-<version>.neu` and updates `updates/manifest.json` with the new version, link, SHA-256 fingerprint and summary.
4. Commit and push. The workflow builds the installer from `packaging/`, creates the `v<version>` release with the installer attached and marks it as the latest. Installed copies of iv31 pick up the update automatically.

If an update needs a new app engine (not just new app files), set `"installer": true` in the manifest's `data` so people are sent to the installer instead. Installers are never committed to the repository; they only live on the Releases page.

## License

By contributing, you agree that your contributions are released under the [MIT License](LICENSE).
