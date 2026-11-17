import csv
import io
import json
import re
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POKEAPI = "89aa167e486774d10d1502ee60bce41dc35f04b2"
BASE = f"https://raw.githubusercontent.com/PokeAPI/pokeapi/{POKEAPI}/data/v2/csv/"
CACHE = ROOT / ".cache" / "pokeapi" / POKEAPI
ENGLISH = "9"

MERGE = {"Sword: The Isle of Armor": "Sword", "Sword: The Crown Tundra": "Sword",
         "Shield: The Isle of Armor": "Shield", "Shield: The Crown Tundra": "Shield"}

METHOD_NAMES = {"walk": "Walking", "surf": "Surfing", "old-rod": "Old Rod", "good-rod": "Good Rod",
                "super-rod": "Super Rod", "rock-smash": "Rock Smash", "headbutt": "Headbutt",
                "seaweed": "Diving", "dark-grass": "Dark grass", "grass-spots": "Rustling grass",
                "cave-spots": "Dust clouds", "bridge-spots": "Bridge shadows", "surf-spots": "Rippling water",
                "super-rod-spots": "Fishing in rippling water", "only-one": "One-time", "gift": "Gift",
                "gift-egg": "Gift egg", "devon-scope": "Devon Scope", "pokeflute": "Poké Flute",
                "squirt-bottle": "Squirt Bottle", "wailmer-pail": "Wailmer Pail", "roaming-grass": "Roaming",
                "roaming-water": "Roaming on water", "honey-tree": "Honey tree", "pokeradar": "Poké Radar",
                "static": "Special encounter", "npc-trade": "Trade", "sos": "SOS calls", "horde": "Horde",
                "feebas-tile-fishing": "Feebas tiles (fishing)", "island-scan": "Island Scan",
                "hidden-grotto": "Hidden Grotto", "headbutt-low": "Headbutt (common trees)",
                "headbutt-high": "Headbutt (rare trees)", "headbutt-normal": "Headbutt"}

HIDDEN_METHODS = {"devon-scope", "only-one", "static", "pokeflute", "squirt-bottle", "wailmer-pail", "gift", "gift-egg",
                  "npc-trade", "feebas-tile-fishing", "island-scan", "hidden-grotto"}
SKIP_METHODS = {"max-raid", "dynamax-adventure"}
DEFAULT_CONDS = {"swarm-no", "radar-off", "slot2-none", "radio-off", "bug-catching-contest-no",
                 "story-progress-before-national-dex", "johto-safari-blocks-inactive", "other-none"}


def table(name):
    path = CACHE / f"{name}.csv"
    if not path.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(BASE + f"{name}.csv") as r:
            path.write_bytes(r.read())
    return list(csv.DictReader(io.StringIO(path.read_text(encoding="utf-8"))))


def english(rows, key):
    return {r[key]: r["name"] for r in rows if r["local_language_id"] == ENGLISH}


def area_label(identifier):
    if not identifier:
        return ""
    words = identifier.replace("-", " ").split()
    return " ".join(w.upper() if re.fullmatch(r"b?\d+f", w) else w if w in ("of", "and", "the") else w[:1].upper() + w[1:] for w in words)


def main():
    wanted = set(json.loads((ROOT / "src/data/locations.json").read_text(encoding="utf-8"))["found"])
    vname = english(table("version_names"), "version_id")
    lname = english(table("location_names"), "location_id")
    areas = {r["id"]: r for r in table("location_areas")}
    slots = {r["id"]: r for r in table("encounter_slots")}
    methods = {r["id"]: r["identifier"] for r in table("encounter_methods")}
    cvals = {r["id"]: r["identifier"] for r in table("encounter_condition_values")}
    cprose = english(table("encounter_condition_value_prose"), "encounter_condition_value_id")
    pokemon = {r["id"]: r for r in table("pokemon")}
    cmap = defaultdict(list)
    for r in table("encounter_condition_value_map"):
        cmap[r["encounter_id"]].append(r["encounter_condition_value_id"])

    groups = defaultdict(lambda: defaultdict(lambda: [0, 999, 0]))
    for e in table("encounters"):
        ver = MERGE.get(vname[e["version_id"]], vname[e["version_id"]])
        if ver not in wanted:
            continue
        area = areas[e["location_area_id"]]
        place = lname.get(area["location_id"])
        if not place:
            continue
        slot = slots[e["encounter_slot_id"]]
        method = methods[slot["encounter_method_id"]]
        if method in SKIP_METHODS:
            continue
        conds = tuple(sorted(cvals[c] for c in cmap[e["id"]] if cvals[c] not in DEFAULT_CONDS))
        mon = pokemon[e["pokemon_id"]]
        form = mon["identifier"].split("-", 1)[1] if mon["is_default"] != "1" and "-" in mon["identifier"] else ""
        key = (ver, place, area_label(area["identifier"]), method, conds)
        g = groups[key][(int(mon["species_id"]), form)]
        g[0] += int(slot["rarity"] or 0)
        g[1] = min(g[1], int(e["min_level"]))
        g[2] = max(g[2], int(e["max_level"]))

    method_list, cond_list, area_list, form_list, condset_list = [], [], [""], [""], [()]
    idx = lambda lst, v: lst.index(v) if v in lst else (lst.append(v) or len(lst) - 1)
    out = defaultdict(lambda: defaultdict(dict))
    for (ver, place, alabel, method, conds), mons in sorted(groups.items()):
        a = idx(area_list, alabel)
        m = idx(method_list, method)
        cs = idx(condset_list, tuple(idx(cond_list, c) for c in conds))
        rows = out[ver][place].setdefault(a, [])
        for (species, form), (rate, lo, hi) in sorted(mons.items(), key=lambda kv: (-kv[1][0], kv[0])):
            rows.append([species, idx(form_list, form), m, lo, hi, min(rate, 100), cs])

    pool, seen = [], {}

    def pooled(rows):
        k = json.dumps(rows, separators=(",", ":"))
        if k not in seen:
            seen[k] = len(pool)
            pool.append(rows)
        return seen[k]

    bexp = {}
    for p in pokemon.values():
        if p["is_default"] == "1" and p["base_experience"]:
            bexp[int(p["species_id"])] = int(p["base_experience"])
    data = {
        "source": f"PokeAPI {POKEAPI[:7]} (BSD 3-Clause)",
        "methods": [METHOD_NAMES.get(m, m.replace("-", " ").capitalize()) for m in method_list],
        "hiddenMethods": [i for i, m in enumerate(method_list) if m in HIDDEN_METHODS],
        "conds": [cprose.get(next(k for k, v in cvals.items() if v == c), c.replace("-", " ")) for c in cond_list],
        "condsets": [list(c) for c in condset_list],
        "areas": area_list,
        "forms": [f.replace("-", " ").title() for f in form_list],
        "bexp": [bexp.get(i, 0) for i in range(max(bexp) + 1)],
        "pool": pool,
        "v": {ver: {place: [[a, pooled(rows)] for a, rows in sorted(areas_.items())] for place, areas_ in sorted(places.items())}
              for ver, places in out.items()},
    }
    dest = ROOT / "src/data/routes.json"
    dest.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(dest.relative_to(ROOT), f"{dest.stat().st_size:,} bytes", f"{len(data['v'])} games",
          f"{sum(len(p) for p in data['v'].values()):,} places")


if __name__ == "__main__":
    sys.exit(main())
