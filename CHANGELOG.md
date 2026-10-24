# Changelog

All notable changes to iv31 are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Planned
- Side-by-side comparison of saved Pokémon

## [1.8.8] - 2026-10-24

### Added
- Side tabs tuck in to symbols and slide out over the page on hover or keyboard focus, without moving the page.
- A three-line menu button above the side tabs keeps them open (pushing the page over) or tucks them away; the choice is saved in `iv31-tabs`.
- Tab symbols: calculator, table, linked circles, lightning bolt and star. Phones show them above the short tab names.

### Checksums (SHA-256)

```
27321ff095149d40108304b9ea094e3afc5dfad4525f4ad7a483f2d8226fc26a  iv31-Setup-1.8.8.exe
2ca82d7fdc3a6bd0a22f60431991b4e8fc52604aeff9ecd329fba06b90261ba2  iv31-1.8.8-mac.zip
106d7da0eaa9461c58f97c985dd43cdb1c576e8154e7385ecb7928bf295731f3  iv31-1.8.8-linux-x64.tar.gz
5f70dbfff56c7e09ae9fb0c92796f81fc0defc0bf99004f21a8240e3e0125ea2  iv31-1.8.8-linux-arm64.tar.gz
0588b7183fc0b731c1c94a6a1f9395d62fe7437271b1e2e9722ad2606e700225  iv31_1.8.8_amd64.deb
52f6e15f44eab664c0dd36047a731c3d569ecaf7ec31608553c3052667c2ee98  iv31_1.8.8_arm64.deb
9caa2a7a5885d8cf109d6381a84c71fef6e83cfa03d76356b158e5df87ee60e4  iv31-1.8.8-x86_64.AppImage
a1b0b8b51b53778e1401f15aaad94ccecda07c3f95effed44dd5f03f3fe523ad  iv31-1.8.8-aarch64.AppImage
```

## [1.8.7] - 2026-10-24

### Changed
- Tabs are folder tabs: a column down the left side on wider screens (numbers only below 1100px), tabs along the top on phones, and folder tabs along the bottom in the Android app. The open tab joins onto its page.
- The Poké Data table and the type chart no longer scroll inside the screen, so there is one scrollbar. Column headings stay pinned while scrolling. A table that can't shrink enough to fit falls back to scrolling sideways.

### Checksums (SHA-256)

```
4992bbcd65a0ae32c02d12ce893861d8bfc9a1d939a32332bdb2c056aa15ed5e  iv31-Setup-1.8.7.exe
13457b269cb65c016eaa103cd027907a3b009dae47e11ad1a4bdd7c2eedf27bd  iv31-1.8.7-mac.zip
ab7c6eb75e7d08548158b974b9e10fa1b75046e1339c9847161ac17181dcdb8b  iv31-1.8.7-linux-x64.tar.gz
1e91ddc30f0ba0b27e63c5fda1d5c26e91203f7402063cf7381a45bd5f47bd1d  iv31-1.8.7-linux-arm64.tar.gz
ac205b4f3526cee781645cc19bf6b2e685b6327987b844d0b2cfcdbdd9f9a67a  iv31_1.8.7_amd64.deb
6b9e918dfbdf5614dfd2f3b986715a75508b29ab3d03487d53d14cd486c90226  iv31_1.8.7_arm64.deb
51a38b1861ea92eee4be21e82c9b8364b5141f5f68197ce04e39568920267922  iv31-1.8.7-x86_64.AppImage
8bb6c1a870c13d75922bb48ec16fdd49980f99170c98730b06aa3c393e41fbd3  iv31-1.8.7-aarch64.AppImage
```

## [1.8.6] - 2026-10-24

### Fixed
- Phones: the data page header stacks into one column (the narrow-screen rule was being overridden by a later rule).
- Floating **?** buttons on folding panels follow the end of a wrapped title, account for the SIZE zoom, and hide when their panel is hidden (for example EVs gained in the free tier).

### Checksums (SHA-256)

```
a893d794fe495d2d049ab77e4f0d12147ab5861b165b6fdfbf8ded13625fdfd5  iv31-Setup-1.8.6.exe
3404db90209795752f9d5ce4e265643b5f05825bf13bc4aad2d52f505f958a1b  iv31-1.8.6-mac.zip
2229935c13f56e1ef602960b5240a9bf0d844c944bdc6746390acccefb6c7fb0  iv31-1.8.6-linux-x64.tar.gz
4603373be75e61d70c602de68d8e289582fa87736ee161f62d67b2c4fa93e155  iv31-1.8.6-linux-arm64.tar.gz
4ae0a34feb3473e1e93388d7fdc07d60fa4548069d1b5fdbdd443c622d0eb8e9  iv31_1.8.6_amd64.deb
63362c8984d9f2b1f8625abb25c25d69c8816a58cd110e62a970c50a415cc9f9  iv31_1.8.6_arm64.deb
9f5033cd3e60cedcca511ef431e8d6ad1578e52e48f2a024fab28e2041120efa  iv31-1.8.6-x86_64.AppImage
a54709cd178f0030960746090c09dfe56f813c005267952c29203a89acbb1644  iv31-1.8.6-aarch64.AppImage
```

## [1.8.5] - 2026-10-24

### Added
- Every section (`section.win` in a view) folds with an **Open ▾ / Close ▴** button or a click on its title bar; folded sections are remembered (`iv31-folded`).
- **SIZE** control on the device's left panel (80–150%, Ctrl/⌘ + / − / 0), applied as `zoom` on the screen's content and remembered (`iv31-size`). Side-by-side panels stack when the scaled screen is narrower than 900 px.

### Changed
- D-pad ▴ ▾ scroll half a screen.

### Checksums (SHA-256)

```
0117bc54c3eb290aa680753779048750c859cd2339d1e4efde44571b5b79513a  iv31-Setup-1.8.5.exe
b8888159c8edd28c60f69baefafadb034b609fc50628d8e149c789d5790d5a59  iv31-1.8.5-mac.zip
1d012602aa5952e72c15062a8ab2186d3f278463973729269854444defca7047  iv31-1.8.5-linux-x64.tar.gz
9ac84494ebc08ed411a8f3a973d80400d56db180f71061f3f03883b301a4778b  iv31-1.8.5-linux-arm64.tar.gz
72eee9bbc75954ff37a57f4364cfd46d4795ea1d1ca7744ee7a2613b3f4fb2b5  iv31_1.8.5_amd64.deb
20eaf14c912cd650ed08259ff902c23b4ea054b83118cf3f2c684780b535547e  iv31_1.8.5_arm64.deb
8116f307dab822679ba190ed02d9c62ca7bdad69c1dcfd7f3c9a2152cfa65d14  iv31-1.8.5-x86_64.AppImage
720626404ddd60b05728b642b6387dedad8a3f73e8c97af4b19708a436b84617  iv31-1.8.5-aarch64.AppImage
```

## [1.8.4] - 2026-10-23

### Changed
- Folding panels (`details.win`) look clickable: dashed outline while folded, a turning arrow, an **Open ▾** / **Close ▴** button, and a hover highlight. The matchup checker's filter button no longer stretches.

### Checksums (SHA-256)

```
c93b568942cf4df3b89a07b3a11bd4eaa0ceaa0bb517a2a61fec237149cdb77e  iv31-Setup-1.8.4.exe
dc37bdd2a042bcb1727408eccb5714bf616c1008f1061e02323b4e8798a4b24a  iv31-1.8.4-mac.zip
9c4c4ea05c896d57835fdb0b449d3fe2c5f5f5808fa303a50bc38e2c2b62f64b  iv31-1.8.4-linux-x64.tar.gz
05b6147f37c4109c0585987f289bd85602bdc154910c138dcd77e80a06e53e63  iv31-1.8.4-linux-arm64.tar.gz
edd4c9be879a06ae4e6d41b043e3ee70494684d9e865787bdb416c1f1836e3d0  iv31_1.8.4_amd64.deb
9fea9d62c085171e8935107f9c990aff591f7991d2addd335d19f3a3c90c3d8f  iv31_1.8.4_arm64.deb
c2e6f505b02de99caaf7930a7c95a4675cdb1e7f439d9d9163b6f4dc666ff18c  iv31-1.8.4-x86_64.AppImage
385c51b26b91bf39ead01a6fa46d7465330d02c25ca432f6b6ef349e20ba7b49  iv31-1.8.4-aarch64.AppImage
```

## [1.8.3] - 2026-10-23

### Added
- **Strong against** column in Poké Data (types the Pokémon's own types hit for 2×, from `offense()`), sortable, clickable to filter by that type, and optional under Columns (`pd.strong`).

### Checksums (SHA-256)

```
e27a4662bad9f993c4bf7a0f2afe1c3f79d735022e14c6c98834d4dc353be5a0  iv31-Setup-1.8.3.exe
3bfe4f53dbd155f6b1de443ce7bed80c312e969d1b972c4e1d9858b59952a32a  iv31-1.8.3-mac.zip
cad4b2e5cc996c3721ec94e760866a7d83af8d44fa8349f9cd62853736b301a9  iv31-1.8.3-linux-x64.tar.gz
8538c7c3e87d452bde530ea24ed6e3b7a029e35247133924b69e619d05c376e7  iv31-1.8.3-linux-arm64.tar.gz
fee355ce34f222a22aa2b2a704abe208757c2bb3b5742694073d619df5bc159a  iv31_1.8.3_amd64.deb
7000ee33cc65a47c4202ce86f3e223b2609a215aa99f797307762534988a3d97  iv31_1.8.3_arm64.deb
427aa2c771bff25f591e8bd63c8d4678ac45085a29dda8512fb28072db1d1c05  iv31-1.8.3-x86_64.AppImage
af5a1e0bf3c486522c7f3a7d9f13d8297be5e8bd2f21e29739f37b0765021600  iv31-1.8.3-aarch64.AppImage
```

## [1.8.2] - 2026-10-23

### Fixed
- The website's update prompt compares the newest offline cache version with the page's version, so it no longer appears when the page already loaded the new version from the network.

### Checksums (SHA-256)

```
eb5de7411d783ad52407307a1ddc369898aa33df4eef62184bc8c7f1fba7228c  iv31-Setup-1.8.2.exe
df986d3f3fafc6ea927f4bbc8be2fd4881c475a78ba80b55b43f4016848b264a  iv31-1.8.2-mac.zip
55894363b5489a0746b7d8accfeb28d2240f8b75b5d5a63ee9d0ce8772d550d3  iv31-1.8.2-linux-x64.tar.gz
9e6f8235a39d5edb89da39d9d616edb1300080cf26244192dbc087e223655e79  iv31-1.8.2-linux-arm64.tar.gz
fca0e155fb2924d1aca5a453d0874c1bb2f6d3c7bb4940f78b1f8ba782e6df7c  iv31_1.8.2_amd64.deb
ea1c963f4eb6d3290025dbba21cc4ac7e19b3cc34fcaf9797e99f9ada2ec8417  iv31_1.8.2_arm64.deb
251e7d7c0f77452dddcbcfcdecfeaa17ee5b352e37d9413c907062dc05d6ee3e  iv31-1.8.2-x86_64.AppImage
8adbc5b7a67f91059d683bb757f9802bfa434019600f06e8dd5331f59cf7e5dc  iv31-1.8.2-aarch64.AppImage
```

## [1.8.1] - 2026-10-23

### Changed
- **EV Training is now Poké Data** (`#pokedata`; `#evs` still works): Type and Weak to columns, a Type filter, **Matchup against** an attacking type with a multiplier column and Weak / Resist / Immune filters, clickable type and weakness chips, search by type name, and the matchup checker as a folding panel with **Filter the table to this type**.
- Quality of life: filters, sorting and column choices are remembered (`iv31-pokedata`), **Clear filters**, active filters listed in the count line, **/** focuses search and **Esc** clears it, optional Weak to and Found in columns, and rows render in chunks so the tab opens faster.
- **EVs gained** and **EV-lowering berries** moved to the IV Calculator tab under the EV calculator (`#berries` opens the berries there). The Types tab keeps the chart and type notes.
- Tips stay open while the screen scrolls into place.

### Checksums (SHA-256)

```
82f22609eb434819786e26b04e62ff36f4fc9e84d2d921529b47d614300bcaf6  iv31-Setup-1.8.1.exe
2cbb7c7e0e730d44abddb9d52cd1a98ba7bb4f29699ca35cb3e24916217e1101  iv31-1.8.1-mac.zip
24b3d0d632111d5dc7a1f6cf1d55bc12bb8d9285f9bdded7995be53abfae665b  iv31-1.8.1-linux-x64.tar.gz
b7a03ef2383ee4498cc2258b8934a66402ca7573ac06b9ae2b57423e7307522b  iv31-1.8.1-linux-arm64.tar.gz
b4aaf0136754eb68af34f3c2ad6e38b8281eb62f5546b65dbd629925e3889bba  iv31_1.8.1_amd64.deb
b2d33a972084b1c13eb6ab68f383da586b79cf7334b8dcba586056170789eda9  iv31_1.8.1_arm64.deb
3f6284cc9d9b32c40b19a61b5da4663b3e7190ef96f15066c34562ae61e9f04a  iv31-1.8.1-x86_64.AppImage
f9c08388cbbf76cd1eda1f941f46fb8467fcce948d2ac678c5002a52c9436867  iv31-1.8.1-aarch64.AppImage
```

## [1.8.0] - 2026-10-23

### Added
- **Website** at https://scooby5328-design.github.io/iV31/ built by `tools/build_web.py` (no Neutralino client, its own security policy, description and social tags, web manifest and icons, `sw.js` offline cache that refreshes the page from the network first) and published by the **Website** workflow (`.github/workflows/pages.yml`) when a release is pushed. The page shows a "new version ready" prompt when the worker updates.

### Changed
- Favorites is a compact list (`favRow`) linking to data pages; the old full cards were removed.
- The Hidden Power calculator moved into Powers → Hidden Power above the chart; the duplicate "Aim for a type" table was removed and the chart row of the current type is highlighted.
- The matchup checker's Pokémon picker opens the data page; the checker itself covers type combinations.
- The EV calculator spans the full width.
- Wording that said "top bar" now refers to the game picker.
- README rewritten for the current features, the website, privacy and fonts.

### Fixed
- Table fitting does one read and one write pass per screen instead of repeated layouts.
- Day screen contrast (accent, version and clock colors) meets WCAG AA.
- Type chart headings use buttons (`.tpick`) instead of `aria-pressed` on table headers; tip buttons on folded panels sit outside the summary element.
- The audio context is only created after a user gesture.

### Removed
- 128 overridden style declarations, 16 style rules for removed elements, and unused code (`seBonus`, an unused variable, duplicate open-in-calculator handlers and DV combination code).

### Checksums (SHA-256)

```
fd3e638f04c5a562db05e3795027c7622af0c46bc2015a82acb865c3f843774c  iv31-Setup-1.8.0.exe
b1c97a617968518686a1f6180a53676186da642e235fa25c93edc2ae3cd53b31  iv31-1.8.0-mac.zip
65d3dfb126d1db28f76ba30b3aebb79ead4659568e428f96668870be8222a2c8  iv31-1.8.0-linux-x64.tar.gz
461cec7983494f7b8a486950bf47bf0468af4a151a820aa328b7cd6b8e90361a  iv31-1.8.0-linux-arm64.tar.gz
f44f4625d094c6a23906823bb450084cd2381b50d814d38b334ca8cf77e31966  iv31_1.8.0_amd64.deb
1c4a961857b701e410d9c9cc7069e2d7d40b0afc072dfd17475557aea9fde16b  iv31_1.8.0_arm64.deb
d1263bcf53597ccefe2c6552033fb27f5cb3ebad4b008261068fcf153500da6d  iv31-1.8.0-x86_64.AppImage
166959322ddbd7dbf9568c3c9bd63d40f5ef9e1d1d5bb894c65dbf76a82d65de  iv31-1.8.0-aarch64.AppImage
```

## [1.7.2] - 2026-10-23

### Changed
- Wide tables fit the screen instead of scrolling sideways: tables no longer have fixed minimum widths, headings wrap, and any table still too wide is scaled down (`fitWide` in `src/index.html`, down to 55%).

### Checksums (SHA-256)

```
e13f17353c099b76faa8bad5c4fe013b841a193ebbea1e455eb903e1256788f9  iv31-Setup-1.7.2.exe
562c51e20c7012f23cca80c1cf0ca5d00f38b90d281f538ca245ece45f76be99  iv31-1.7.2-mac.zip
f147f0a6dda5580656d5f29f4920786b41952d6bfd5918170d206a1a3bf703ba  iv31-1.7.2-linux-x64.tar.gz
0463c88a3a1d36f8f41c4e0ee3829b4213051fd1183cb6d87d1278b6d59b6c86  iv31-1.7.2-linux-arm64.tar.gz
70a7533023e451f92a38fae1434e589fbbbec0c4c34c229a4c68e28596b74b0b  iv31_1.7.2_amd64.deb
b10818f6f8fa06acf473302167eb535eb8b8875f29eeac24a3bfe4ed56839575  iv31_1.7.2_arm64.deb
737c72a8e4bd5ab5cbbebdd652d210a4acff1efc4b38fbb2946f264ec5ccbdfb  iv31-1.7.2-x86_64.AppImage
f245d87be35b5a71486a77feac63708abd19b72292926fe39ef3101aced46bfb  iv31-1.7.2-aarch64.AppImage
```

## [1.7.1] - 2026-10-23

### Changed
- Device layout: wide side panels hold the controls (left: game picker, D-pad, SOUND; right: version and clock, B/A, DAY/NIGHT) and the screen runs the full height of the device. Narrower windows get slimmer panels; phones keep the game picker and version in one row above the screen.

### Checksums (SHA-256)

```
008cb0d7e620d483aa2cf05d21339dd0161057a3af1b6507bf90d97225d9cada  iv31-Setup-1.7.1.exe
46bb2abdaad7b6b042e23f5aa29e1d6642a4378de9dc4b477c4011be97ad18de  iv31-1.7.1-mac.zip
1566dec673f36d9df835531b37bc13429625bf43cc0364c8bc110a7c778aed66  iv31-1.7.1-linux-x64.tar.gz
2e807f932eb5560d5df61c4dfc28698b81c35b1812dbb074ec75edb64769932d  iv31-1.7.1-linux-arm64.tar.gz
4478017715565b8b91dbec8c5b95df99d2fa5f550a2a85cb285e8c716c248251  iv31_1.7.1_amd64.deb
7bb0699ef6b3bcdc3e0deb68d220317ba60474351118c089d4319bcf21b026f2  iv31_1.7.1_arm64.deb
02e5d02c69e997816fe0e220186745b99a6e912c81ffb64354763c2371fc6867  iv31-1.7.1-x86_64.AppImage
ea97fd501d48692bdc1cf614a64f160ec834adc1299b1c2ad65b8552b05544eb  iv31-1.7.1-aarch64.AppImage
```

## [1.7.0] - 2026-10-23

### Changed
- **Handheld device redesign:** the app sits inside an original graphite field unit with a status screen (game, version, clock), a blue main screen that scrolls inside the device, and a control deck. Blue day and night screen palettes replace the green ones.

### Added
- **Device buttons:** D-pad ◂ ▸ switches tabs (steps through the Pokédex on a data page), ▴ ▾ scrolls the screen; **B** back, **A** forward; **SOUND** and **DAY/NIGHT** keys (remembered).
- **Start-up screen** once per session, a screen flicker on page changes, press animations, and synthesized click sounds (Web Audio, no sound files). Motion is skipped when the system asks for reduced motion.
- On phones the frame is slim, the deck is hidden and Back/Forward sit in the tab bar.

### Checksums (SHA-256)

```
20c51af63a9ce81bfa3d7efa932841df76677627313608510baa06ba13532b43  iv31-Setup-1.7.0.exe
14588ac9af1bc6ae05575c69691e563ac97e40d6b566a5c16906ac850d0114f3  iv31-1.7.0-mac.zip
77f3a0ee5d7b6ebc77f29504921ad210bd3a6311efab36a869ea63c92aa6a578  iv31-1.7.0-linux-x64.tar.gz
941703dfbb2cb9814e3d9788611f1dae9585915a2c0a0fc9e6a20ed990172b0f  iv31-1.7.0-linux-arm64.tar.gz
ce9836ef106adb6897214d45e5a976cf296eb879ec4ae372d0d2b86696f71e7a  iv31_1.7.0_amd64.deb
dacc587b8725f520c19baed10bcf54142f4bdf2e6c40900044e4cb56ab1f2a1b  iv31_1.7.0_arm64.deb
0ad9faf6bcc06eee760c2d040a272c5a39ddae92c25c259ecface2ea6dcf94b3  iv31-1.7.0-x86_64.AppImage
be4da5f1a27c9b578381dff12b6a3492d0c9b5839231a68aea72e8477274ebf3  iv31-1.7.0-aarch64.AppImage
```

## [1.6.8] - 2026-10-23

### Added
- **Pokémon data page** (`#dex/<number>`): base stats, the 2 stats to focus, proper nature, EV yield, locations, evolutions and type matchups, with buttons to check IVs, add to the party or add its EVs to the EV calculator. Every Pokémon name and number in the app links to it.
- **Back and Forward** buttons in the top bar (and on the data page), Alt+←/→ and mouse side buttons. The Android back gesture steps back through pages first.
- **Matchup strengths:** the matchup checker and data page show what the Pokémon's own types hit super effectively, per type for dual types.
- **Type chart multi-select:** click any number of types to highlight their rows and columns; **Clear** resets.

### Changed
- **Redesign** as a retro field-guide screen: green-screen palette with day (LCD) and night (phosphor) versions, scanlines, framed device panels, pixel headings (Silkscreen) and LCD number readouts (VT323), both bundled under the SIL Open Font License.

### Checksums (SHA-256)

```
1e372204d2ae6940f6809d2f935f226716f34df9d59b023d2823bafd58aae661  iv31-Setup-1.6.8.exe
f6c3abbdebe6f0572e8ff13311d43a715df7f1846eb2e323d95fe554fba5da7a  iv31-1.6.8-mac.zip
9e43357ceea55858e641fa5e40b1bc59a85b99b854e98cac295121baabd5d9b6  iv31-1.6.8-linux-x64.tar.gz
220c368f391285266012338adc3bf014c61c1af0bd6cb1776e4a3c3ce9c556b0  iv31-1.6.8-linux-arm64.tar.gz
a17ba41d730846546f68dab4539e9fec1ac8880004b0fa8a755bdf5287e46f61  iv31_1.6.8_amd64.deb
5ac9846e17223d99602cd48e452052712a3d826442b89a077a1938e351d635fe  iv31_1.6.8_arm64.deb
a4325ef02dadaebcbbab0cbf1289f6aea67ef9c7ce731cbb857a7759bd55be5c  iv31-1.6.8-x86_64.AppImage
555db718082cd87c100a914251fa51d16f41255a7a00d16cdff81969d10d8287  iv31-1.6.8-aarch64.AppImage
```

## [1.6.2] - 2026-10-17

### Changed
- The **Secret Power** tab is renamed **Powers** and has three charts behind tabs: **Hidden Power** (highest IVs and power for each type; the Attack/Defense DV type grid in Gen II; **Load** sends a row to the Hidden Power calculator), **Secret Power** (move and extra effect per ground, per area) and **Nature Power** (attack per area, grounds that give the same attack merged; terrain list for Gen VIII+). Links `#hiddenpower`, `#secret`, `#naturepower` and `#powers` open them.

### Checksums (SHA-256)

```
b8cdf3403af3483fb7c2d193b3b0e2b141836e0100299caecb0de8ccdc06d1a7  iv31-Setup-1.6.2.exe
ecb3987f7418207dd91b4494af14b451c3e8ab7c4cd5f3678463e8b1c4ae2483  iv31-1.6.2-mac.zip
76a8dd39f058f6ca2325fae40f7a4633d5da30ba192538d35e70affb84002cf3  iv31-1.6.2-linux-x64.tar.gz
57461d94eee43d85341b8824dbd50f6c82a8e58273c81720f521dc48d7d1bac7  iv31-1.6.2-linux-arm64.tar.gz
5d87de52797e39aade03061f8fb7d86db48f8e5fd05d86197aa551f2a49f6a8d  iv31_1.6.2_amd64.deb
5504d3a1a536b2df65e4a0648e2874e39208b9ac183b7f18fabf156820d6d245  iv31_1.6.2_arm64.deb
9a6b47afb7e5f2ddff6c15afb2da4b0c85f3556130956552d2ec407b34dcec66  iv31-1.6.2-x86_64.AppImage
a11649898d55a2baa88b051a8d59051b7d500ccabdd149a313804afca3747149  iv31-1.6.2-aarch64.AppImage
```

## [1.6.1] - 2026-10-17

### Added
- A **?** button in every section's title bar. Hover, click or tap it for what the section is for, step-by-step use, and how it works with the other sections. Lines about Full-only features are left out in the free tier. Text lives in `TIPS` in `src/index.html`.

### Checksums (SHA-256)

```
0701142ad1d1e6ab48d90ba123765b89b23489e1d0d1853ad900bcb6f0e55a9d  iv31-Setup-1.6.1.exe
321445ad4da6cd0d065a22265cec84a18a72c2b79f9c878e8372905902477874  iv31-1.6.1-mac.zip
c4d15a4dc59f6fffcc9e281e7ef411a852a9268d672a8ab95407350abb832ea1  iv31-1.6.1-linux-x64.tar.gz
54f5400d846dc03c7a7d01bb71266071692595f06d4b6564342629aacdc50cee  iv31-1.6.1-linux-arm64.tar.gz
bc3ff084fb38b98494fd790f37336757f82355c62ba0374a38033268a70242bd  iv31_1.6.1_amd64.deb
d53de50a2cc3d96375bccd0e5c52bb02a7327af9c6db35a2b35a1bca0f01294c  iv31_1.6.1_arm64.deb
c0631c8e9692eeb47df90565557829866c1648d0fb3fc359dd1d4e2f73036656  iv31-1.6.1-x86_64.AppImage
76a702d0f99ddb267b094e9a92583c8111f4d06fc7acec8bb3f1d95f0af64b9f  iv31-1.6.1-aarch64.AppImage
```

## [1.6.0] - 2026-10-17

### Added
- **EVs** choice on each level entry in the IV calculator: Not sure (default), None yet, Has battled. When EVs are raising a stat, the readout shows the IV range and EV range that fit, within 31 per IV, 255 per stat (252 from Gen VI) and 510 in total, instead of "No match". Gen I–II do the same for Stat Exp.
- **EVs gained** panel in the EV Training tab (Full): compares stats before and after training and shows the EVs gained per stat, the EVs it has now and the room left, with **Add to EV calculator**. Remembers what was typed.

### Changed
- The EV boxes are now **Known EVs (optional)**; a blank box no longer always means 0.

### Checksums (SHA-256)

```
72e8b5aab6b1e8b5ecebc2ad8610fd5fc8b29d379bdd5130dc76dd489b23c5a1  iv31-Setup-1.6.0.exe
df0f4f411211e501f5bbac095ca7605cd272f572e4fc72a32abd6587895c7424  iv31-1.6.0-mac.zip
bee8bd5724e5341052bcb154519cebf64db851ed062c12fe978b8e2bce7cfbdb  iv31-1.6.0-linux-x64.tar.gz
4336759f2e46670e4b33b5c2c6536d1e8c9e2925a98059877122b3f9f39f0501  iv31-1.6.0-linux-arm64.tar.gz
7f49d4dc5c361fde61b25734c9434f66dd94830a40f6bcc84d9a1ca3a7a752bc  iv31_1.6.0_amd64.deb
72b4c6fe3b169fa27c8298c42af7d561ac8992e92325499e7cf82cca197f9ad0  iv31_1.6.0_arm64.deb
121317e8aa56ded46c18ab3a41d68ce4577d77e5c95e2888b55a3173608fd54a  iv31-1.6.0-x86_64.AppImage
2e4daf1629656693603193e82ba18e56bb115c99130c5d2eb2b6f18283a253a7  iv31-1.6.0-aarch64.AppImage
```

## [1.5.4] - 2026-10-16

### Changed
- Story order in the EV Training table is a toggle (**Story order** checkbox or the **Found in** heading) instead of a sort column. It stays on while the EV filter is used, and a stat heading becomes the order within each place.

### Checksums (SHA-256)

```
39baae9429bd5f2b6a62ab9b9fbfa4b78e77a9164c89e4dff4690e6c10444b93  iv31-Setup-1.5.4.exe
2387fd9b05c70ca5741e5b8c220b5d5d6040601bc6a11b1d1d17c25585649f78  iv31-1.5.4-mac.zip
7755b6ecded9427fd9b95e4ed789f7ccba82373bae33d11852d4672095b40d87  iv31-1.5.4-linux-x64.tar.gz
1cf8b58baec95203f59ea8aa6aa0faf15a9dd92b9b3f5e2c227f2ae5fc32084d  iv31-1.5.4-linux-arm64.tar.gz
7d8f359149cbe4c25f8e79050b37d1970b81fbb513c38c942cf3f79cdc6d5c16  iv31_1.5.4_amd64.deb
2d2653d55f458999488fd5281d7c3cb4e926099fd7356a555ff93adf306c5a6c  iv31_1.5.4_arm64.deb
048907b0eb4a2b24ddb00277ac70adb317b54fe48b9935ebdad80195991d94ab  iv31-1.5.4-x86_64.AppImage
2126ee16ce748a83a5b3168dad784cc26476d367f69d76bafccc0beec4059e2f  iv31-1.5.4-aarch64.AppImage
```

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
