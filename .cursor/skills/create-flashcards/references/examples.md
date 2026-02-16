# Flashcard Examples — Complete Reference

Concrete examples for every workflow and card type.
Each example shows BAD vs GOOD to make the quality difference clear.

---

## Example 1: Free Topic — Pretérito Perfecto Compuesto (Workflow C)

User says: "Create flashcards about pretérito perfecto compuesto."

### Bad: Shallow, few cards, no structure

```markdown
---
topic: "Pretérito Perfecto"
created: 2026-02-16
tags: [spanish, preterito-perfecto]
deck: "Espanhol"
---

## Card 1
id: fc-20260216-100000-001
anki_id:
tags: spanish, preterito-perfecto
type: basic

**Front:** How is pretérito perfecto formed?

**Back:** haber + participio pasado

---

## Card 2
id: fc-20260216-100000-002
anki_id:
tags: spanish, preterito-perfecto
type: basic

**Front:** Conjugate haber in present tense.

**Back:** he, has, ha, hemos, habéis, han
```

Problems: Only 2 cards. Card 2 is an enumeration (6 answers!). No cloze, no
contextual sentences, no irregulars, no usage contrast.

### Good: Thorough, layered, follows all best practices

```markdown
---
topic: "Pretérito Perfecto Compuesto"
created: 2026-02-16
tags: [spanish, preterito-perfecto, verb-tense]
deck: "Espanhol"
---

## Card 1
id: fc-20260216-100000-001
anki_id:
tags: preterito-perfecto, concept
type: basic

**Front:** ¿Para qué se usa el pretérito perfecto compuesto en español?

**Back:** Para acciones pasadas conectadas al presente (hoy, esta semana, ya, todavía no).

---

## Card 2
id: fc-20260216-100000-002
anki_id:
tags: preterito-perfecto, formation
type: basic

**Front:** ¿Cómo se forma el pretérito perfecto compuesto?

**Back:** Presente de "haber" + participio pasado (-ado / -ido).

---

## Card 3
id: fc-20260216-100000-003
anki_id:
tags: preterito-perfecto, haber, yo
type: cloze

**Front:** Yo {{c1::he}} viajado mucho este año. (haber, presente)

**Back:**

---

## Card 4
id: fc-20260216-100000-004
anki_id:
tags: preterito-perfecto, haber, tu
type: cloze

**Front:** Tú {{c1::has}} aprendido muy rápido. (haber, presente)

**Back:**

---

## Card 5
id: fc-20260216-100000-005
anki_id:
tags: preterito-perfecto, haber, el-ella
type: cloze

**Front:** Ella {{c1::ha}} llegado tarde a la reunión. (haber, presente)

**Back:**

---

## Card 6
id: fc-20260216-100000-006
anki_id:
tags: preterito-perfecto, haber, nosotros
type: cloze

**Front:** Nosotros {{c1::hemos}} trabajado mucho esta semana. (haber, presente)

**Back:**

---

## Card 7
id: fc-20260216-100000-007
anki_id:
tags: preterito-perfecto, haber, vosotros
type: cloze

**Front:** Vosotros {{c1::habéis}} comido demasiado. (haber, presente)

**Back:**

---

## Card 8
id: fc-20260216-100000-008
anki_id:
tags: preterito-perfecto, haber, ellos
type: cloze

**Front:** Ellos {{c1::han}} salido de casa hace un rato. (haber, presente)

**Back:**

---

## Card 9
id: fc-20260216-100000-009
anki_id:
tags: preterito-perfecto, participio, regular-ar
type: basic

**Front:** ¿Cómo se forma el participio pasado de verbos regulares -ar?

**Back:** raíz + -ado (hablar → hablado).

---

## Card 10
id: fc-20260216-100000-010
anki_id:
tags: preterito-perfecto, participio, regular-er-ir
type: basic

**Front:** ¿Cómo se forma el participio pasado de verbos regulares -er / -ir?

**Back:** raíz + -ido (comer → comido, vivir → vivido).

---

## Card 11
id: fc-20260216-100000-011
anki_id:
tags: preterito-perfecto, participio, hablar
type: cloze

**Front:** Esta mañana he {{c1::hablado}} con mi madre por teléfono. (hablar, participio)

**Back:**

---

## Card 12
id: fc-20260216-100000-012
anki_id:
tags: preterito-perfecto, participio, comer
type: cloze

**Front:** ¿Ya has {{c1::comido}}? Tengo hambre. (comer, participio)

**Back:**

---

## Card 13
id: fc-20260216-100000-013
anki_id:
tags: preterito-perfecto, participio, vivir
type: cloze

**Front:** Nunca he {{c1::vivido}} en otro país. (vivir, participio)

**Back:**

---

## Card 14
id: fc-20260216-100000-014
anki_id:
tags: preterito-perfecto, participio-irregular, escribir
type: basic

**Front:** ¿Cuál es el participio irregular de "escribir"? (not *escribido)

**Back:** escrito

---

## Card 15
id: fc-20260216-100000-015
anki_id:
tags: preterito-perfecto, participio-irregular, hacer
type: basic

**Front:** ¿Cuál es el participio irregular de "hacer"? (not *hacido)

**Back:** hecho

---

## Card 16
id: fc-20260216-100000-016
anki_id:
tags: preterito-perfecto, participio-irregular, abrir
type: basic

**Front:** ¿Cuál es el participio irregular de "abrir"? (not *abrido)

**Back:** abierto

---

## Card 17
id: fc-20260216-100000-017
anki_id:
tags: preterito-perfecto, participio-irregular, ver
type: basic

**Front:** ¿Cuál es el participio irregular de "ver"? (not *veído)

**Back:** visto

---

## Card 18
id: fc-20260216-100000-018
anki_id:
tags: preterito-perfecto, participio-irregular, volver
type: basic

**Front:** ¿Cuál es el participio irregular de "volver"? (not *volvido)

**Back:** vuelto

---

## Card 19
id: fc-20260216-100000-019
anki_id:
tags: preterito-perfecto, participio-irregular, decir
type: basic

**Front:** ¿Cuál es el participio irregular de "decir"? (not *decido)

**Back:** dicho

---

## Card 20
id: fc-20260216-100000-020
anki_id:
tags: preterito-perfecto, participio-irregular, cloze, escribir
type: cloze

**Front:** He {{c1::escrito}} tres emails esta mañana. (escribir, participio irregular)

**Back:**

---

## Card 21
id: fc-20260216-100000-021
anki_id:
tags: preterito-perfecto, participio-irregular, cloze, hacer
type: cloze

**Front:** ¿Qué has {{c1::hecho}} hoy? (hacer, participio irregular)

**Back:**

---

## Card 22
id: fc-20260216-100000-022
anki_id:
tags: preterito-perfecto, usage, contrast
type: basic

**Front:** "He viajado mucho" vs "Viajé mucho" — ¿cuándo usar cada uno?

**Back:** "He viajado" (pret. perfecto) = connected to present / no specific time. "Viajé" (pret. indefinido) = specific finished event.

---

## Card 23
id: fc-20260216-100000-023
anki_id:
tags: preterito-perfecto, usage, temporal-markers
type: basic

**Front:** Which temporal markers signal pretérito perfecto? (not indefinido)

**Back:** hoy, esta semana, este mes, este año, ya, todavía no, alguna vez, nunca.

---

## Card 24
id: fc-20260216-100000-024
anki_id:
tags: preterito-perfecto, common-mistake
type: basic

**Front:** Common mistake: "Ayer he ido al cine." — Is this correct?

**Back:** No. "Ayer" signals a finished past event → "Ayer fui al cine" (pret. indefinido).
```

---

## Example 2: Image of Verb Table — Hablar, Present Tense (Workflow A)

User provides a screenshot of a textbook showing the hablar conjugation table.

### Bad: Enumeration card

```markdown
## Card 1
id: fc-20260216-130000-001
anki_id:
tags: spanish, hablar
type: basic

**Front:** Conjugate "hablar" in the present tense.

**Back:** hablo, hablas, habla, hablamos, habláis, hablan
```

### Good: One cloze per pronoun with contextual sentences

```markdown
## Card 1
id: fc-20260216-130000-001
anki_id:
tags: spanish, hablar, presente, yo
type: cloze

**Front:** Yo {{c1::hablo}} español con mis amigos. (hablar, presente)

**Back:**

---

## Card 2
id: fc-20260216-130000-002
anki_id:
tags: spanish, hablar, presente, tu
type: cloze

**Front:** Tú {{c1::hablas}} demasiado rápido, no te entiendo. (hablar, presente)

**Back:**

---

## Card 3
id: fc-20260216-130000-003
anki_id:
tags: spanish, hablar, presente, el-ella
type: cloze

**Front:** Mi profesora {{c1::habla}} tres idiomas. (hablar, presente)

**Back:**

---

## Card 4
id: fc-20260216-130000-004
anki_id:
tags: spanish, hablar, presente, nosotros
type: cloze

**Front:** Nosotros siempre {{c1::hablamos}} de la película después de verla. (hablar, presente)

**Back:**

---

## Card 5
id: fc-20260216-130000-005
anki_id:
tags: spanish, hablar, presente, vosotros
type: cloze

**Front:** Vosotros {{c1::habláis}} con un acento muy bonito. (hablar, presente)

**Back:**

---

## Card 6
id: fc-20260216-130000-006
anki_id:
tags: spanish, hablar, presente, ellos
type: cloze

**Front:** Los políticos {{c1::hablan}} mucho pero hacen poco. (hablar, presente)

**Back:**
```

---

## Example 3: Class Transcription — Travel Vocabulary (Workflow B)

User uploads a transcription. After discovery (Step B2), they select topic
"Vocabulary — travel". Relevant excerpts from transcription:

> Profesora: "Cuando llegas al aeropuerto, primero tienes que facturar el
> equipaje. Luego pasas por el control de seguridad. En la puerta de embarque
> esperas hasta que anuncien tu vuelo..."

### Good: Contextual vocabulary cards from the transcription

```markdown
---
topic: "Vocabulary — Travel (from class transcription)"
created: 2026-02-16
tags: [spanish, vocabulary, travel, class-2026-02-16]
deck: "Espanhol"
---

## Card 1
id: fc-20260216-150000-001
anki_id:
tags: vocabulary, travel, aeropuerto
type: cloze

**Front:** Cuando llegas al {{c1::aeropuerto}}, primero tienes que facturar el equipaje. (airport)

**Back:**

---

## Card 2
id: fc-20260216-150000-002
anki_id:
tags: vocabulary, travel, facturar
type: cloze

**Front:** Primero tienes que {{c1::facturar}} el equipaje en el mostrador. (to check in luggage)

**Back:**

---

## Card 3
id: fc-20260216-150000-003
anki_id:
tags: vocabulary, travel, equipaje
type: cloze

**Front:** No puedes llevar líquidos en el {{c1::equipaje}} de mano. (luggage)

**Back:**

---

## Card 4
id: fc-20260216-150000-004
anki_id:
tags: vocabulary, travel, control-de-seguridad
type: cloze

**Front:** Después de facturar, pasas por el {{c1::control de seguridad}}. (security check)

**Back:**

---

## Card 5
id: fc-20260216-150000-005
anki_id:
tags: vocabulary, travel, puerta-de-embarque
type: cloze

**Front:** Espera en la {{c1::puerta de embarque}} hasta que anuncien tu vuelo. (boarding gate)

**Back:**

---

## Card 6
id: fc-20260216-150000-006
anki_id:
tags: vocabulary, travel, vuelo
type: cloze

**Front:** Mi {{c1::vuelo}} sale a las ocho de la mañana. (flight)

**Back:**

---

## Card 7
id: fc-20260216-150000-007
anki_id:
tags: vocabulary, travel, tarjeta-de-embarque
type: cloze

**Front:** Necesitas la {{c1::tarjeta de embarque}} para subir al avión. (boarding pass)

**Back:**

---

## Card 8
id: fc-20260216-150000-008
anki_id:
tags: vocabulary, travel, reverse, aeropuerto
type: basic

**Front:** ¿Cómo se dice "airport" en español?

**Back:** aeropuerto

---

## Card 9
id: fc-20260216-150000-009
anki_id:
tags: vocabulary, travel, reverse, equipaje
type: basic

**Front:** ¿Qué significa "equipaje de mano"?

**Back:** Hand luggage / carry-on bag.
```

Note: Cards 8-9 show the "redundancy" pattern — same words, different angle
(comprehension vs production). Not every word needs both, but key vocabulary does.

---

## Example 4: Ser vs Estar — Contrast Cards (Workflow C)

User says: "Flashcards about when to use ser vs estar."

### Good: Structured contrast with common mistakes

```markdown
---
topic: "Ser vs Estar"
created: 2026-02-16
tags: [spanish, ser, estar, grammar]
deck: "Espanhol"
---

## Card 1
id: fc-20260216-160000-001
anki_id:
tags: ser, concept
type: basic

**Front:** What are the main uses of "ser"?

**Back:** Identity, origin, profession, permanent characteristics, time, material, events.

---

## Card 2
id: fc-20260216-160000-002
anki_id:
tags: estar, concept
type: basic

**Front:** What are the main uses of "estar"?

**Back:** Location, temporary states, emotions, conditions, progressive tenses.

---

## Card 3
id: fc-20260216-160000-003
anki_id:
tags: ser, estar, contrast, cansado
type: basic

**Front:** "Soy cansado" vs "Estoy cansado" — which is correct and why?

**Back:** "Estoy cansado" — tired is temporary. "Soy cansado" would mean "I'm a tiring person."

---

## Card 4
id: fc-20260216-160000-004
anki_id:
tags: ser, estar, contrast, aburrido
type: basic

**Front:** "Es aburrido" vs "Está aburrido" — what's the difference?

**Back:** "Es aburrido" = he's a boring person. "Está aburrido" = he's bored right now.

---

## Card 5
id: fc-20260216-160000-005
anki_id:
tags: ser, estar, contrast, listo
type: basic

**Front:** "Es listo" vs "Está listo" — what's the difference?

**Back:** "Es listo" = he's clever/smart. "Está listo" = he's ready.

---

## Card 6
id: fc-20260216-160000-006
anki_id:
tags: ser, estar, contrast, malo
type: basic

**Front:** "Es malo" vs "Está malo" — what's the difference?

**Back:** "Es malo" = he's a bad person. "Está malo" = he's sick / it tastes bad.

---

## Card 7
id: fc-20260216-160000-007
anki_id:
tags: estar, location, cloze
type: cloze

**Front:** Madrid {{c1::está}} en el centro de España. (location → estar)

**Back:**

---

## Card 8
id: fc-20260216-160000-008
anki_id:
tags: ser, origin, cloze
type: cloze

**Front:** Mi amigo {{c1::es}} de Brasil. (origin → ser)

**Back:**

---

## Card 9
id: fc-20260216-160000-009
anki_id:
tags: ser, profession, cloze
type: cloze

**Front:** Ella {{c1::es}} profesora de español. (profession → ser)

**Back:**

---

## Card 10
id: fc-20260216-160000-010
anki_id:
tags: estar, emotion, cloze
type: cloze

**Front:** Hoy {{c1::estoy}} muy contento porque es viernes. (temporary emotion → estar)

**Back:**

---

## Card 11
id: fc-20260216-160000-011
anki_id:
tags: ser, estar, common-mistake, age
type: basic

**Front:** Common mistake: "Estoy 25 años." — Is this correct?

**Back:** No. "Tengo 25 años." (In Spanish you "have" years, using tener, not ser or estar.)

---

## Card 12
id: fc-20260216-160000-012
anki_id:
tags: ser, estar, mnemonic
type: basic

**Front:** Mnemonic to remember "estar" uses: what does PLACE stand for?

**Back:** Position, Location, Action (progressive), Condition, Emotion.
```

---

## Example 5: Irregular Verb — Tener in Pretérito Indefinido (Workflow C)

### Good: Full coverage with contrast

```markdown
---
topic: "Tener — Pretérito Indefinido (irregular)"
created: 2026-02-16
tags: [spanish, tener, preterito-indefinido, irregular]
deck: "Espanhol"
---

## Card 1
id: fc-20260216-170000-001
anki_id:
tags: tener, preterito-indefinido, irregular, stem
type: basic

**Front:** What is the irregular stem of "tener" in pretérito indefinido?

**Back:** tuv- (not ten-). Uses special irregular endings: -e, -iste, -o, -imos, -isteis, -ieron.

---

## Card 2
id: fc-20260216-170000-002
anki_id:
tags: tener, preterito-indefinido, yo
type: cloze

**Front:** Ayer {{c1::tuve}} que trabajar hasta muy tarde. (tener, pret. indefinido)

**Back:**

---

## Card 3
id: fc-20260216-170000-003
anki_id:
tags: tener, preterito-indefinido, tu
type: cloze

**Front:** ¿{{c1::Tuviste}} tiempo de hacer la tarea? (tener, pret. indefinido)

**Back:**

---

## Card 4
id: fc-20260216-170000-004
anki_id:
tags: tener, preterito-indefinido, el-ella
type: cloze

**Front:** Ella {{c1::tuvo}} un accidente la semana pasada. (tener, pret. indefinido)

**Back:**

---

## Card 5
id: fc-20260216-170000-005
anki_id:
tags: tener, preterito-indefinido, nosotros
type: cloze

**Front:** Nosotros {{c1::tuvimos}} mucha suerte con el clima. (tener, pret. indefinido)

**Back:**

---

## Card 6
id: fc-20260216-170000-006
anki_id:
tags: tener, preterito-indefinido, ellos
type: cloze

**Front:** Los estudiantes {{c1::tuvieron}} que repetir el examen. (tener, pret. indefinido)

**Back:**

---

## Card 7
id: fc-20260216-170000-007
anki_id:
tags: tener, preterito-indefinido, pattern
type: basic

**Front:** Which other verbs follow the same irregular pattern as "tener" (tuv-) in pretérito indefinido?

**Back:** estar (estuv-), andar (anduv-). They all use tuv/estuv/anduv + -e, -iste, -o, -imos, -isteis, -ieron.
```

---

## Example 6: Grammar Expression — "Acabar de + infinitivo" (Workflow B)

From a class transcription where the teacher explains this expression.

```markdown
---
topic: "Acabar de + infinitivo"
created: 2026-02-16
tags: [spanish, expression, acabar-de, recent-past]
deck: "Espanhol"
---

## Card 1
id: fc-20260216-180000-001
anki_id:
tags: acabar-de, concept
type: basic

**Front:** What does "acabar de + infinitivo" express?

**Back:** An action that JUST happened (very recent past).

---

## Card 2
id: fc-20260216-180000-002
anki_id:
tags: acabar-de, example, yo
type: cloze

**Front:** {{c1::Acabo de}} llegar a casa, estoy agotado. (I just arrived)

**Back:**

---

## Card 3
id: fc-20260216-180000-003
anki_id:
tags: acabar-de, example, ella
type: cloze

**Front:** Ella {{c1::acaba de}} terminar el examen. (She just finished)

**Back:**

---

## Card 4
id: fc-20260216-180000-004
anki_id:
tags: acabar-de, example, nosotros
type: cloze

**Front:** {{c1::Acabamos de}} comer, no tenemos hambre. (We just ate)

**Back:**

---

## Card 5
id: fc-20260216-180000-005
anki_id:
tags: acabar-de, contrast
type: basic

**Front:** "Acabo de comer" vs "He comido" — what's the difference?

**Back:** "Acabo de comer" = I JUST ate (minutes ago). "He comido" = I have eaten (anytime today).

---

## Card 6
id: fc-20260216-180000-006
anki_id:
tags: acabar-de, past-usage
type: basic

**Front:** How do you say "I had just arrived" (acabar de in the past)?

**Back:** "Acababa de llegar" — use imperfecto of acabar + de + infinitivo.
```

---

## Quick Reference: Card Type Decision

| Content Type | Card Type | Example |
|---|---|---|
| Verb conjugation (one form) | cloze | `Yo {{c1::hablo}} español.` |
| Grammar rule (what/when) | basic | `When to use subjunctive? → After verbs of desire/doubt.` |
| Irregular form (what is it) | basic | `Participio de "escribir"? → escrito` |
| Irregular form (in context) | cloze | `He {{c1::escrito}} tres emails.` |
| Vocabulary (in context) | cloze | `Necesito la {{c1::maleta}}.` |
| Vocabulary (translation) | basic | `"suitcase" en español? → maleta` |
| Contrast (X vs Y) | basic | `"soy cansado" vs "estoy cansado"?` |
| Common mistake | basic | `"Ayer he ido" — correct? → No, "Ayer fui."` |
| Mnemonic/pattern | basic | `"-go" verbs: tengo, vengo, pongo, salgo, hago.` |
