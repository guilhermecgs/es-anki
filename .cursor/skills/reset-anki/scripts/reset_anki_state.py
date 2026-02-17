#!/usr/bin/env python3
"""Reset Anki state for this repository.

Actions:
1) Optionally delete all notes in Anki via AnkiConnect.
2) Move `flashcards/` to a timestamped backup folder.
3) Recreate an empty `flashcards/` folder.
4) Clear all `anki_id` values in backed up markdown files (set to empty).
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.error import URLError
from urllib.request import Request, urlopen


def load_config(project_root: Path) -> dict[str, Any]:
    config_path = project_root / "sync_anki.config.json"
    if not config_path.exists():
        return {}
    with config_path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def ankiconnect(url: str, action: str, params: dict[str, Any] | None = None) -> Any:
    payload = {
        "action": action,
        "version": 6,
        "params": params or {},
    }
    data = json.dumps(payload).encode("utf-8")
    req = Request(url=url, data=data, headers={"Content-Type": "application/json"})
    with urlopen(req, timeout=10) as resp:  # nosec B310 - local endpoint by design
        body = json.loads(resp.read().decode("utf-8"))
    if body.get("error"):
        raise RuntimeError(f"AnkiConnect error on {action}: {body['error']}")
    return body.get("result")


def wipe_anki_notes(url: str, dry_run: bool) -> int:
    try:
        ankiconnect(url, "version")
    except (URLError, RuntimeError) as exc:
        raise RuntimeError(
            "Could not connect to AnkiConnect. Open Anki Desktop and check the "
            "AnkiConnect addon, or run with --skip-anki-cleanup."
        ) from exc

    note_ids = ankiconnect(url, "findNotes", {"query": ""}) or []
    if dry_run:
        return len(note_ids)

    if note_ids:
        ankiconnect(url, "deleteNotes", {"notes": note_ids})
    return len(note_ids)


def clear_anki_ids_in_dir(target_dir: Path) -> tuple[int, int]:
    md_files = list(target_dir.rglob("*.md"))
    files_changed = 0
    ids_reset = 0
    pattern = re.compile(r"(?m)^(anki_id\s*:).*$")

    for md in md_files:
        content = md.read_text(encoding="utf-8")
        updated, replacements = pattern.subn(r"\g<1>", content)
        if replacements:
            md.write_text(updated, encoding="utf-8")
            files_changed += 1
            ids_reset += replacements

    return files_changed, ids_reset


def move_flashcards_to_backup(
    project_root: Path,
    flashcards_dir_name: str,
    backup_root_name: str,
    dry_run: bool,
) -> tuple[Path, Path, bool]:
    flashcards_dir = project_root / flashcards_dir_name
    backup_root = project_root / backup_root_name
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_run_dir = backup_root / f"anki-reset-{timestamp}"
    backup_flashcards_dir = backup_run_dir / "flashcards"

    moved = False
    if dry_run:
        return flashcards_dir, backup_flashcards_dir, moved

    backup_run_dir.mkdir(parents=True, exist_ok=True)
    if flashcards_dir.exists():
        shutil.move(str(flashcards_dir), str(backup_flashcards_dir))
        moved = True

    flashcards_dir.mkdir(parents=True, exist_ok=True)
    return flashcards_dir, backup_flashcards_dir, moved


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Reset local + remote Anki state.")
    parser.add_argument(
        "--project-root",
        default=".",
        help="Project root where sync_anki.config.json lives (default: current directory).",
    )
    parser.add_argument(
        "--backup-dir",
        default="backup",
        help="Relative backup base directory inside project root (default: backup).",
    )
    parser.add_argument(
        "--skip-anki-cleanup",
        action="store_true",
        help="Skip deleting notes in Anki (useful if you already deleted everything there).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without modifying files or Anki.",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Confirm destructive actions (required unless --dry-run).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).resolve()
    config = load_config(project_root)

    flashcards_dir_name = str(config.get("flashcards_dir", "flashcards"))
    anki_connect_url = str(config.get("anki_connect_url", "http://127.0.0.1:8765"))

    if not args.dry_run and not args.yes:
        print("Refusing to run without confirmation. Re-run with --yes (or use --dry-run).")
        return 2

    summary: dict[str, Any] = {
        "project_root": str(project_root),
        "flashcards_dir": flashcards_dir_name,
        "backup_dir": args.backup_dir,
        "dry_run": args.dry_run,
        "anki_cleanup_skipped": args.skip_anki_cleanup,
        "deleted_notes_count": 0,
        "moved_flashcards": False,
        "backup_flashcards_path": None,
        "reset_anki_id_files": 0,
        "reset_anki_id_entries": 0,
    }

    try:
        if not args.skip_anki_cleanup:
            summary["deleted_notes_count"] = wipe_anki_notes(
                anki_connect_url, dry_run=args.dry_run
            )

        _, backup_flashcards_dir, moved = move_flashcards_to_backup(
            project_root=project_root,
            flashcards_dir_name=flashcards_dir_name,
            backup_root_name=args.backup_dir,
            dry_run=args.dry_run,
        )
        summary["moved_flashcards"] = moved
        summary["backup_flashcards_path"] = str(backup_flashcards_dir)

        if not args.dry_run and moved:
            files_changed, ids_reset = clear_anki_ids_in_dir(backup_flashcards_dir)
            summary["reset_anki_id_files"] = files_changed
            summary["reset_anki_id_entries"] = ids_reset

    except Exception as exc:  # pylint: disable=broad-except
        print(json.dumps(summary, ensure_ascii=True, indent=2))
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(summary, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
