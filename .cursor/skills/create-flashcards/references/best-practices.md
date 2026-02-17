# Flashcard Best Practices — Complete Reference

Based on Dr. Piotr Wozniak's "20 Rules of Formulating Knowledge" (SuperMemo),
Anki community consensus, and cognitive science research on memory.

This is the authoritative reference for card quality. Read it fully before
generating any flashcards.

---

## Part 1: The 20 Rules of Formulating Knowledge

### Rule 1: Do Not Learn What You Don't Understand

**Rationale**: Memorizing incomprehensible material produces near-zero retention
and wastes enormous time. The brain cannot form meaningful associations with
things it doesn't understand.

**What this means for card generation**:
- If you receive an image or text with unfamiliar concepts, ASK the user before
  creating cards.
- If a grammar rule seems ambiguous in context, research it or confirm with the user.
- Never assume: "the user probably knows what this means."

**Anti-pattern**:
```
Front: ¿Qué es el aspecto perfectivo?
Back: Es el aspecto que presenta la acción como terminada.
```
This card is useless if the user doesn't understand what "aspecto verbal" means
in linguistics. First create a card explaining what "aspecto verbal" is.

### Rule 2: Understand Before You Memorize (Big Picture First)

**Rationale**: Isolated facts without a framework are like scattered puzzle pieces.
The brain needs a structure to attach individual memories to.

**What this means for card generation**:
- When generating cards for a grammar topic (e.g. pretérito perfecto), ALWAYS
  start with 1-2 "big picture" cards before diving into conjugations.
- The first cards should answer: "What is this?", "When is it used?", "How is it
  formed?"

**Good sequence** (pretérito perfecto):
1. Card: "What is pretérito perfecto compuesto used for?" → Actions connected to the present.
2. Card: "How is pretérito perfecto formed?" → haber (presente) + participio pasado.
3. Card: "What is the participio pasado of -ar verbs?" → -ado (hablado).
4. THEN: individual conjugation cards.

**Bad sequence**: Jumping straight to "Yo he ___" cloze cards without context.

### Rule 3: Build Upon Basics

**Rationale**: Simple foundational concepts are easy to retain, take minimal
review time (3-5% of total material ≈ 50% of review effort), and make everything
else easier to learn. Skipping basics means building on sand.

**What this means for card generation**:
- Regular verbs before irregular verbs.
- Present tense before past tenses.
- Common verbs (ser, estar, tener, ir, hacer) before uncommon ones.
- Formation rules before exceptions.
- If generating cards for "pretérito indefinido de verbos irregulares", first
  include a card about the regular pattern so the user sees what's "normal"
  before learning what's different.

**Practical ordering for a verb tense topic**:
1. What is this tense? When to use it?
2. How to form it (regular -ar, -er, -ir).
3. Regular verb examples (high frequency: hablar, comer, vivir).
4. Irregular patterns (stem changes, completely irregular).
5. Confusing pairs (pretérito vs imperfecto, perfecto vs indefinido).

### Rule 4: Minimum Information Principle (THE MOST CRITICAL RULE)

**Rationale**: This is the single rule that most determines card quality.

The brain processes simple items identically each time → strong, consistent
memory traces. Complex items activate different neural pathways on different
reviews → weak, unstable memory.

Simple items also schedule better in spaced repetition. A card with 5 facts
means you review at the pace of the hardest fact, wasting time on the 4 you
already know.

**The test**: Can the user read the front, recall the answer, and confirm it
in under 8 seconds? If not, the card is too complex.

**Anti-pattern — too much in one card**:
```
Front: Conjugate "tener" in pretérito indefinido.
Back: tuve, tuviste, tuvo, tuvimos, tuvisteis, tuvieron
```
This is an enumeration (6 answers). The user will fail repeatedly because
forgetting any ONE of the six means failing the entire card.

**Correct approach** — one card per person:
```
Front: Yo {{c1::tuve}} un sueño muy raro anoche. (tener, pret. indefinido)
```
Six separate cards, one per pronoun, each with a contextual sentence.

**Anti-pattern — compound question**:
```
Front: What's the difference between ser and estar?
Back: Ser is for permanent characteristics, estar is for temporary states and locations.
```
This is two concepts. Split into:
```
Card 1 — Front: When do you use "ser" instead of "estar"?
         Back: For permanent/inherent characteristics (nationality, profession, identity).
Card 2 — Front: When do you use "estar" instead of "ser"?
         Back: For temporary states, emotions, locations, and conditions.
Card 3 — Front: "Soy aburrido" vs "Estoy aburrido" — what's the difference?
         Back: "Soy aburrido" = I'm a boring person. "Estoy aburrido" = I'm bored right now.
```

### Rule 5: Cloze Deletion Is Easy and Effective

**Rationale**: Cloze deletion (fill-in-the-blank) provides context around the
answer, making recall easier and more natural. It's faster to create than
question-answer pairs and has strong mnemonic power.

**When to use cloze**:
- Verb conjugations (always prefer cloze for these)
- Vocabulary in context
- Grammar rules with fill-in examples
- Definitions where the term appears in a sentence
- Any factual statement where one piece is the "answer"

**When to use basic (Q&A) instead**:
- "Why" questions (understanding, not recall)
- Conceptual questions ("When do you use subjunctive?")
- Comparison questions ("What's the difference between X and Y?")
- Questions where the answer isn't a single word/phrase

**Cloze best practices**:
- The sentence must be natural and contextual, not artificially constructed.
- Add a hint in parentheses if the cloze could have multiple valid answers.
- Use only one cloze per card for language learning (not multiple `{{c1::}} {{c2::}}`).

**Good cloze**:
```
Front: Ayer yo {{c1::estuve}} en la biblioteca estudiando. (estar, pret. indefinido)
```

**Bad cloze** (artificial sentence):
```
Front: Estar, yo, pretérito indefinido: {{c1::estuve}}.
```

**Bad cloze** (ambiguous without hint):
```
Front: Yo {{c1::estuve}} en la biblioteca.
```
Could be "estuve", "estaba", "estaré" — needs a tense hint.

### Rule 6: Use Imagery

**Rationale**: The visual cortex processes and retains information far more
effectively than verbal processing. One image can encode details that would
take many words to describe.

**What this means for card generation**:
- When generating from an image (Workflow A), reference the visual structure
  in the card if helpful.
- For geography, anatomy, diagrams: suggest the user add the image to the card.
- For abstract concepts: suggest a mental image or analogy.

**Example**: Instead of "Spain is in southwestern Europe", a card with a map
showing Spain highlighted is far more memorable.

### Rule 7: Use Mnemonic Techniques

**Rationale**: For 1-5% of stubborn items, mnemonics make the difference
between remembering and forgetting. They create artificial but strong
memory hooks.

**When to suggest mnemonics**:
- Irregular forms that don't follow any pattern.
- Confusing similar words (e.g. "hecho" vs "echo").
- Lists that must be memorized in order.

**Example for Spanish**:
```
Front: Mnemonic: What are the 7 "go" verbs in Spanish? (yo form ends in -go)
Back: "Silly People Don't Sing Very Horribly Today"
      — Salir, Poner, Decir, Suponer, Venir, Hacer, Tener
```

### Rule 8: Graphic Deletion (Occlusion)

**Rationale**: Like cloze deletion but for images. Hide part of an image and
ask "what goes here?" One diagram/table image can generate 10-20 cards.

**When applicable**:
- Conjugation tables: occlude one cell at a time.
- Maps: "What country/region is hidden?"
- Diagrams: "What label goes here?"

Since Anki supports image occlusion natively, suggest the user create these
directly in Anki when images are involved.

### Rule 9: Avoid Sets

**Rationale**: "Name all X" cards are nearly impossible to memorize because
the brain can retrieve the items in any order, creating chaotic neural pathways.
Forgetting one item means failing the whole card.

**Anti-pattern**:
```
Front: What are the irregular participles in Spanish?
Back: abierto, dicho, escrito, hecho, muerto, puesto, resuelto, roto, visto, vuelto
```

**Correct approach** — individual cards:
```
Card 1 — Front: ¿Cuál es el participio pasado irregular de "abrir"?
         Back: abierto (not *abrido)
Card 2 — Front: ¿Cuál es el participio pasado irregular de "decir"?
         Back: dicho (not *decido)
...etc for each verb
```

You may also add a "grouping" card to tie them together:
```
Front: Irregular past participles often end in which two patterns?
Back: -to (abierto, muerto, puesto, escrito, roto, visto, vuelto) and -cho (dicho, hecho).
```

### Rule 10: Avoid Enumerations

**Rationale**: Even ordered lists are hard because forgetting any link in the
chain means failing everything after it.

**When enumerations are unavoidable** — use overlapping cloze deletions:
```
Card 1: a, b, {{c1::c}}, d, e
Card 2: b, c, {{c1::d}}, e, f
Card 3: c, d, {{c1::e}}, f, g
```
This creates redundancy where each item is reinforced from multiple positions.

**For verb conjugation "tables"**: Don't create one card asking for the full
paradigm. Create one card per pronoun. The "enumeration" emerges naturally
from individual cards.

### Rule 11: Combat Interference

**Rationale**: Interference is the #1 cause of forgetting in mature collections.
Similar items confuse each other. You may know both "hecho" and "echo" perfectly
separately, but when both are in your deck, you constantly mix them up.

**Detection**: If you're generating cards for two similar concepts (e.g. pretérito
perfecto vs pretérito indefinido), interference is almost guaranteed.

**Prevention strategies**:
1. **Add distinguishing context** to the front of each card:
   ```
   Front: He {{c1::hablado}} con ella esta mañana. (pret. perfecto, "this morning" = connected to present)
   Front: {{c1::Hablé}} con ella ayer. (pret. indefinido, "yesterday" = finished, disconnected)
   ```
2. **Create explicit contrast cards**:
   ```
   Front: "He ido al cine" vs "Fui al cine" — which tense is each?
   Back: "He ido" = pretérito perfecto (connected to present). "Fui" = pretérito indefinido (finished past).
   ```
3. **Reference the confusing sibling**:
   ```
   Front: ¿Participio pasado de "hacer"? (not "echo", which means "I throw")
   Back: hecho
   ```

### Rule 12: Optimize Wording

**Rationale**: Every unnecessary word slows down review and introduces ambiguity.
The front of a card should trigger the right memory instantly.

**Guidelines**:
- Front should be as short as possible while remaining unambiguous.
- Back should be as short as possible — ideally 1-5 words.
- Remove filler words: "Can you tell me...", "Do you know...", "What is it that...".
- Use parenthetical hints only when needed for disambiguation.

**Bad**:
```
Front: In the Spanish language, when you want to express an action that happened
       in the past and is connected to the present moment, which verb tense do
       you use?
Back: Pretérito perfecto compuesto
```

**Good**:
```
Front: Which Spanish past tense expresses actions connected to the present?
Back: Pretérito perfecto compuesto.
```

### Rule 13: Refer to Other Memories

**Rationale**: New knowledge anchored to existing knowledge is retained far
better. Cross-references reduce interference and build a network of associations.

**How to apply**:
```
Front: Unlike "ser" (permanent), "estar" is used for...?
Back: Temporary states, emotions, locations, and conditions.
```
The reference to "ser" activates existing knowledge, making the distinction
stick better.

For verb tenses:
```
Front: Unlike pretérito indefinido (completed, disconnected past), pretérito
       perfecto is used for...?
Back: Past actions connected to the present moment.
```

### Rule 14: Personalize and Use Concrete Examples

**Rationale**: Abstract facts are hard to memorize. Facts connected to personal
experience, vivid imagery, or real situations are retained far better.

**How to apply to language cards**:
- Use natural, believable sentences — not textbook filler.
- Sentences should describe situations the user might actually encounter.
- Vary the contexts: travel, food, daily routines, conversations.

**Bad** (abstract/textbook):
```
Front: Ella {{c1::ha comido}} la manzana. (comer, pret. perfecto)
```

**Good** (vivid, relatable):
```
Front: Ya {{c1::he comido}} demasiado en la cena de Navidad. (comer, pret. perfecto)
```

### Rule 15: Use Redundancy Wisely

**Rationale**: Approaching the same fact from different angles strengthens memory
without bloating any single card. This is NOT the same as having duplicate cards.

**Good redundancy patterns**:
- Forward + reverse: "Capital of France?" + "Paris is the capital of?"
- Recall + recognition: "Conjugate tener, yo, pret. perfecto" + "He tenido means?"
- Production + comprehension: "How do you say 'I have eaten'?" + "¿Qué significa 'he comido'?"

**For language learning**, always create at least two angles:
1. Production cloze: `Yo {{c1::he tenido}} mucha suerte. (tener, pret. perfecto)`
2. Comprehension: `What does "He tenido mucha suerte" mean? → I have been very lucky.`

### Rule 16: Provide Sources

When generating cards from a transcription or book, add a note about the source
in the file's frontmatter `tags` field. This helps the user trust and revisit the
material later.

### Rule 17: Provide Date Stamps

For time-sensitive facts (current population, political facts, etc.), note the
date. Grammar rules don't need this, but vocabulary related to current events does.

### Rule 18: Prioritize

**Rationale**: Not everything is worth memorizing. The user's time is limited.
Focus on high-value, high-frequency knowledge.

**For language learning**:
- Prioritize the 100 most common verbs over rare ones.
- Prioritize tricky irregulars over easy regulars (the user won't forget "hablado").
- Prioritize usage distinctions (ser/estar, por/para) over simple vocabulary.
- Ask: "Will this card still be useful in 6 months?"

### Rule 19: Card Independence

**Rationale**: Each card must make complete sense on its own. During review,
cards appear in random order. A card that says "See Card 3" is useless.

**Anti-pattern**:
```
Card 3 — Front: And the third irregular participle is...?
```
This is meaningless without Card 1 and 2.

**Every card must be fully self-contained.** Include the verb name, the tense,
and any context needed to answer correctly.

### Rule 20: Emotional Connection

**Rationale**: Emotionally charged memories are retained better. Surprise, humor,
curiosity, and personal relevance all improve retention.

**How to apply**:
- Use funny or surprising example sentences.
- Highlight interesting exceptions ("Why does 'ir' in pretérito indefinido use
  the same forms as 'ser'? Nobody knows for sure!").
- Frame questions that provoke curiosity.

### Rule 21: Language Variety (Chilean Spanish Standard)

**Rationale**: To maintain consistency and relevance for the user, stick to one Spanish variety. The user specifically requests Chilean Spanish as the standard.

**What this means for card generation**:
- **Pronouns**: Always use "ustedes" instead of "vosotros".
- **Vocabulary**: Prefer Chilean terms (e.g., "auto" instead of "coche", "celular" instead of "móvil", "computador" instead of "ordenador") when applicable.
- **Grammar**: Be aware of voseo (used in Chile but often informal/verbal), but stick to standard Latin American forms for general cards unless colloquial Chilean is requested.
- **Pronunciation**: If adding audio notes or phonetic descriptions, reference Chilean pronunciation (seseo, aspiration of 's').

**Anti-pattern (Peninsular Spanish)**:
```
Front: Vosotros sois mis amigos.
```

**Correct approach (Chilean/LatAm Standard)**:
```
Front: Ustedes son mis amigos.
```

---

## Part 2: Card Design Patterns

### Pattern A: Conjugation Cards (The Core Pattern)

For any verb tense, generate cards in this structure:

**Layer 1 — Concept card (basic)**:
```
Front: ¿Para qué se usa el pretérito perfecto compuesto?
Back: Para acciones pasadas conectadas al presente (hoy, esta semana, ya, todavía no).
```

**Layer 2 — Formation card (basic)**:
```
Front: ¿Cómo se forma el pretérito perfecto compuesto?
Back: Presente de "haber" + participio pasado (-ado/-ido).
```

**Layer 3 — Auxiliary verb cards (cloze, one per pronoun)**:
```
Front: Yo {{c1::he}} viajado mucho este año. (haber, pret. perfecto)
Front: Tú {{c1::has}} aprendido rápido. (haber, pret. perfecto)
Front: Él {{c1::ha}} llegado tarde. (haber, pret. perfecto)
Front: Nosotros {{c1::hemos}} trabajado mucho. (haber, pret. perfecto)
Front: Vosotros {{c1::habéis}} comido ya. (haber, pret. perfecto)
Front: Ellos {{c1::han}} salido de casa. (haber, pret. perfecto)
```

**Layer 4 — Participle cards (cloze, one per verb)**:
```
Front: Este año he {{c1::viajado}} a tres países. (viajar, participio)
Front: ¿Has {{c1::comido}} ya? (comer, participio)
Front: Nunca he {{c1::vivido}} en el extranjero. (vivir, participio)
```

**Layer 5 — Irregular participle cards (basic + cloze)**:
```
Front: ¿Cuál es el participio irregular de "escribir"? (not *escribido)
Back: escrito

Front: He {{c1::escrito}} tres cartas hoy. (escribir, participio irregular)
```

**Layer 6 — Usage contrast cards (basic)**:
```
Front: "He viajado mucho" vs "Viajé mucho" — when to use each?
Back: "He viajado" (pret. perfecto) = connected to present / no specific time.
      "Viajé" (pret. indefinido) = specific finished event in the past.
```

### Pattern B: Vocabulary Cards

**Cloze in context** (preferred):
```
Front: Necesito hacer la {{c1::maleta}} antes del vuelo. (suitcase)
```

**Basic with reverse** (for critical words):
```
Card 1 — Front: ¿Cómo se dice "suitcase" en español?    Back: maleta
Card 2 — Front: ¿Qué significa "maleta" en inglés?       Back: suitcase
```

**Never** create vocabulary lists:
```
Front: Translate: airport, suitcase, flight, boarding pass
Back: aeropuerto, maleta, vuelo, tarjeta de embarque
```

### Pattern C: Grammar Rule Cards

**Structure**: Rule card + Example cards + Exception cards + Contrast cards.

**Example — "acabar de + infinitivo"**:
```
Card 1 (rule):
Front: What does "acabar de + infinitivo" express?
Back: An action that just happened (very recent past).

Card 2 (example cloze):
Front: {{c1::Acabo de}} llegar a casa. (I just arrived)

Card 3 (example cloze):
Front: Ella {{c1::acaba de}} terminar el examen. (She just finished)

Card 4 (negative):
Front: How do you say "I haven't just eaten" using acabar de?
Back: No acabo de comer.

Card 5 (contrast):
Front: "Acabo de comer" vs "He comido" — difference?
Back: "Acabo de comer" = I JUST ate (seconds/minutes ago).
      "He comido" = I have eaten (anytime today, connected to present).
```

### Pattern D: Contrast/Confusion Cards

Use whenever two concepts are frequently confused.

**Structure**: Always create BOTH directions + an explicit comparison.

```
Card 1 — Front: "Soy cansado" — is this correct?
         Back: No. "Estoy cansado" (tired is temporary). "Soy cansado" would mean "I'm a tiring person."

Card 2 — Front: "Estoy médico" — is this correct?
         Back: No. "Soy médico" (profession is permanent/inherent).

Card 3 — Front: Ser vs estar — which for "tired"?
         Back: ESTAR cansado (temporary state).

Card 4 — Front: Ser vs estar — which for professions?
         Back: SER médico/profesor/abogado (inherent characteristic).
```

### Pattern E: Table Cards (User Preference / Concise Mode)

**Rationale**: While standard best practices (Rule 4) discourage large sets, some advanced learners prefer to memorize full paradigms at once to see the "big picture" and reduce card count.

**When to use**: ONLY when the user explicitly asks for "tables", "concise cards", "less cards", or "full conjugations".

**Structure**:
- Front: "Conjugate [Verb] in [Tense]" or "Table of [Topic]".
- Back: The full table, formatted clearly.

**Example**:
```
Front: Conjugate "Tener" in Pretérito Indefinido (Full Table).
Back:
| Person | Form |
|---|---|
| Yo | tuve |
| Tú | tuviste |
| Él/Ella/Ud. | tuvo |
| Nosotros | tuvimos |
| Vosotros | tuvisteis |
| Ellos/Uds. | tuvieron |
```

**Hybrid Approach (Recommended for Tables)**:
Even in Table Mode, add *one* example sentence below the table to ground it in reality.

```
Front: Conjugate "Ser" in Pretérito Imperfecto.
Back:
| Yo | era |
| Tú | eras |
| Él | era |
| Nosotros | éramos |
| Vosotros | erais |
| Ellos | eran |

Example: "Cuando yo era niño, vivía en Madrid."
```

---

## Part 3: Language Learning Specifics

### Contextual Sentences Are Mandatory

Every conjugation cloze card MUST have a natural, complete sentence — never
just the isolated verb form. The sentence provides:
- Context to disambiguate the answer (tense hint, temporal markers).
- A usage example the user unconsciously absorbs.
- An emotional/vivid anchor for memory.

**Mandatory**: `Ayer {{c1::fui}} al supermercado. (ir, pret. indefinido)`
**Forbidden**: `ir, yo, pret. indefinido → {{c1::fui}}`

### Temporal Markers as Context Clues

For past tenses, always include temporal markers in the sentence to help the
user identify the correct tense:

| Tense | Markers | Example sentence |
|-------|---------|------------------|
| Pretérito perfecto | hoy, esta semana, ya, todavía no, este año | Hoy he comido paella. |
| Pretérito indefinido | ayer, anoche, la semana pasada, en 2020 | Ayer comí paella. |
| Pretérito imperfecto | siempre, todos los días, cuando era niño | De niño comía paella los domingos. |

### Irregular Verb Strategy

1. **Always contrast** with the expected regular form:
   ```
   Front: Yo {{c1::tuve}} que estudiar mucho. (tener, pret. indefinido — irregular: not *tení)
   ```
2. **Group irregulars** by pattern:
   - "-go" verbs in present: tener→tengo, venir→vengo, salir→salgo, etc.
   - Stem-changing: e→ie (querer→quiero), o→ue (poder→puedo), e→i (pedir→pido).
   - Completely irregular: ir/ser (fui), dar (di), saber (supe).
3. **Create a "pattern" card** for each irregular group:
   ```
   Front: What do tener, venir, poner, salir, and hacer have in common in "yo" present?
   Back: They all end in -go (tengo, vengo, pongo, salgo, hago).
   ```

### Common Pitfalls to Avoid

1. **Don't put translations on the front.** "Translate 'I went'" tests English
   reading, not Spanish recall. Instead use a cloze in a Spanish sentence.

2. **Don't combine tenses.** "Conjugate hablar in present and past" → too many
   answers. Separate files/sections per tense.

3. **Don't ask "Conjugate X in Y".** "Conjugate ir in pretérito indefinido" has
   6 answers. One card per pronoun.

4. **Don't skip the auxiliary.** For pretérito perfecto, create separate cards
   for the auxiliary "haber" conjugation AND for the participle. Don't only test
   the combined form.

5. **Don't create bilingual cards by default.** Create Spanish-only cloze cards.
   Only add translation cards when the user specifically asks for them.

6. **Don't forget common mistake cards.** If students often confuse something,
   make a card about it:
   ```
   Front: Common mistake — "Yo soy 25 años." Is this correct?
   Back: No. "Yo tengo 25 años." (In Spanish, you "have" years, not "are" years.)
   ```

---

## Part 4: Quality Checklist

Before saving any flashcard file, verify every card against this checklist:

- [ ] Each card tests exactly ONE concept.
- [ ] Every answer is under 15 words (ideally under 8).
- [ ] Every conjugation card has a natural contextual sentence.
- [ ] Cloze cards include a hint in parentheses (verb, tense) when needed.
- [ ] No card asks "List all X" or "Conjugate X in Y" (enumeration).
- [ ] Similar/confusable cards have distinguishing context.
- [ ] Cards are ordered from basics → details.
- [ ] Irregular forms are contrasted with the expected regular form.
- [ ] Tags are specific and granular (verb name, tense, pronoun).
- [ ] The first 2-3 cards provide "big picture" context for the topic.
