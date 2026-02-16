# Flashcard Examples: Good vs Bad

## Example 1: Geography — Dead Sea

### Bad (one complex card)

```markdown
## Card 1
id: fc-20260216-120000-001
anki_id:
tags: geography, dead-sea
type: basic

**Front:** What are the characteristics of the Dead Sea?

**Back:** Salt lake on the border of Israel and Jordan. Shoreline is the lowest point on Earth at 396m below sea level. 74 km long. Seven times saltier than the ocean (30% salt by volume). Density keeps swimmers afloat. Only simple organisms survive.
```

### Good (split into atomic cards)

```markdown
## Card 1
id: fc-20260216-120000-001
anki_id:
tags: geography, dead-sea, location
type: basic

**Front:** Where is the Dead Sea located?

**Back:** On the border between Israel and Jordan.

---

## Card 2
id: fc-20260216-120000-002
anki_id:
tags: geography, dead-sea, elevation
type: basic

**Front:** What is the lowest point on the Earth's surface?

**Back:** The Dead Sea shoreline (~400m below sea level).

---

## Card 3
id: fc-20260216-120000-003
anki_id:
tags: geography, dead-sea, salinity
type: basic

**Front:** How much saltier is the Dead Sea compared to the ocean?

**Back:** About 7 times (30% salt by volume).

---

## Card 4
id: fc-20260216-120000-004
anki_id:
tags: geography, dead-sea, buoyancy
type: basic

**Front:** Why can the Dead Sea keep swimmers afloat?

**Back:** Its extremely high salt content increases water density.

---

## Card 5
id: fc-20260216-120000-005
anki_id:
tags: geography, dead-sea, biology
type: basic

**Front:** Why is the Dead Sea called "Dead"?

**Back:** Only simple organisms can survive in its highly saline water.
```

---

## Example 2: Spanish Verb Conjugation — Hablar (Present Tense)

### Bad (one enumeration card)

```markdown
## Card 1
id: fc-20260216-130000-001
anki_id:
tags: spanish, verbs
type: basic

**Front:** Conjugate "hablar" in the present tense.

**Back:** hablo, hablas, habla, hablamos, habláis, hablan
```

### Good (one card per person, with context)

```markdown
## Card 1
id: fc-20260216-130000-001
anki_id:
tags: spanish, hablar, presente, yo
type: cloze

**Front:** Yo {{c1::hablo}} español con mis amigos.

**Back:**

---

## Card 2
id: fc-20260216-130000-002
anki_id:
tags: spanish, hablar, presente, tu
type: cloze

**Front:** Tú {{c1::hablas}} demasiado rápido.

**Back:**

---

## Card 3
id: fc-20260216-130000-003
anki_id:
tags: spanish, hablar, presente, el-ella
type: cloze

**Front:** Ella {{c1::habla}} tres idiomas.

**Back:**

---

## Card 4
id: fc-20260216-130000-004
anki_id:
tags: spanish, hablar, presente, nosotros
type: cloze

**Front:** Nosotros {{c1::hablamos}} de la película de ayer.

**Back:**

---

## Card 5
id: fc-20260216-130000-005
anki_id:
tags: spanish, hablar, presente, vosotros
type: cloze

**Front:** Vosotros {{c1::habláis}} con acento andaluz.

**Back:**

---

## Card 6
id: fc-20260216-130000-006
anki_id:
tags: spanish, hablar, presente, ellos
type: cloze

**Front:** Ellos {{c1::hablan}} sobre política todo el tiempo.

**Back:**
```

---

## Example 3: Irregular Verb — Tener (Present Tense)

### Good (contrasting regular expectation with irregular form)

```markdown
## Card 1
id: fc-20260216-140000-001
anki_id:
tags: spanish, tener, presente, yo, irregular
type: cloze

**Front:** Yo {{c1::tengo}} mucha hambre. (tener, irregular: ten→teng)

**Back:**

---

## Card 2
id: fc-20260216-140000-002
anki_id:
tags: spanish, tener, presente, tu, irregular
type: cloze

**Front:** Tú {{c1::tienes}} razón. (tener, irregular: e→ie)

**Back:**

---

## Card 3
id: fc-20260216-140000-003
anki_id:
tags: spanish, tener, presente, el-ella, irregular
type: cloze

**Front:** Él {{c1::tiene}} dos hermanos. (tener, irregular: e→ie)

**Back:**

---

## Card 4
id: fc-20260216-140000-004
anki_id:
tags: spanish, tener, irregular, explanation
type: basic

**Front:** Why is "tener" irregular in the "yo" form of presente de indicativo?

**Back:** Stem changes from "ten" to "teng" → yo tengo (a common -go irregularity).
```

---

## Example 4: Programming — Python DataFrames

### Bad (two concepts in one card)

```markdown
## Card 1
id: fc-20260216-150000-001
anki_id:
tags: python, pandas
type: basic

**Front:** How do you add a column to a DataFrame and what are the arguments?

**Back:** Use df.insert(loc, column, value) where loc is index position, column is name, and value is data.
```

### Good (atomic)

```markdown
## Card 1
id: fc-20260216-150000-001
anki_id:
tags: python, pandas, dataframe, insert
type: basic

**Front:** What pandas method inserts a column at a specific position in a DataFrame?

**Back:** `df.insert()`

---

## Card 2
id: fc-20260216-150000-002
anki_id:
tags: python, pandas, dataframe, insert, arguments
type: cloze

**Front:** `df.insert({{c1::loc}}, {{c2::column}}, {{c3::value}})` — position, name, data.

**Back:**
```

---

## Example 5: Using Redundancy (Same Fact, Different Angles)

```markdown
## Card 1
id: fc-20260216-160000-001
anki_id:
tags: geography, capitals, france
type: basic

**Front:** What is the capital of France?

**Back:** Paris.

---

## Card 2
id: fc-20260216-160000-002
anki_id:
tags: geography, capitals, france
type: basic

**Front:** Paris is the capital of which country?

**Back:** France.
```

Both cards reinforce the same association from different directions (production vs recognition). This is acceptable redundancy.
