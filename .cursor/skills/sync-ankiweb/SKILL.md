---
name: sync-ankiweb
description: Sync locally generated flashcard Markdown files to Anki and then to AnkiWeb using the project's sync_anki.py workflow. Use when the user asks to sync flashcards, send cards to Anki/AnkiWeb, publish generated cards, run AnkiConnect sync, or avoid duplicate imports.
metadata:
  author: guilhermesilveira
  version: 1.0.0
  category: education
  tags: [anki, ankiweb, sync, flashcards, ankiconnect]
---

# Sync AnkiWeb

Sync flashcards from `flashcards/*.md` into Anki Desktop and then to AnkiWeb.

Use this skill after cards were created by `create-flashcards` and reviewed.

## Preconditions

Before running sync:

1. Confirm `flashcards/` has at least one `.md` file.
2. Confirm Anki Desktop is open.
3. Confirm AnkiConnect add-on is enabled (`2055492159`).
4. Prefer running a preview first (`--dry-run`).

If Anki Desktop is closed or AnkiConnect is unavailable, stop and tell the user what to fix.

## Sync Workflow

Follow this exact order:

1. Preview:

```bash
uv run python sync_anki.py --dry-run
```

2. If preview looks correct, run real sync:

```bash
uv run python sync_anki.py
```

3. Verify outcome in terminal summary (`synced`, `skipped`, `errors`).
4. If `errors > 0`, report the failing card IDs and error messages.
5. Ask the user to click **Sync** in Anki Desktop to send data to AnkiWeb.

## Expected Behavior

- New cards get sent to Anki through AnkiConnect.
- `anki_id` is written back to each synced card in its Markdown file.
- Re-running sync should skip cards that already have `anki_id` (no duplicates).

## Command Reference

```bash
# Preview only (no writes to Anki, no file updates)
uv run python sync_anki.py --dry-run

# Real sync
uv run python sync_anki.py

# Sync from another folder of markdown cards
uv run python sync_anki.py --dir path/to/flashcards
```

## Troubleshooting

### Cannot connect to AnkiConnect

Symptoms: message about `http://127.0.0.1:8765`.

Actions:
- Open Anki Desktop.
- Check AnkiConnect add-on is installed and enabled.
- Restart Anki Desktop and retry.

### Cards imported but not on AnkiWeb

Cause: local import succeeded, cloud sync not triggered.

Action: click **Sync** in Anki Desktop and confirm AnkiWeb credentials/session.

### Unexpected duplicates

Checks:
- Confirm cards already synced contain `anki_id` in the markdown.
- Avoid manually removing `anki_id` from previously synced cards.
- Keep stable card `id` values between edits.

## Scope Boundaries

- This skill only syncs cards and validates sync results.
- This skill does not create new flashcards; use `create-flashcards` for generation.
- This skill does not configure Anki decks/models globally unless the user asks.
