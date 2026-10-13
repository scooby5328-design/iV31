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

The app's source code isn't published in this repository yet. Once it is, this section will cover setup, branches and pull requests. Until then, the best way to help is through the issue forms above.

## Writing a good report

- One problem or idea per issue.
- For calculation problems, include the Pokémon, level, nature, stats and EVs you entered.
- For data corrections, link to where the correct value comes from.
- Screenshots help a lot.

## Releases (maintainer)

1. Update the version number in the installer and in `CHANGELOG.md`.
2. Move the **Unreleased** notes under a new version heading with the date.
3. Zip the new installer and upload it to the repository, replacing the old one.
4. Create a GitHub release tagged `v1.x.x`, attach the installer, and paste its SHA-256 checksum into the notes.

## License

By contributing, you agree that your contributions are released under the [MIT License](LICENSE).
