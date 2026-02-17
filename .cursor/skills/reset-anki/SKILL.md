---
name: reset-anki
description: Delete all notes from Anki and reset local flashcard sync state by moving flashcards/ to backup and clearing anki_id values. Use when the user asks to reset Anki, wipe cards, start from zero, clear flashcards, or reset anki_id after deleting cards in Anki.
metadata:
  author: guilhermesilveira
  version: 1.0.0
  category: education
  tags: [anki, reset, cleanup, backup, ankiconnect]
---

# Reset Anki

Reset Anki and local sync state safely.

This skill does:

1. Delete all notes in Anki (via AnkiConnect), unless skipped.
2. Move `flashcards/` to a timestamped folder under `backup/`.
3. Recreate an empty `flashcards/`.
4. Set `anki_id:` (empty) in all markdown files inside the moved backup.

Use this before starting a new import cycle from scratch.

## Preconditions

1. Confirm the user wants a destructive reset.
2. If deleting from Anki, Anki Desktop must be open with AnkiConnect enabled.
3. If the user already deleted cards in Anki, use `--skip-anki-cleanup`.

## Workflow

Run from repository root.

### Step 1: Preview

```bash
uv run python .cursor/skills/reset-anki/scripts/reset_anki_state.py --dry-run --skip-anki-cleanup
```

If user also wants deletion in Anki:

```bash
uv run python .cursor/skills/reset-anki/scripts/reset_anki_state.py --dry-run
```

### Step 2: Execute

If cards were already deleted in Anki:

```bash
uv run python .cursor/skills/reset-anki/scripts/reset_anki_state.py --yes --skip-anki-cleanup
```

If cards should also be deleted in Anki now:

```bash
uv run python .cursor/skills/reset-anki/scripts/reset_anki_state.py --yes
```

## Output and Validation

The script prints a JSON summary with:

- `deleted_notes_count`: notes removed from Anki.
- `moved_flashcards`: whether `flashcards/` was archived.
- `backup_flashcards_path`: exact backup folder path.
- `reset_anki_id_entries`: number of `anki_id` fields cleared.

After execution, validate:

1. `flashcards/` exists and is empty.
2. Backup folder exists under `backup/anki-reset-<timestamp>/flashcards`.
3. Backup markdown files have `anki_id:` (empty value).

## Command Reference

```bash
# Custom project root
uv run python .cursor/skills/reset-anki/scripts/reset_anki_state.py --project-root /path/to/repo --yes --skip-anki-cleanup

# Custom backup directory (inside project root)
uv run python .cursor/skills/reset-anki/scripts/reset_anki_state.py --backup-dir my-backups --yes --skip-anki-cleanup
```

## Scope Boundaries

- This skill is for full reset only.
- This skill does not generate new cards.
- After reset, use `create-flashcards` to generate cards again and `sync-ankiweb` to reimport.
