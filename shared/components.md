# Shared components — reference for unit/section agents (READ-ONLY)

Every page links the global stylesheet. From `book/units/unit-NN-slug/`:

```html
<link rel="stylesheet" href="../../shared/styles.css">
```

From `book/front/` or `book/back/`:

```html
<link rel="stylesheet" href="../shared/styles.css">
```

## 1. Body class → unit gradient

Add `class="unit-N"` (N = 1…14, **no leading zero**) to `<body>`. This sets
`--grad-start` / `--grad-end` for every banner and strip on the page.
Front/back matter omits the class and gets the neutral cream→gold gradient.

```html
<body class="unit-7">
```

## 2. Page skeleton

Copy `shared/page-template.html`. Structure:

```html
<div class="page">
  <!-- corner blob (omit on cover / title / opener) -->
  <svg class="corner-blob" viewBox="0 0 150 120" aria-hidden="true">…</svg>

  <div class="section-banner">VOCABULARY</div>
  … content …

  <nav class="page-nav">
    <a href="PREV.html">← Previous</a>
    <a href="../../front/04-contents.html">Contents</a>
    <a href="NEXT.html">Next →</a>
  </nav>
  <div class="page-number">12</div>
</div>
```

## 3. Corner blob SVG (paste verbatim)

```html
<svg class="corner-blob" viewBox="0 0 150 120" aria-hidden="true">
  <path d="M150 0 L60 0 C40 18 52 38 74 42 C100 47 102 70 88 84 C76 96 84 112 104 116 L150 120 Z" fill="#F8B4D0" opacity="0.85"/>
  <path d="M150 0 L95 0 C82 14 92 28 108 32 C128 37 130 56 120 66 C112 75 118 88 132 92 L150 96 Z" fill="#FFE066" opacity="0.9"/>
  <circle cx="70" cy="14" r="7" fill="#F8B4D0" opacity="0.6"/>
  <circle cx="56" cy="34" r="4" fill="#FFD43B" opacity="0.7"/>
</svg>
```

## 4. Reader icon SVG (inside every `.activity-strip` — paste verbatim)

```html
<svg class="reader-icon" viewBox="0 0 26 26" aria-hidden="true">
  <circle cx="13" cy="7" r="4" fill="#5A4632"/>
  <path d="M4 22 C4 15 8 13 13 13 C18 13 22 15 22 22 Z" fill="#5A4632"/>
  <path d="M6 17 L13 19 L20 17 L20 23 L13 25 L6 23 Z" fill="#FFFDF0" stroke="#5A4632" stroke-width="1"/>
  <line x1="13" y1="19" x2="13" y2="25" stroke="#5A4632" stroke-width="1"/>
</svg>
```

## 5. Section banner naming convention

Exactly these labels, uppercase, one per `.section-banner`:
`WARM UP` · `VOCABULARY` · `GRAMMAR` · `LISTENING` · `READING` ·
`SPEAKING` · `WRITING` · `HOMETASK`

## 6. Activity strip + box pair

```html
<div class="activity-strip">
  <svg class="reader-icon" …>…</svg>
  <span class="instruction">3. Fill in the blanks with the correct form.</span>
</div>
<div class="activity-box">
  <ol>
    <li>The hotel <span class="gap"></span> 120 rooms. (have)</li>
  </ol>
</div>
```

Activity numbering is **consecutive across the whole unit** (warm-up = 1).
Write numbers literally in the instruction text.

## 7. Specialized blocks

| Block | Class | Used by |
|---|---|---|
| Useful language (set phrases) | `.useful-language` (+`.sub` for sub-functions) | Units 4, 6, 7, 8, 9, 11, 12, 13, 14 |
| Grammar rule presentation | `.grammar-rule-box` + `.form-table` | all grammar pages |
| Recycled-grammar note | `.watch-out` | Units 12, 13, 14 (+ any repeat) |
| Dialogue (A/B color turns) | `.dialogue` > `.turn.a` / `.turn.b` + `.who` | dialogues everywhere |
| Telephone script (2 columns) | `table.phone-script` | Unit 8 |
| Map / directions | `.map-box` (inline SVG grid inside) | Unit 6 |
| Email | `.email-block` > `.email-header` + `.email-body` | Units 3, 7, 12, 13 |
| Itinerary / schedule | `table.itinerary` (`td.time` for the time column) | Units 9, 13 |
| Warning / safety notice | `.warning-box` | Unit 14 |
| Role-play pair | `.roleplay-cards` > `.roleplay-card.student-a/.student-b`; situations in `.situation-card` | every speaking page |
| Word cloud | `.word-cloud` > `.cloud` (+`.cloud.center`) | warm-ups |
| Photo placeholder | `.photo-placeholder` (caption text inside) | everywhere |
| Image-match grid | `.img-grid` > `.cell` (`.letter`, `.caption`) | vocab matching |
| Vocab card | `.vocab-card` | vocab presentations |
| Reading text | `.reading-text` | reading pages |
| Can-do self-check | `ul.cando-list` | hometask pages |
| Discussion questions | `ul.discussion-list` | warm-up/reading/speaking |
| Listening media row | `.listening-media` (audio + `.qr-code`) | listening pages |
| 2/3-column layout | `.cols-2` / `.cols-3` | anywhere |

## 8. Listening media (audio + QR side by side)

```html
<div class="listening-media">
  <audio controls src="../../assets/audio/unit-07.mp3"></audio>
  <div>
    <div class="qr-code"><img src="../../assets/qr/unit-07.svg" alt="QR code for audio track"></div>
    <div class="qr-note">Scan to listen on your phone</div>
  </div>
</div>
```

## 9. Photo placeholder

```html
<div class="photo-placeholder" style="min-height:140px">Tour guide leading a group in front of a landmark — placeholder</div>
```

The 📷 prefix is added by CSS — don't type it.

## 10. Harvest comments (MANDATORY — see your prompt)

- `02-…` and `03-…` vocabulary files: `<!-- GLOSSARY: [ … ] -->` at the top.
- `04…08` files: `<!-- ANSWERS: { … } -->` at the top.
- `05-listening.html`: also `<!-- TRANSCRIPT: { … } -->`.

Keep the JSON valid — back-matter agents parse it mechanically.
