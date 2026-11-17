import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_routes import ROOT, ENGLISH, table

LINEAGE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 20, 23, 25]
SAME = {21: 20, 22: 20, 26: 25, 27: 25}
REGION = {1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 1, 8: 4, 9: 4, 10: 2, 11: 5, 14: 5, 15: 6, 16: 3, 17: 7, 18: 7, 20: 8, 23: 4, 25: 10}
SIDE = {19: "Let's Go Pikachu/Eevee", 24: "Legends: Arceus", 30: "Legends: Z-A"}
BEAUTY = {5, 6, 8, 9, 16}
AFFECTION = {15, 16, 17, 18}
NO_CLOCK = {1, 2, 7}
NO_HELD = {1, 2}
TIME = {"day": "during the day", "night": "at night", "dusk": "at dusk", "full-moon": "under a full moon"}
STATS = {"1": "with Attack higher than Defense", "-1": "with Defense higher than Attack", "0": "with Attack equal to Defense"}
ROCK = {"leafeon": "Moss Rock", "glaceon": "Ice Rock"}
REGIONAL = {"alola": "Alolan", "galar": "Galarian", "hisui": "Hisuian", "paldea": "Paldean"}


def main():
    names = {r["pokemon_species_id"]: r["name"] for r in table("pokemon_species_names") if r["local_language_id"] == ENGLISH}
    species = {r["id"]: r for r in table("pokemon_species")}
    items = {r["item_id"]: r["name"] for r in table("item_names") if r["local_language_id"] == ENGLISH}
    moves = {r["move_id"]: r["name"] for r in table("move_names") if r["local_language_id"] == ENGLISH}
    types = {r["type_id"]: r["name"] for r in table("type_names") if r["local_language_id"] == ENGLISH}
    places = {r["location_id"]: r["name"] for r in table("location_names") if r["local_language_id"] == ENGLISH}
    place_region = {r["id"]: int(r["region_id"] or 0) for r in table("locations")}
    forms = {r["id"]: r for r in table("pokemon_forms")}
    form_names = {r["pokemon_form_id"]: r["form_name"] for r in table("pokemon_form_names") if r["local_language_id"] == ENGLISH}
    nature_names = {r["nature_id"]: r["name"] for r in table("nature_names") if r["local_language_id"] == ENGLISH}
    natures = sorted(nature_names, key=int)
    version_names = {r["version_id"]: r["name"] for r in table("version_names") if r["local_language_id"] == ENGLISH}
    group_versions = defaultdict(list)
    for v in table("versions"):
        if v["id"] in version_names:
            group_versions[int(v["version_group_id"])].append(version_names[v["id"]])

    def form_label(fid):
        f = forms.get(fid)
        if not f or f["is_default"] == "1" and not f["form_identifier"]:
            return ""
        ident = f["form_identifier"]
        if ident in REGIONAL:
            return f"{REGIONAL[ident]} form"
        return form_names.get(fid, ident.replace("-", " ").title())

    def an(word):
        return f"{'an' if word[:1].upper() in 'AEIOU' else 'a'} {word}"

    def describe(r):
        target = species[r["evolved_species_id"]]["identifier"]
        trig = r["evolution_trigger_id"]
        parts, after = [], []
        loc = ""
        if r["location_id"]:
            loc = places.get(r["location_id"], "")
        if trig == "1" or trig == "10":
            parts.append(f"Level {r['minimum_level']}" if r["minimum_level"] else "Level up")
            if trig == "10":
                parts.append("in battle")
        elif trig == "2":
            parts.append("Trade")
        elif trig == "3":
            parts.append(f"Use {an(items.get(r['trigger_item_id'], 'item'))}")
        elif trig == "4":
            return "Appears when Nincada evolves at level 20, if you have a free party slot and a spare Poké Ball", ""
        elif trig == "5":
            return "Hold a Sweet and spin your character around; the spin direction, length and time of day decide its flavor", ""
        elif trig == "6":
            return "Read the scroll at the top of the Tower of Darkness (becomes Single Strike Style)", ""
        elif trig == "7":
            return "Read the scroll at the top of the Tower of Waters (becomes Rapid Strike Style)", ""
        elif trig == "8":
            parts.append("Land 3 critical hits in one battle")
        elif trig == "9":
            return f"Take at least {r['minimum_damage_taken']} damage without fainting, then walk under the stone arch in {loc or 'Dusty Bowl'} (Galarian form only)", ""
        elif trig in ("11", "12"):
            parts.append(f"Use {moves.get(r['used_move_id'], 'a move')} in {'Agile' if trig == '11' else 'Strong'} Style {r['minimum_move_count']} times, then level up")
        elif trig == "13":
            parts.append(f"Lose at least {r['minimum_damage_taken']} HP from recoil without fainting, then level up")
        elif trig == "14":
            parts.append(f"Use {moves.get(r['used_move_id'], 'a move')} {r['minimum_move_count']} times, then level up")
        elif trig == "15":
            parts.append("Defeat 3 Bisharp holding a Leader's Crest, then level up")
        elif trig == "16":
            parts.append("Level up with 999 Gimmighoul Coins in your bag")
        elif trig == "17":
            return "Feed 400 Meltan Candy in Pokémon GO", ""
        else:
            parts.append("Special method")
        if r["held_item_id"]:
            parts.append(f"holding {an(items.get(r['held_item_id'], 'item'))}")
        if r["trade_species_id"]:
            parts.append(f"for {an(names.get(r['trade_species_id'], ''))}")
        if r["minimum_happiness"]:
            parts.append("with high friendship")
        if r["minimum_affection"]:
            parts.append("with 2+ Affection hearts")
        if r["minimum_beauty"]:
            parts.append("with high Beauty")
        if r["known_move_id"]:
            parts.append(f"knowing {moves.get(r['known_move_id'], 'a move')}")
        if r["known_move_type_id"]:
            parts.append(f"knowing {an(types.get(r['known_move_type_id'], ''))}-type move")
        if r["party_species_id"]:
            parts.append(f"with {names.get(r['party_species_id'], '')} in your party")
        if r["party_type_id"]:
            parts.append(f"with {an(types.get(r['party_type_id'], ''))}-type Pokémon in your party")
        if r["relative_physical_stats"]:
            parts.append(STATS[r["relative_physical_stats"]])
        if r["needs_overworld_rain"] == "1":
            parts.append("while it's raining")
        if r["turn_upside_down"] == "1":
            parts.append("while holding the console upside down")
        if r["minimum_steps"]:
            parts.append(f"after walking {int(r['minimum_steps']):,} steps with it following you")
        if loc:
            on = "on" if loc.startswith(("Route", "Sea Route")) else "in"
            parts.append(f"near the {ROCK[target]} {on} {{L}}" if r["near_special_rock"] == "1" and target in ROCK else ("on {L}" if on == "on" else "at {L}"))
        if r["time_of_day"]:
            parts.append(TIME.get(r["time_of_day"], r["time_of_day"]))
        if r["gender_id"]:
            after.append("females only" if r["gender_id"] == "1" else "males only")
        if r["required_pokemon_form_id"]:
            req = form_label(r["required_pokemon_form_id"])
            if req:
                after.append(f"{req} only")
        out = form_label(r["evolved_pokemon_form_id"]) if r["evolved_pokemon_form_id"] else ""
        if r["gender_id"]:
            out = ""
        if r["nature_bitmask"] and out:
            mask = int(r["nature_bitmask"])
            after.append(f"{out} with " + ", ".join(nature_names[n] for i, n in enumerate(natures) if mask >> i & 1) + " natures")
        elif r["percentage_chance"] and r["percentage_chance"] != "100":
            after.append(f"{r['percentage_chance']}% chance" + (f", becomes {out}" if out else ""))
        elif out:
            after.append(f"becomes {out}")
        text = " ".join(p for p in parts if p)
        if after:
            text += f" ({'; '.join(after)})"
        return text, loc

    rows = []
    for r in table("pokemon_evolution"):
        vg = SAME.get(int(r["version_group_id"]), int(r["version_group_id"]))
        side = vg in SIDE
        if vg not in LINEAGE and not side:
            continue
        text, loc = describe(r)
        region = int(r["region_id"] or 0) or (place_region.get(r["location_id"], 0) if r["location_id"] else 0)
        kind = "|".join([r["evolution_trigger_id"], "L" if r["location_id"] else "", r["required_pokemon_form_id"],
                         "" if r["region_id"] else r["evolved_pokemon_form_id"], r["gender_id"]])
        blocked = []
        for i, g in enumerate(LINEAGE):
            if r["minimum_beauty"] and g not in BEAUTY or r["minimum_affection"] and g not in AFFECTION \
                    or r["time_of_day"] and g in NO_CLOCK or r["held_item_id"] and g in NO_HELD \
                    or r["evolution_trigger_id"] in ("6", "7") and g != 20:
                blocked.append(i)
        rows.append([int(r["evolved_species_id"]), LINEAGE.index(vg) if not side else -1, region, kind, text, loc, blocked,
                     SIDE.get(vg, "")])
    seen, unique = set(), []
    for row in rows:
        key = json.dumps(row[:6] + [row[7]])
        if key not in seen:
            seen.add(key)
            unique.append(row)
    dex = json.loads((ROOT / "src/data/pokedex.json").read_text(encoding="utf-8"))["dex"]
    listed = {k for p in dex for k in p[7]}
    extra = defaultdict(list)
    for sid, sp in species.items():
        n, parent = int(sid), sp["evolves_from_species_id"]
        if parent and n <= len(dex) and n not in listed and n in {row[0] for row in unique}:
            extra[parent].append(n)
    data = {"extra": {k: sorted(v) for k, v in sorted(extra.items(), key=lambda kv: int(kv[0]))}, "region": [REGION[g] for g in LINEAGE], "names": ["/".join(group_versions[g]) for g in LINEAGE],
            "vers": {v: i for i, g in enumerate(LINEAGE) for v in group_versions[g]}, "rows": unique}
    (ROOT / "src/data/evolutions.json").write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"{len(unique)} evolution rows")


if __name__ == "__main__":
    main()
