"""Sync local flashcard Markdown files to Anki via AnkiConnect.

Reads all .md files in flashcards/, parses cards, sends new ones to Anki,
and writes back the anki_id to prevent duplicates on subsequent runs.

Usage:
    uv run python sync_anki.py
    uv run python sync_anki.py --dry-run     # preview without sending
    uv run python sync_anki.py --dir other/   # custom flashcards directory
"""

import argparse
import re
import sys
from pathlib import Path

import requests

ANKI_CONNECT_URL = "http://127.0.0.1:8765"
FLASHCARDS_DIR = Path("flashcards")


def invoke_anki(action: str, params: dict | None = None) -> dict:
    payload = {"action": action, "version": 6, "params": params or {}}
    resp = requests.post(ANKI_CONNECT_URL, json=payload, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    if data.get("error"):
        raise RuntimeError(f"AnkiConnect error: {data['error']}")
    return data


def get_deck_names() -> list[str]:
    data = invoke_anki("deckNames")
    return data.get("result") or []


def resolve_deck(requested: str | None, available: list[str]) -> str:
    if requested and requested in available:
        return requested
    for preferred in ("Default", "Padrão", "default"):
        if preferred in available:
            return preferred
    return available[0] if available else "Default"


def get_cloze_model() -> str | None:
    data = invoke_anki("modelNames")
    names = data.get("result") or []
    for candidate in (
        "Cloze",
        "Cloze (tipo de nota)",
        "Omissão de Palavras",
        "Lacunas",
    ):
        if candidate in names:
            return candidate
    for name in names:
        if "cloze" in name.lower() or "lacuna" in name.lower() or "omiss" in name.lower():
            return name
    return None


def get_basic_model_and_fields() -> tuple[str, list[str]]:
    data = invoke_anki("modelNames")
    names = data.get("result") or []
    for candidate in ("Básico", "Basic"):
        if candidate in names:
            fields_data = invoke_anki("modelFieldNames", {"modelName": candidate})
            return candidate, fields_data.get("result") or []
    if names:
        fields_data = invoke_anki("modelFieldNames", {"modelName": names[0]})
        return names[0], fields_data.get("result") or []
    raise RuntimeError("No note models found in Anki.")


def parse_frontmatter(text: str) -> dict:
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    meta = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            value = value.strip().strip('"').strip("'")
            if value.startswith("[") and value.endswith("]"):
                value = [v.strip().strip('"').strip("'") for v in value[1:-1].split(",")]
            meta[key.strip()] = value
    return meta


def parse_cards(text: str) -> list[dict]:
    body = re.sub(r"^---\s*\n.*?\n---\s*\n?", "", text, count=1, flags=re.DOTALL)
    raw_cards = re.split(r"\n---\s*\n", body)
    cards = []
    for block in raw_cards:
        block = block.strip()
        if not block:
            continue

        card: dict = {}

        header_match = re.match(r"^##\s+Card\s+\d+", block)
        if not header_match:
            continue

        id_match = re.search(r"^id:\s*(.+)$", block, re.MULTILINE)
        card["id"] = id_match.group(1).strip() if id_match else None

        anki_match = re.search(r"^anki_id:\s*(.*)$", block, re.MULTILINE)
        raw_anki = anki_match.group(1).strip() if anki_match else ""
        card["anki_id"] = int(raw_anki) if raw_anki and raw_anki.isdigit() else None

        tags_match = re.search(r"^tags:\s*(.+)$", block, re.MULTILINE)
        card["tags"] = (
            [t.strip() for t in tags_match.group(1).split(",") if t.strip()]
            if tags_match
            else []
        )

        type_match = re.search(r"^type:\s*(.+)$", block, re.MULTILINE)
        card["type"] = type_match.group(1).strip() if type_match else "basic"

        front_match = re.search(
            r"\*\*Front:\*\*\s*(.*?)(?=\n\s*\*\*Back:\*\*|\Z)",
            block,
            re.DOTALL,
        )
        card["front"] = front_match.group(1).strip() if front_match else ""

        back_match = re.search(r"\*\*Back:\*\*\s*(.*)", block, re.DOTALL)
        card["back"] = back_match.group(1).strip() if back_match else ""

        if card["id"] and card["front"]:
            cards.append(card)

    return cards


def add_card_to_anki(
    card: dict,
    deck: str,
    basic_model: str,
    basic_fields: list[str],
    cloze_model: str | None,
) -> int:
    tags = card.get("tags", []) + ["flashcard-sync"]

    if card["type"] == "cloze" and cloze_model:
        note = {
            "deckName": deck,
            "modelName": cloze_model,
            "fields": {"Texto": card["front"], "Extra": card["back"]},
            "tags": tags,
            "options": {"allowDuplicate": False},
        }
        try:
            data = invoke_anki("addNote", {"note": note})
            return data["result"]
        except RuntimeError:
            cloze_fields = invoke_anki(
                "modelFieldNames", {"modelName": cloze_model}
            ).get("result", [])
            fields = {}
            if len(cloze_fields) >= 1:
                fields[cloze_fields[0]] = card["front"]
            if len(cloze_fields) >= 2:
                fields[cloze_fields[1]] = card["back"]
            note["fields"] = fields
            data = invoke_anki("addNote", {"note": note})
            return data["result"]
    else:
        fields = {}
        if len(basic_fields) >= 2:
            fields[basic_fields[0]] = card["front"]
            fields[basic_fields[1]] = card["back"]
        elif basic_fields:
            fields[basic_fields[0]] = f"{card['front']}\n\n{card['back']}"
        note = {
            "deckName": deck,
            "modelName": basic_model,
            "fields": fields,
            "tags": tags,
            "options": {"allowDuplicate": False},
        }
        data = invoke_anki("addNote", {"note": note})
        return data["result"]


def update_anki_id_in_file(filepath: Path, card_id: str, anki_id: int) -> None:
    content = filepath.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"(id:[ \t]*{re.escape(card_id)}[ \t]*\nanki_id:)[ \t]*(.*)",
        re.MULTILINE,
    )
    new_content = pattern.sub(rf"\g<1> {anki_id}", content)
    filepath.write_text(new_content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync flashcards to Anki.")
    parser.add_argument(
        "--dir",
        default=str(FLASHCARDS_DIR),
        help="Directory containing flashcard .md files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be synced without sending to Anki.",
    )
    args = parser.parse_args()

    flashcards_dir = Path(args.dir)
    if not flashcards_dir.is_dir():
        print(f"Directory not found: {flashcards_dir}")
        sys.exit(1)

    md_files = sorted(flashcards_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {flashcards_dir}/")
        sys.exit(0)

    deck_names: list[str] = []
    if not args.dry_run:
        try:
            deck_names = get_deck_names()
            basic_model, basic_fields = get_basic_model_and_fields()
            cloze_model = get_cloze_model()
        except requests.exceptions.RequestException:
            print(
                "Cannot connect to AnkiConnect at http://127.0.0.1:8765.\n"
                "Open Anki Desktop with the AnkiConnect add-on enabled."
            )
            sys.exit(1)

    synced = 0
    skipped = 0
    errors = 0

    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        file_deck = meta.get("deck", None)
        cards = parse_cards(text)

        if not cards:
            continue

        print(f"\n--- {md_file.name} ({len(cards)} cards) ---")

        for card in cards:
            if card["anki_id"]:
                print(f"  SKIP {card['id']} (already synced: {card['anki_id']})")
                skipped += 1
                continue

            if args.dry_run:
                front_preview = card["front"][:60].replace("\n", " ")
                print(f"  WOULD SYNC {card['id']}: {front_preview}...")
                synced += 1
                continue

            try:
                target_deck = resolve_deck(file_deck, deck_names)
                anki_id = add_card_to_anki(
                    card, target_deck, basic_model, basic_fields, cloze_model
                )
                update_anki_id_in_file(md_file, card["id"], anki_id)
                print(f"  OK {card['id']} → anki_id={anki_id}")
                synced += 1
            except RuntimeError as exc:
                print(f"  ERROR {card['id']}: {exc}")
                errors += 1

    print(f"\nDone: {synced} synced, {skipped} skipped, {errors} errors.")


if __name__ == "__main__":
    main()
