---
name: create-flashcards
description: >-
  Generate high-quality Anki flashcards from any content including photos of
  grammar book pages, class transcription files, PDF documents, free-text topic requests,
  concise topic lists, or any study material. Follows spaced repetition best practices
  from SuperMemo's 20 Rules. Cards are saved locally as Markdown in flashcards/ for review before
  syncing. Use when the user says "create flashcards", "generate cards", "make
  study cards", "I want to memorize", "help me study", "flashcards about",
  "cards from this image", "cards from this transcription", "cards from this PDF", "cards from this list",
  "flashcards about preterito perfecto", or provides any content they want to turn into study
  material. Defaults to Chilean Spanish standard (e.g. ustedes instead of vosotros) unless otherwise requested. Do NOT use for syncing cards to Anki or general Anki configuration.
metadata:
  author: guilhermesilveira
  version: 3.1.0
  category: education
  tags: [flashcards, anki, spaced-repetition, memorization, study, spanish]
---

# Create Flashcards

Generate flashcards optimized for spaced repetition from any input.
Cards are saved as Markdown in `flashcards/` — never synced to Anki automatically.

There are five workflows. Pick the one that matches the input.

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
Go straight to creating cards.

**CRITICAL: Intelligent Mode Selection (Hybrid)**
- **Default (Hybrid)**: Use your judgment to balance card count vs. retention.
  - **Use Table Mode** for: Verb conjugations (full paradigms), sets of simple related items (e.g. pronouns, days), or when the user asks for "concise" or "summary". This is the preferred default for structural content to keep card count low.
  - **Use Atomic Mode** for: Complex grammar rules that need distinct examples, specific vocabulary in context (cloze), or when deep retention of a subtle nuance is required.
  - **Mix & Match**: It is perfectly fine to create a "Table" card for the conjugation rule and then 2-3 "Atomic" cloze cards for key examples.

Key rules for image-based content:
- **Analyze the content**: Does it look like a table? Make a Table card. Is it a list of sentences? Make Atomic cards.
- If Table Mode: One card per verb/tense with the full table on the back.
- If Atomic Mode: One card per atomic fact.
- Aim for exhaustive coverage but efficient presentation.

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

### Step B3: Parallel Generation with Task Agents

For each selected topic, launch a **Task agent** (`subagent_type="generalPurpose"`) that runs independently. Up to 4 agents run in parallel (tool limit).

Each agent's prompt includes:
- The relevant excerpt or full context of the transcription for that topic.
- The full content of `references/best-practices.md` (inlined).
- The file format specification.
- The existing flashcard files list.
- Instructions to save to `flashcards/YYYY-MM-DD-topic-slug.md`.
- Instructions to deep-dive: re-read, extract examples/rules, and supplement with own knowledge if the transcription is brief.

If there are more than 4 topics, batch them in groups of 4.

### Step B4: Collect and Confirm

After all agents finish:
- Report how many cards were created per topic and total.
- List the generated file names.
- Remind the user to review and optionally sync.

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

Create cards covering the topic.

**CRITICAL: Intelligent Mode Selection (Hybrid)**
- **Default (Hybrid)**: Use your judgment.
  - **Conjugations**: Prefer **Table Mode** (one card per tense) to keep card count manageable, unless the specific verb is highly irregular and needs individual focus.
  - **Rules/Nuance**: Prefer **Atomic Mode** to ensure understanding.

For language topics (Hybrid Strategy):
- **Card 1 (Rule)**: Formation rule (Atomic or Table).
- **Card 2-4 (Tables)**: Full conjugation tables (Regular AR, ER/IR, Irregulars).
- **Card 5-7 (Context)**: Select 2-3 key examples and create Atomic Cloze cards to ensure the user can actually *use* the tense, not just recite the table.
- **Card 8 (Usage)**: When to use this tense (Atomic).

### Step C5: Save and Confirm

Save to `flashcards/YYYY-MM-DD-topic-slug.md`.
Tell the user the card count and file name.

## Workflow D: PDF Document (Extract, Discover, Parallel Generate)

Use when the user provides a PDF file (e.g. grammar exercises, textbook chapter,
article).

### Step D1: Read and Extract PDF Content (Hybrid: Text-first, Image fallback)

**Strategy**: Try text extraction first (fast, lightweight). If it fails, fall back to image-based extraction (robust, handles any PDF).

**Text-first attempt**:
- Use the Read tool on the PDF file path. Cursor's Read tool supports PDF-to-text extraction natively.
- **Quality check**: If the output contains readable Spanish text with recognizable words, headers, and structure, the extraction succeeded. Proceed with the text.
- **Failure detection**: If the output is mostly binary garbage, mojibake, or has fewer than ~50 readable words across multiple pages, the extraction failed.

**Image fallback** (when text extraction fails):
- Use Shell to convert PDF pages to PNG images via `pdftoppm` (from poppler).
- Command: `pdftoppm -png -r 200 "source_material/file.pdf" /tmp/pdf-pages/page`
- This generates one PNG per page: `page-1.png`, `page-2.png`, etc.
- Read each page image using the Read tool (which supports PNG natively).
- The AI model processes each page image visually, exactly like Workflow A.
- After extracting content from all page images, proceed to topic identification (D2).

**Note**: Inform the user which method was used ("Text extraction worked" or "Text extraction failed, processing pages as images").

### Step D2: Automatic Topic Identification

Analyze the full extracted text. Identify every distinct topic, grammar concept,
vocabulary group, or thematic section.

Present them as a numbered list with brief descriptions (same pattern as Workflow B Step B2).

**Key difference from Workflow B**: topics are identified automatically -- no "teacher said X" context.
Rely on structural cues in the PDF: headers, numbered sections, bold text, page breaks.

Example output:
```
I found these topics in the PDF:

1. Pretérito Indefinido vs Imperfecto -- choosing the correct form (exercises with answers)
2. Pretérito Indefinido vs Imperfecto -- conjugation in context (fill-in texts)
3. Translation exercises -- English to Spanish using past tenses

Which topics would you like flashcards for? (all, or specific numbers)
```

Wait for user confirmation on which topics to generate cards for.

### Step D3: Parallel Generation with Task Agents

For each selected topic, launch a **Task agent** (`subagent_type="generalPurpose"`) that runs independently. Up to 4 agents run in parallel (tool limit).

Each agent's prompt includes:
- The relevant excerpt of the PDF for that topic
- The full content of `references/best-practices.md` (inlined, not as a file reference, since agents don't share context)
- The file format specification (from SKILL.md)
- The existing flashcard files list (to avoid duplicates)
- Instructions to save to `flashcards/YYYY-MM-DD-topic-slug.md`

If there are more than 4 topics, batch them in groups of 4.

### Step D4: Collect and Confirm

After all agents finish:
- Report how many cards were created per topic and total.
- List the generated file names.
- Remind the user to review and optionally sync.

## Workflow E: Topic List (Concise Notes)

Use when the user provides a text file containing concise, unformatted phrases or topic names separated by underscores (e.g. `_______`). This often represents raw notes from a class where only the topic name was jotted down.

### Step E1: Read and Parse the File

1. Read the provided text file.
2. Split the content by the separator (usually a line of underscores like `____` or `-------`).
3. Treat each separated block as a distinct topic request.

### Step E2: Parallel Generation with Task Agents

For each block/topic found in the file, launch a **Task agent** (`subagent_type="generalPurpose"`) that runs independently. Up to 4 agents run in parallel.

Each agent's prompt includes:
- The concise topic name (e.g. "Pretérito Indefinido").
- The instruction to treat this as a **Free Topic (Workflow C)**: research and supply all content based on the name.
- The full content of `references/best-practices.md` (inlined).
- The file format specification.
- Instructions to save to `flashcards/YYYY-MM-DD-topic-slug.md`.

If there are more than 4 topics, batch them in groups of 4.

### Step E3: Collect and Confirm

After all agents finish:
- Report the list of created files to the user.
- Remind the user to review and sync.

## Card Best Practices (Summary)

CRITICAL: Before writing any cards, read `references/best-practices.md`.

**User Preference Override**: The user prefers an **Intelligent Hybrid** approach.
- **Bias towards Tables** for conjugations and lists to keep card count low.
- **Bias towards Atomic** for complex rules and usage examples.
- Do not force one or the other; use what best fits the specific content.

1. **Intelligent Mode** — Choose Table vs Atomic based on content type.
2. **Front = one precise question.** Back = answer (concise or table).
3. **Prefer cloze deletions** for vocabulary in context.
4. **Use sets/tables** — *When appropriate for conjugations or groups*.
5. **Use context clues**.
6. **Build basics first**, then details.
7. **Fight interference**.
8. **Personalize**.
9. **Use redundancy**.
10. **Exhaustive coverage**.
11. **Chilean Spanish Standard** — Always use Chilean Spanish by default.

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
- **Cards separated by** `---`.

## What NOT to Do

- Never call AnkiConnect or sync automatically.
- Never use 'vosotros' or Peninsular Spanish forms unless explicitly requested. Default to Chilean Spanish.
- Never create cards for content you don't understand — ask first.
- Never put multiple concepts in one card (UNLESS it is a Table card or necessary for context).
- Never create cards with answers longer than ~15 words (UNLESS it is a Table card).
- Never generate cards from a transcription without presenting topics first.
- Never skip content visible in an image — be exhaustive.
- Never generate shallow/few cards for a free topic — be thorough.
- Never process all topics from a PDF, Transcription, or List sequentially if parallel agents are available.

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

### PDF text extraction returns garbled content
Cause: PDF is scanned or uses non-standard encoding.
Solution: Automatically fall back to image-based extraction via `pdftoppm`. If `pdftoppm` is not installed, inform the user to run `brew install poppler` and retry.

## Additional Resources

- Full rules with rationale, examples, and anti-patterns: `references/best-practices.md`
- Good vs bad card examples across all workflows: `references/examples.md`
