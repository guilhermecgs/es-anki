# Flashcard Best Practices

Based on Dr. Piotr Wozniak's "20 Rules of Formulating Knowledge" (SuperMemo) and Anki community consensus.

## The 20 Rules (Condensed)

### 1. Do Not Learn What You Don't Understand
Never create a card for content you haven't grasped. If the source material is unclear, research it first or ask the user to clarify. Blind memorization wastes time and produces negligible retention.

### 2. Understand Before You Memorize
Build the big picture first. Read the full chapter, article, or source. Only then break it into individual cards. Isolated facts without context are like single words in a foreign language.

### 3. Build Upon Basics
Start with the simplest, most fundamental concepts. Basics are easy to retain, take minimal review time, yet form the foundation for everything else. Usually 3-5% of material accounts for 50% of review time — basics should not be part of that 3-5%.

### 4. Minimum Information Principle (CRITICAL)
**The single most important rule.** Each card must be as simple as possible.

Why:
- Simple items are easier to schedule in spaced repetition.
- The brain processes simple items the same way every time → stronger memory traces.
- Complex items create multiple neural pathways that interfere with each other.

**Bad:** "What are the characteristics of the Dead Sea?" → long multi-fact answer.
**Good:** Split into 8+ cards, each asking one fact (location, depth, salt content, etc.).

### 5. Cloze Deletion Is Easy and Effective
A sentence with a missing part replaced by `{{c1::...}}`. Fast to create, strong mnemonic power. Ideal for:
- Vocabulary
- Facts embedded in context
- Definitions
- Formulas

### 6. Use Imagery
The visual cortex retains information far more easily than verbal processing. When possible, describe images or suggest the user include screenshots/diagrams. Geographic, anatomical, and scientific content benefits enormously.

### 7. Use Mnemonic Techniques
Acronyms, memory palaces, peg lists, rhymes. Only needed for ~1-5% of cards but can make the difference for stubborn items.

### 8. Graphic Deletion (Occlusion)
Like cloze deletion but for images — hide part of an image and ask "what goes here?" Great for maps, anatomy, diagrams. One image can generate 10-20 cards.

### 9. Avoid Sets
"List all countries in the EU" is nearly impossible to memorize. Convert sets into:
- Historical narratives ("Which country joined in 1981?")
- Individual fact cards
- Grouped sub-sets of 2-3 items max

### 10. Avoid Enumerations
Ordered lists are slightly better than sets but still hard. Use overlapping cloze deletions:
- "A, ___, C, D" → B
- "B, ___, D, E" → C
This creates redundancy that strengthens each link.

### 11. Combat Interference
Similar cards cause confusion. When you notice two cards could be mixed up:
- Add distinguishing context to both
- Use contrasting examples
- Reference the "confusing sibling" explicitly

### 12. Optimize Wording
Every unnecessary word slows review. Strip to the minimum needed for unambiguous recall.

**Bad:** "Aldus invented desktop publishing in 1985 with PageMaker. Aldus had little competition for years, and so failed to improve. Then Denver-based ___ blew past."
**Good:** "PageMaker lost ground to ___" → Quark

### 13. Refer to Other Memories
Cross-reference related cards. "Unlike X (which means Y), this word means ___" helps the brain anchor new knowledge to existing memories and reduces interference.

### 14. Personalize and Provide Examples
Connect knowledge to the learner's life. "Your hometown has 100k people; the Dead Sea is ___ km long" is more memorable than an isolated number.

### 15. Use Redundancy Wisely
Multiple cards approaching the same fact from different angles is OK — this is different from having one bloated card. "What is the capital of France?" and "Paris is the capital of ___" both reinforce the same memory.

### 16. Provide Sources
When relevant, note where the information came from. Helps the user trust and revisit the material.

### 17. Provide Date Stamps
For time-sensitive facts (statistics, current events), note the date so the user knows when it may become outdated.

### 18. Prioritize
Not everything deserves a card. Focus on high-value knowledge. Ask: "Will the user need this in 6 months?"

### 19. Card Independence
Each card must be self-contained. It should make sense without seeing other cards. Don't use "as mentioned in Card 3" references.

### 20. Emotional Connection
Facts tied to emotions (surprise, humor, curiosity) are retained better. A well-crafted question that triggers "oh, interesting!" is better than a dry factual prompt.

---

## Language Learning Specific Tips

Since the user studies Spanish verb conjugations, these extra rules apply:

### Conjugation Cards
- One card per person/tense combination (yo/tú/él/nosotros/vosotros/ellos).
- Front: sentence with blank. Back: conjugated verb only.
- Include an example sentence — not just the isolated verb form.

### Example Pattern for Verbs

**Basic conjugation:**
```
Front: "hablar" — yo, presente de indicativo → ___
Back: hablo
```

**Contextual (preferred):**
```
Front: Yo ___ (hablar) español todos los días. [presente]
Back: hablo
```

**Cloze (best):**
```
Front: Yo {{c1::hablo}} español todos los días.
```

### Irregular Verb Strategy
- Create cards that contrast the irregular form with what the regular form *would* be.
- "Yo ___ (tener) hambre" → tengo (not *teno*)
- Add a card: "Why is 'tener' irregular in yo? → stem change: ten → teng"

### Common Pitfalls in Language Cards
- Don't put translations on the front (tests reading, not recall).
- Don't combine multiple tenses in one card.
- Don't ask "conjugate hablar in present" → too many answers. One person at a time.
