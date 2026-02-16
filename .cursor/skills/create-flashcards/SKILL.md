---
name: create-flashcards
description: >-
  Generate high-quality Anki flashcards from any content including photos of
  grammar book pages, class transcription files, free-text topic requests, or
  any study material. Follows spaced repetition best practices from SuperMemo's
  20 Rules. Cards are saved locally as Markdown in flashcards/ for review before
  syncing. Use when the user says "create flashcards", "generate cards", "make
  study cards", "I want to memorize", "help me study", "flashcards about",
  "cards from this image", "cards from this transcription", "flashcards about
  preterito perfecto", or provides any content they want to turn into study
  material. Do NOT use for syncing cards to Anki or general Anki configuration.
metadata:
  author: guilhermesilveira
  version: 3.0.0
  category: education
  tags: [flashcards, anki, spaced-repetition, memorization, study, spanish]
---

# Create Flashcards

Generate flashcards optimized for spaced repetition from any input.
Cards are saved as Markdown in `flashcards/` — never synced to Anki automatically.

There are three workflows. Pick the one that matches the input.

## Workflow A: Image of a Book Page (Direct Extraction)

Use when the user provides a photo or screenshot of a grammar book, vocabulary
list, verb table, or any structured visual content.

### Step A1: Extract Content from the Image

Read the image carefully and extract ALL visible content:
- Every verb, tense, conjugation, rule, example sentence, and note.
- Preserve the structure (tables, groupings, headers).
- Briefly confirm with the user what you see before generating cards.

### Step A2: Check for Existing Cards

Read all files in `flashcards/` to avoid duplicates.

### Step A3: Generate Cards Directly

The image already contains the exact content — no discovery phase needed.
Go straight to creating cards following `references/best-practices.md`.

Key rules for image-based content:
- One card per atomic fact (one verb-person-tense combo, one grammar rule, one example).
- For conjugation tables: one cloze card per cell, with a natural contextual sentence.
- For grammar rules: one basic card for the rule, then cloze cards for each example.
- For irregular forms: add a card contrasting the irregular vs expected regular form.
- Aim for exhaustive coverage — extract every learnable fact from the image.

### Step A4: Save and Confirm

Save to `flashcards/YYYY-MM-DD-topic-slug.md` using the file format below.
Tell the user the card count and file name.

## Workflow B: Class Transcription (Discover, Select, Generate)

Use when the user provides a transcription file of a class, lesson, or conversation
with a teacher.

### Step B1: Read and Analyze the Full Transcription

Read the entire file. Build a mental model of what was taught.

### Step B2: Discover and Present Topics

Identify every distinct topic, concept, or grammar point covered. Present them
to the user as a numbered list with brief descriptions. Example:

```
I found these topics in the transcription:

1. Pretérito indefinido — conjugation of regular -ar verbs (hablar, caminar)
2. Pretérito indefinido — irregular verbs (ir, ser, tener, hacer)
3. Vocabulary — travel (aeropuerto, equipaje, vuelo, reserva)
4. Expressions — "acabar de + infinitivo" (just did something)
5. Pronunciation — difference between b/v in Spanish

Which topics would you like flashcards for? (all, or specific numbers)
```

CRITICAL: Wait for the user to choose. Do not generate cards until they confirm.

### Step B3: Deep-Dive on Each Selected Topic

For each chosen topic:
1. Re-read the relevant sections of the transcription.
2. Extract every concrete example, conjugation, vocabulary word, and rule discussed.
3. If the transcription is incomplete (teacher only mentioned a concept briefly),
   supplement with your own knowledge to make the cards thorough and complete.
4. Generate cards following `references/best-practices.md`.

### Step B4: Save and Confirm

Save one file per topic or one combined file — user's preference.
Tell the user the card count and remind them to run `uv run python sync_anki.py`.

## Workflow C: Free Topic (Research and Generate)

Use when the user specifies a topic without providing source material.
Examples: "flashcards about pretérito perfecto", "I want to study ser vs estar",
"create cards about Spanish subjunctive", "flashcards about irregular verbs".

### Step C1: Understand the Request

Clarify scope if needed:
- "Pretérito perfecto" → all regular + irregular forms? Just the most common verbs?
- "Ser vs estar" → all use cases? Focus on the tricky ones?

If the request is clear enough (e.g. "tempos verbais do pretérito perfecto"), proceed.

### Step C2: Check for Existing Cards

Read all files in `flashcards/` to avoid duplicates.

### Step C3: Research and Structure the Content

Use your own knowledge to build comprehensive material:
1. Identify the key sub-topics (e.g. for pretérito perfecto: formation rule,
   regular conjugation, irregular participles, usage contexts, contrast with
   pretérito indefinido).
2. For each sub-topic, prepare facts, examples, and common mistakes.
3. Organize from basics → details (rule 3 of best practices).

### Step C4: Generate Cards

Create 15-30+ cards covering the topic thoroughly. Follow `references/best-practices.md`.

For language topics:
- Start with the formation rule (basic card: "How is pretérito perfecto formed?").
- Then one cloze card per verb-person combo with a contextual sentence.
- Then cards for irregular participles.
- Then usage/context cards ("When to use pretérito perfecto vs indefinido?").
- Then common mistake cards.

### Step C5: Save and Confirm

Save to `flashcards/YYYY-MM-DD-topic-slug.md`.
Tell the user the card count and file name.

## Card Best Practices (Summary)

CRITICAL: Before writing any cards, read `references/best-practices.md` for the
full rules with detailed rationale, examples, and anti-patterns.

1. **One concept per card** (atomic). Answerable in under 8 seconds.
2. **Front = one precise question.** Back = shortest possible answer.
3. **Prefer cloze deletions** for vocabulary, conjugations, and factual content.
4. **No sets or enumerations.** Never "List all X." Split into individual cards.
5. **Use context clues** — add hints in parentheses when ambiguity is possible.
6. **Build basics first**, then details.
7. **Fight interference** — if two cards could be confused, add distinguishing context.
8. **Personalize** with relevant examples.
9. **Use redundancy** — same fact from different angles (e.g. question and reverse).
10. **Exhaustive coverage** — 15-30 cards per topic. Do not under-generate.

For concrete good-vs-bad examples, consult `references/examples.md`.

## File Format

```markdown
---
topic: "Descriptive Topic Name"
created: YYYY-MM-DD
tags: [tag1, tag2]
deck: "Espanhol"
---

## Card 1
id: fc-YYYYMMDD-HHMMSS-001
anki_id:
tags: specific-tag1, specific-tag2
type: basic

**Front:** Your precise question here?

**Back:** Concise answer here.

---

## Card 2
id: fc-YYYYMMDD-HHMMSS-002
anki_id:
tags: specific-tag3
type: cloze

**Front:** Yo {{c1::hablo}} español con mis amigos.

**Back:**
```

Format rules:
- **File name**: `flashcards/YYYY-MM-DD-topic-slug.md`
- **id**: `fc-YYYYMMDD-HHMMSS-NNN` — unique, timestamp + sequence.
- **anki_id**: empty on creation. Filled by `sync_anki.py`.
- **type**: `basic` or `cloze` (use `{{c1::answer}}` syntax).
- **tags**: comma-separated per card.
- **Front/Back**: use `**Front:**` and `**Back:**` prefixes exactly.
- Cards separated by `---`.

## What NOT to Do

- Never call AnkiConnect or sync automatically.
- Never create cards for content you don't understand — ask first.
- Never put multiple concepts in one card.
- Never create cards with answers longer than ~15 words.
- Never create enumeration cards ("List all X...").
- Never generate cards from a transcription without presenting topics first.
- Never skip content visible in an image — be exhaustive.
- Never generate shallow/few cards for a free topic — be thorough.

## Troubleshooting

### Cards too complex
Cause: Multiple concepts in one card.
Solution: Split. See `references/best-practices.md` rule 4.

### Similar cards cause confusion
Cause: Interference between related facts.
Solution: Add distinguishing context. See rule 11.

### Transcription topics are vague
Cause: Teacher mentioned a concept only briefly.
Solution: Supplement with your own knowledge, but note the source as "expanded from class".

### User can't answer in 8 seconds
Cause: Answer too long or question ambiguous.
Solution: Shorten answer, sharpen question.

### Free topic cards feel generic
Cause: Cards lack contextual sentences or real-world examples.
Solution: Every conjugation card should have a natural sentence, not just "verb → form".

## Additional Resources

- Full rules with rationale, examples, and anti-patterns: `references/best-practices.md`
- Good vs bad card examples across all workflows: `references/examples.md`
