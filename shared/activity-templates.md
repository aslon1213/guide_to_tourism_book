# Activity templates — ready-to-paste HTML snippets (READ-ONLY)

Every activity = `.activity-strip` (numbered, italic-bold instruction, reader
icon) + `.activity-box` (content). The reader-icon SVG is in `components.md §4`
— paste it verbatim into every strip; below it is abbreviated as
`<svg class="reader-icon" …>…</svg>`.

---

## 1. Match words to pictures

```html
<div class="activity-strip">
  <svg class="reader-icon" …>…</svg>
  <span class="instruction">1. Match the words with their pictures.</span>
</div>
<div class="activity-box">
  <div class="cols-2">
    <ol>
      <li>single room</li>
      <li>lobby</li>
      <!-- 8 items total -->
    </ol>
    <div></div>
  </div>
  <div class="img-grid">
    <div class="cell">
      <div class="letter">A</div>
      <div class="photo-placeholder">a hotel lobby with sofas — placeholder</div>
      <div class="caption">the entrance area of a hotel where guests wait</div>
    </div>
    <!-- cells B–H -->
  </div>
</div>
```

## 2. Match words to definitions

```html
<div class="activity-strip">…<span class="instruction">2. Match the words (1–8) with their definitions (a–h).</span></div>
<div class="activity-box">
  <table class="match-table">
    <tr><th>Word</th><th>Definition</th></tr>
    <tr><td>1. concierge</td><td>a) a hotel employee who helps guests with tours, taxis and tickets</td></tr>
    <!-- shuffled definitions -->
  </table>
</div>
```

## 3. Multiple choice (a/b/c)

```html
<div class="activity-strip">…<span class="instruction">3. Choose the correct option.</span></div>
<div class="activity-box">
  <ol>
    <li>The guests ___ at the front desk every morning.
      <br>a) checks in &nbsp;&nbsp; b) check in &nbsp;&nbsp; c) checking in</li>
  </ol>
</div>
```

## 4. Fill in the blanks

```html
<div class="activity-strip">…<span class="instruction">4. Fill in the blanks with the correct word.</span></div>
<div class="activity-box">
  <ol>
    <li>Our hotel <span class="gap"></span> a swimming pool and a spa.</li>
    <li>The tour starts <span class="gap wide"></span> the main square.</li>
  </ol>
</div>
```

## 5. True / False

```html
<div class="activity-strip">…<span class="instruction">5. Read the statements and mark them True (T) or False (F).</span></div>
<div class="activity-box">
  <ol>
    <li>The museum is open on Mondays. &nbsp; <strong>T / F</strong></li>
  </ol>
</div>
```

## 6. Picture-prompt discussion

```html
<div class="activity-strip">…<span class="instruction">1. Look at the picture and discuss the questions with a partner.</span></div>
<div class="activity-box">
  <div class="cols-2">
    <div class="photo-placeholder" style="min-height:150px">busy airport check-in hall — placeholder</div>
    <ul class="discussion-list">
      <li>Where are these people?</li>
      <li>What is happening?</li>
      <li>Have you ever been in a similar situation?</li>
    </ul>
  </div>
</div>
```

## 7. Word cloud

```html
<div class="activity-strip">…<span class="instruction">1. Write words related to hotels into the clouds.</span></div>
<div class="activity-box">
  <div class="word-cloud">
    <div class="cloud">reception</div>  <!-- one filled example -->
    <div class="cloud">&nbsp;</div>
    <div class="cloud">&nbsp;</div>
    <div class="cloud">&nbsp;</div>
    <div class="cloud center">HOTEL</div>
    <div class="cloud">&nbsp;</div>
    <div class="cloud">&nbsp;</div>
    <div class="cloud">&nbsp;</div>
    <div class="cloud">&nbsp;</div>
  </div>
</div>
```

## 8. Listening with QR + audio

```html
<div class="activity-strip">…<span class="instruction">8. Listen and complete the sentences with ONE word or a number.</span></div>
<div class="activity-box">
  <div class="listening-media">
    <audio controls src="../../assets/audio/unit-NN.mp3"></audio>
    <div>
      <div class="qr-code"><img src="../../assets/qr/unit-NN.svg" alt="QR code for audio track"></div>
      <div class="qr-note">Scan to listen on your phone</div>
    </div>
  </div>
  <ol>
    <li>The guest's reservation is for <span class="gap"></span> nights.</li>
  </ol>
</div>
```

## 9. Reading text block

```html
<div class="activity-strip">…<span class="instruction">10. Read the text and underline all the Present Simple forms.</span></div>
<div class="reading-text">
  <h3>“My First Week at the Front Desk”</h3>
  <p>…original 280–380 word text, justified…</p>
</div>
```

## 10. Role-play card pair + situations

```html
<div class="activity-strip">…<span class="instruction">12. Work in pairs. Role-play the situations below.</span></div>
<div class="activity-box">
  <div class="roleplay-cards">
    <div class="roleplay-card student-a">
      <h5>Student A — Guest</h5>
      <p>You arrive at the hotel at 23:00. Your booking has disappeared from the system. Stay polite but firm.</p>
    </div>
    <div class="roleplay-card student-b">
      <h5>Student B — Receptionist</h5>
      <p>The hotel is almost full. Apologize, check the options, and offer a solution.</p>
    </div>
  </div>
  <div class="situation-card">
    <h6>Situation 1</h6>
    <p>…</p>
  </div>
</div>
```

## 11. Sentence construction (word / word / word)

```html
<div class="activity-strip">…<span class="instruction">6. Make correct sentences from the prompts.</span></div>
<div class="activity-box">
  <ol>
    <li>guide / meet / tourists / lobby / 9 a.m. →</li>
  </ol>
</div>
```

## 12. Dialogue scaffold (gapped)

```html
<div class="activity-strip">…<span class="instruction">7. Complete the dialogue with the phrases from the box.</span></div>
<div class="activity-box">
  <div class="useful-language"><ul><li>How may I help you?</li><li>…word bank…</li></ul></div>
  <div class="dialogue">
    <div class="turn a"><span class="who">Receptionist:</span><span>Good evening! <span class="gap wide"></span></span></div>
    <div class="turn b"><span class="who">Guest:</span><span>Hello. I'd like to <span class="gap wide"></span>, please.</span></div>
  </div>
</div>
```

## 13. Discussion questions list

```html
<div class="activity-strip">…<span class="instruction">9. Discuss these questions with your partner.</span></div>
<div class="activity-box">
  <ul class="discussion-list">
    <li>Why do people travel?</li>
  </ul>
</div>
```

## 14. Grammar rule + form table

```html
<div class="grammar-rule-box">
  <h4>Present Simple — describing jobs and routines</h4>
  <p>We use the Present Simple to talk about things that happen regularly or are always true.</p>
  <ul class="examples">
    <li>A concierge <strong>helps</strong> guests with restaurant bookings.</li>
  </ul>
  <table class="form-table">
    <tr><th></th><th>Affirmative</th><th>Negative</th><th>Question</th></tr>
    <tr><td>I / you / we / they</td><td>work</td><td>don't work</td><td>Do you work…?</td></tr>
    <tr><td>he / she / it</td><td>works</td><td>doesn't work</td><td>Does she work…?</td></tr>
  </table>
</div>
```

## 15. Useful-language box (functional sets)

```html
<div class="useful-language">
  <h4>Useful language — answering the phone</h4>
  <div class="sub">Opening the call</div>
  <ul><li>Good morning, Sunrise Tours, Aziza speaking. How can I help you?</li></ul>
  <div class="sub">Asking for spelling</div>
  <ul><li>Could you spell that for me, please?</li></ul>
  <div class="sub">Closing the call</div>
  <ul><li>Thank you for calling. Have a great day!</li></ul>
</div>
```

## 16. Telephone-script template (Unit 8)

```html
<div class="activity-strip">…<span class="instruction">11. Complete the telephone conversation. Then practise it in pairs.</span></div>
<div class="activity-box">
  <table class="phone-script">
    <tr><th>Caller (Customer)</th><th>Receiver (Receptionist)</th></tr>
    <tr><td></td><td>Good afternoon, Grand Silk Road Hotel. <span class="gap wide"></span>?</td></tr>
    <tr><td>Hello, I'd like to book a tour for tomorrow.</td><td></td></tr>
    <tr><td></td><td>Certainly. <span class="gap wide"></span> your name, please?</td></tr>
  </table>
</div>
```

## 17. Map / directions template (Unit 6)

```html
<div class="activity-strip">…<span class="instruction">5. Look at the map. Follow the directions and find the destination.</span></div>
<div class="map-box">
  <svg viewBox="0 0 560 320" width="560" height="320">
    <rect width="560" height="320" fill="#FBF7E4"/>
    <!-- streets -->
    <rect x="0" y="140" width="560" height="40" fill="#E2DCC0"/>
    <rect x="180" y="0" width="40" height="320" fill="#E2DCC0"/>
    <rect x="380" y="0" width="40" height="320" fill="#E2DCC0"/>
    <text x="280" y="165" text-anchor="middle" font-size="13" font-family="Georgia" font-style="italic">Main Street</text>
    <!-- landmark blocks: label each with <rect> + <text> -->
    <rect x="20" y="30" width="130" height="80" rx="8" fill="#F8B4D0"/>
    <text x="85" y="75" text-anchor="middle" font-size="12" font-family="Inter,sans-serif">HOTEL</text>
    <rect x="240" y="30" width="110" height="80" rx="8" fill="#BAE6FD"/>
    <text x="295" y="75" text-anchor="middle" font-size="12" font-family="Inter,sans-serif">MUSEUM</text>
    <rect x="240" y="210" width="110" height="80" rx="8" fill="#B5E48C"/>
    <text x="295" y="255" text-anchor="middle" font-size="12" font-family="Inter,sans-serif">BANK</text>
    <rect x="440" y="210" width="100" height="80" rx="8" fill="#FED7AA"/>
    <text x="490" y="255" text-anchor="middle" font-size="12" font-family="Inter,sans-serif">STATION</text>
    <!-- you-are-here + arrow -->
    <circle cx="200" cy="160" r="8" fill="#D32F2F"/>
    <text x="200" y="190" text-anchor="middle" font-size="10" font-family="Inter,sans-serif">YOU ARE HERE</text>
    <path d="M220 160 H300 V120" stroke="#D32F2F" stroke-width="3" fill="none" stroke-dasharray="6 4" marker-end="url(#arrow)"/>
    <defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#D32F2F"/></marker></defs>
  </svg>
</div>
```

Adapt the landmark set (PARK, CAFÉ, MOSQUE, THEATRE, PHARMACY, BAZAAR…) and
the route arrow to the exercise. Keep it a simple grid.

## 18. Email template (Unit 13 and others)

```html
<div class="email-block">
  <div class="email-header">
    <div><span class="label">From:</span> events@silkroadhotel.uz</div>
    <div><span class="label">To:</span> j.miller@globex.com</div>
    <div><span class="label">Subject:</span> Conference booking confirmation — 12–14 May</div>
  </div>
  <div class="email-body">
    <p>Dear Ms Miller,</p>
    <p>…</p>
    <p>Kind regards,<br>Dilnoza Karimova<br>Events Coordinator</p>
  </div>
</div>
```

## 19. Itinerary / schedule template (Units 9, 13)

```html
<table class="itinerary">
  <tr><th>Time</th><th>Activity</th><th>Location</th></tr>
  <tr><td class="time">09:00</td><td>Welcome coffee and registration</td><td>Hotel lobby</td></tr>
  <tr><td class="time">09:30</td><td>Old-town walking tour begins</td><td>Registan Square</td></tr>
</table>
```

## 20. Emergency notice template (Unit 14)

```html
<div class="warning-box">
  <h4>Safety Notice</h4>
  <p><strong>In case of fire:</strong> Do not use the lifts. Leave the building by the nearest emergency exit and go to the assembly point in the front garden.</p>
</div>
```

## 21. Can-do self-check (hometask pages)

```html
<div class="activity-strip">…<span class="instruction">Self-check: tick what you can do now.</span></div>
<div class="activity-box">
  <ul class="cando-list">
    <li>I can describe a hotel and its facilities.</li>
    <li>I can compare two hotels using comparatives and superlatives.</li>
  </ul>
</div>
```

---

### Variety rules

- Never use the same activity type 3× in one unit.
- Vary warm-up types across units (cloud / picture / brainstorm / discussion / ranking).
- Vary reading genres (see your unit prompt).
- Keep every scenario inside tourism / hospitality.
