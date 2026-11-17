import json
import re
import struct
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "pret"
REPOS = {
    "pokeruby": "5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f",
    "pokeemerald": "9103e529c2fbdd7add4a1ff3350c6c1f92112c42",
    "pokefirered": "ce6406d8c2eaf46d543c8a2606de0c3cb1951982",
}
GAMES = {"Ruby": "pokeruby", "Sapphire": "pokeruby", "Emerald": "pokeemerald", "FireRed": "pokefirered", "LeafGreen": "pokefirered"}
SPARSE = ["/data/maps/", "/data/layouts/", "/data/tilesets/*/*/metatile_attributes.bin", "/src/data/region_map/",
          "/include/constants/metatile_behaviors.h", "/data/scripts/item_ball_scripts.inc", "/data/item_ball_scripts.inc"]
ALIASES = {"Kanto Victory Road": "Victory Road", "Kanto Safari Zone": "Safari Zone", "Power Plant": "Kanto Power Plant",
           "Underground Path": "Kanto Underground Path", "Route 19": "Sea Route 19", "Route 20": "Sea Route 20",
           "Route 21": "Sea Route 21", "Viapois Chamber": "Viapos Chamber", "Aqua Hideout": "Team Aqua Hideout",
           "Magma Hideout": "Team Magma Hideout", "Battle Frontier": "Hoenn Battle Frontier"}
SKIP_PLACES = {"Special Area", "Sevii Isle 6", "Sevii Isle 7", "Sevii Isle 8", "Sevii Isle 9", "Trainer Tower 2", "Underground Path 2"}
RENAME = {"Ruby": {"Evil Team Hideout": "Team Magma Hideout"}, "Sapphire": {"Evil Team Hideout": "Team Aqua Hideout"}}
WATER = {"MB_POND_WATER", "MB_INTERIOR_DEEP_WATER", "MB_DEEP_WATER", "MB_SOOTOPOLIS_DEEP_WATER", "MB_OCEAN_WATER",
         "MB_WATERFALL", "MB_EASTWARD_CURRENT", "MB_WESTWARD_CURRENT", "MB_NORTHWARD_CURRENT", "MB_SOUTHWARD_CURRENT"}
GFX = {"cut": ("CUT_TREE", "CUTTABLE_TREE"), "rocksmash": ("BREAKABLE_ROCK", "ROCK_SMASH_ROCK"), "strength": ("PUSHABLE_BOULDER",)}
ITEM_FIX = {"POKE BALL": "Poké Ball", "HP UP": "HP Up", "PP UP": "PP Up", "PP MAX": "PP Max", "X SPECIAL": "X Special",
            "X ATTACK": "X Attack", "X DEFEND": "X Defend", "X SPEED": "X Speed", "X ACCURACY": "X Accuracy",
            "TINY MUSHROOM": "Tiny Mushroom", "BLACKGLASSES": "Black Glasses", "NEVERMELTICE": "Never-Melt Ice",
            "TWISTEDSPOON": "Twisted Spoon", "SILVERPOWDER": "Silver Powder", "DEEPSEATOOTH": "Deep Sea Tooth",
            "DEEPSEASCALE": "Deep Sea Scale", "KINGS ROCK": "King's Rock", "BRIGHTPOWDER": "Bright Powder"}


def fetch(repo):
    path = CACHE / repo
    if not (path / ".git").exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", "-q", "--filter=blob:none", "--no-checkout", f"https://github.com/pret/{repo}.git", str(path)], check=True)
    subprocess.run(["git", "-C", str(path), "sparse-checkout", "set", "--no-cone", *SPARSE], check=True)
    subprocess.run(["git", "-C", str(path), "checkout", "-q", REPOS[repo]], check=True)
    return path


def item_name(const):
    words = const.removeprefix("ITEM_").replace("_", " ")
    tm = re.fullmatch(r"(TM|HM) ?(\d+)( .*)?", words)
    if tm:
        return f"{tm.group(1)}{tm.group(2)}" + (tm.group(3).title() if tm.group(3) else "")
    return ITEM_FIX.get(words, words.title())


def behaviors(path):
    text = (path / "include/constants/metatile_behaviors.h").read_text()
    defs = dict(re.findall(r"#define\s+(MB_\w+)\s+(0x[0-9A-Fa-f]+|\d+)", text))
    if defs:
        return {k: int(v, 0) for k, v in defs.items()}
    body = text[text.index("{"):text.index("}")]
    names = re.findall(r"^\s*(MB_\w+)", body, re.M)
    return {n: i for i, n in enumerate(names)}


def tileset_index(path):
    out = {}
    for f in (path / "data/tilesets").glob("*/*/metatile_attributes.bin"):
        out[f.parent.name.replace("_", "").lower()] = f
    return out


def layout_tiles(path, layout, tilesets, frlg):
    blocks = (path / layout["blockdata_filepath"]).read_bytes()
    size = 4 if frlg else 2
    mask = 0x1FF if frlg else 0xFF
    split = 640 if frlg else 512

    def attrs(sym):
        f = tilesets.get(sym.removeprefix("gTileset_").lower())
        if not f:
            return []
        raw = f.read_bytes()
        return [struct.unpack_from("<I" if frlg else "<H", raw, i)[0] & mask for i in range(0, len(raw), size)]

    prim, sec = attrs(layout["primary_tileset"]), attrs(layout["secondary_tileset"])
    out = []
    for i in range(0, len(blocks), 2):
        mt = struct.unpack_from("<H", blocks, i)[0] & 0x3FF
        b = prim[mt] if mt < split and mt < len(prim) else (sec[mt - split] if mt >= split and mt - split < len(sec) else 0)
        out.append(b)
    return out, layout["width"], layout["height"]


def where(x, y, w, h):
    ns = "north" if y < h / 3 else "south" if y >= 2 * h / 3 else ""
    ew = "west" if x < w / 3 else "east" if x >= 2 * w / 3 else ""
    return f"{ns}-{ew}" if ns and ew else ns or ew or "middle"


def split_words(s):
    s = re.sub(r"(?<=[a-z])(?=[A-Z0-9])|(?<=[0-9])(?=[A-Z][a-z])", " ", s).replace("_", " ")
    return re.sub(r"\s+", " ", s).strip()


def norm(s):
    s = s.lower().replace("mount", "mt").replace("é", "e")
    return re.sub(r"[^a-z0-9]", "", s)


def section_name(sec):
    words = sec.removeprefix("MAPSEC_").replace("_", " ").title()
    words = re.sub(r"\bMt\b", "Mt.", words)
    return words.replace("Ss Anne", "S.S. Anne").replace("Pokemon", "Pokémon")


def region_grids(path, repo):
    grids = []
    rm = path / "src/data/region_map"
    if repo == "pokefirered":
        for f, label in (("region_map_layout_kanto.h", "Kanto"), ("region_map_layout_sevii_123.h", "Sevii Islands 1-3"),
                         ("region_map_layout_sevii_45.h", "Sevii Islands 4-5"), ("region_map_layout_sevii_67.h", "Sevii Islands 6-7")):
            text = (rm / f).read_text()
            layers = re.split(r"\[LAYER_(\w+)\]\s*=", text)[1:]
            got = {}
            for name, body in zip(layers[0::2], layers[1::2]):
                got[name] = [re.findall(r"MAPSEC_\w+", row) for row in re.findall(r"\{([^{}]*)\}", body)]
            grids.append((label, got.get("MAP", []), got.get("DUNGEON", [])))
    else:
        text = (rm / "region_map_layout.h").read_text().split("=", 1)[1]
        rows = [re.findall(r"MAPSEC_\w+", row) for row in re.findall(r"\{([^{}]*)\}", text)]
        if len(rows) == 1:
            flat = rows[0]
            rows = [flat[i:i + 28] for i in range(0, len(flat), 28)]
        grids.append(("Hoenn", rows, []))
    return grids


def build(repo, version_places):
    path = fetch(repo)
    frlg = repo == "pokefirered"
    mb = behaviors(path)
    water = {mb[k] for k in WATER if k in mb}
    fall = mb.get("MB_WATERFALL")
    tilesets = tileset_index(path)
    layouts = {l["id"]: l for l in json.loads((path / "data/layouts/layouts.json").read_text())["layouts"] if "blockdata_filepath" in l}
    items = {}
    for f in [path / "data/scripts/item_ball_scripts.inc", path / "data/item_ball_scripts.inc"]:
        if f.exists():
            items.update(re.findall(r"^(\w+)::.*\n\s*(?:finditem|giveitem_std|finditem_std)\s+(ITEM_\w+)", f.read_text(), re.M))
    maps = {}
    for f in sorted((path / "data/maps").glob("*/map.json")):
        m = json.loads(f.read_text())
        maps[m["id"]] = m
    names = {}
    for p in version_places:
        names.setdefault(norm(p), p)
    def place_of(sec):
        n = norm(section_name(sec))
        if re.fullmatch(r"underwater\d+", n):
            n = "route" + n[10:]
        if n in names:
            return names[n]
        got = section_name(sec)
        alias = ALIASES.get(got)
        return names[norm(alias)] if alias and norm(alias) in names else got

    places = defaultdict(lambda: {"items": [], "hidden": [], "hm": set(), "dive": set(), "surface": set(), "links": set(), "maps": 0})
    for mid, m in maps.items():
        sec = m.get("region_map_section", "MAPSEC_NONE")
        if sec in ("MAPSEC_NONE", "MAPSEC_DYNAMIC", "MAPSEC_SECRET_BASE", "MAPSEC_INSIDE_OF_TRUCK"):
            continue
        pl = place_of(sec)
        if pl in SKIP_PLACES:
            continue
        P = places[pl]
        P["maps"] += 1
        base = norm(m["name"].split("_")[0])
        label = split_words(m["name"].split("_", 1)[1]) if "_" in m["name"] and norm(section_name(sec)) in base + "x" or "_" in m["name"] else ""
        if not norm(m["name"]).startswith(norm(section_name(sec)).replace("underwaterroute", "underwater")) and "_" not in m["name"]:
            label = split_words(m["name"])
        if norm(label).startswith("underwater") or m["name"].lower().startswith("underwater"):
            label = "Underwater"
            P["underwater"] = True
        lay = layouts.get(m.get("layout"))
        tiles, w, h = layout_tiles(path, lay, tilesets, frlg) if lay else ([], 1, 1)
        spot = lambda x, y: (f"{label}, " if label else "") + where(x, y, w, h)
        for o in m.get("object_events", []):
            g = o.get("graphics_id", "")
            if g.endswith("ITEM_BALL") and o.get("script") in items:
                P["items"].append([item_name(items[o["script"]]), spot(o["x"], o["y"])])
            for k, keys in GFX.items():
                if any(g.endswith(x) for x in keys):
                    P["hm"].add(k)
        for b in m.get("bg_events", []):
            if b.get("type") == "hidden_item" and b.get("item", "").startswith("ITEM_"):
                q = int(b.get("quantity", 1) or 1)
                P["hidden"].append([item_name(b["item"]) + (f" ×{q}" if q > 1 else ""), spot(b["x"], b["y"])])
        if tiles:
            if fall is not None and fall in tiles:
                P["hm"].add("waterfall")
            if any(t in water for t in tiles):
                P["hm"].add("surf")
        if m.get("requires_flash"):
            P["hm"].add("flash")
        for c in m.get("connections") or []:
            other = maps.get(c["map"])
            if not other:
                continue
            op = place_of(other.get("region_map_section", "MAPSEC_NONE"))
            if c["direction"] == "dive":
                P["hm"].add("dive")
                if op != pl:
                    P["dive"].add(op)
            elif c["direction"] == "emerge":
                if op != pl:
                    P["surface"].add(op)
            elif op != pl and op not in SKIP_PLACES:
                P["links"].add(op)
        for wp in m.get("warp_events", []):
            other = maps.get(wp.get("dest_map"))
            if other and other.get("region_map_section") not in ("MAPSEC_NONE", "MAPSEC_DYNAMIC", None):
                op = place_of(other["region_map_section"])
                if op != pl and op not in SKIP_PLACES:
                    P["links"].add(op)
    for pl, P in places.items():
        for op in P["links"]:
            if op in places:
                places[op]["links"].add(pl)

    sections = {}
    secfile = path / "src/data/region_map/region_map_sections.json"
    for s in json.loads(secfile.read_text())["map_sections"]:
        if "x" in s:
            sections[s["id"]] = [s["x"], s["y"], s.get("width", 1), s.get("height", 1)]
    regions = []
    for label, grid, dungeon in region_grids(path, repo):
        cells = defaultdict(list)
        for y, row in enumerate(grid):
            for x, sec in enumerate(row):
                if sec not in ("MAPSEC_NONE",):
                    cells[place_of(sec)].append([x, y])
        dots = defaultdict(list)
        for y, row in enumerate(dungeon):
            for x, sec in enumerate(row):
                if sec != "MAPSEC_NONE":
                    dots[place_of(sec)].append([x, y])
        if not frlg:
            for sec, (x, y, sw, sh) in sections.items():
                pl = place_of(sec)
                if pl not in cells and pl in places:
                    dots[pl].append([x, y])
        regions.append({"name": label, "w": max((len(r) for r in grid), default=0), "h": len(grid),
                        "cells": dict(cells), "dots": dict(dots)})
    for g in regions:
        for k in ("cells", "dots"):
            g[k] = {p: v for p, v in g[k].items() if p not in SKIP_PLACES}
    out = {}
    for pl, P in places.items():
        out[pl] = {k: (sorted(v) if isinstance(v, set) else v) for k, v in P.items() if v and k != "maps"}
    return {"places": out, "regions": regions}


def rename(d, names):
    if not names:
        return d
    r = lambda p: names.get(p, p)
    places = {r(k): {**v, **{f: [r(x) for x in v[f]] for f in ("links", "dive", "surface") if f in v}} for k, v in d["places"].items()}
    regions = [{**g, "cells": {r(k): v for k, v in g["cells"].items()}, "dots": {r(k): v for k, v in g["dots"].items()}} for g in d["regions"]]
    return {"places": places, "regions": regions}


def main():
    routes = json.loads((ROOT / "src/data/routes.json").read_text(encoding="utf-8"))
    loc = json.loads((ROOT / "src/data/locations.json").read_text(encoding="utf-8"))
    data, done = {}, {}
    for ver, repo in GAMES.items():
        known = list(routes["v"].get(ver, {})) + sorted({loc["locs"][li] for lst in loc["found"].get(ver, {}).values() for li, _ in lst})
        if repo not in done:
            done[repo] = build(repo, known)
        data[ver] = rename(done[repo], RENAME.get(ver, {}))
    dest = ROOT / "src/data/gen3maps.json"
    dest.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(dest.relative_to(ROOT), f"{dest.stat().st_size:,} bytes")


if __name__ == "__main__":
    sys.exit(main())
