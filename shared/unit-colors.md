# Per-unit gradient palettes

Each unit owns a unique gradient pair used by its `.section-banner` and
`.activity-strip` components. **Never hardcode these hex values in unit
pages** — instead add `class="unit-N"` to `<body>` and the CSS custom
properties `--grad-start` / `--grad-end` are inherited automatically
(defined in `tokens.css`).

| Unit | Theme | `--grad-start` | `--grad-end` | Feel |
|------|-------|----------------|--------------|------|
| 1  | Introduction to the Tourism Industry | `#F8B4D0` | `#FFE9B0` | pink → soft yellow |
| 2  | Hotel Types and Accommodation        | `#FF8A8A` | `#FFCBA4` | coral → peach |
| 3  | Making and Managing Reservations     | `#FFB36B` | `#FFE388` | orange → yellow |
| 4  | Check-in and Check-out Procedures    | `#7FD1C7` | `#FFE388` | teal → yellow |
| 5  | Food and Beverage Service            | `#B5E48C` | `#99C7FF` | green → blue |
| 6  | Giving Directions and Information    | `#A78BFA` | `#FBCFE8` | violet → pink |
| 7  | Handling Complaints and Problems     | `#FCD34D` | `#FECACA` | gold → rose |
| 8  | Telephone Skills in Tourism          | `#FB923C` | `#FDE68A` | deep orange → soft yellow |
| 9  | Tour Guiding Basics                  | `#FCA5A5` | `#FED7AA` | rose → peach |
| 10 | Describing Attractions and Landmarks | `#FBA74D` | `#F8B4D0` | amber → pink |
| 11 | Cultural Awareness and Etiquette     | `#FDBA74` | `#FCD34D` | peach → gold |
| 12 | Promoting Tourism Services           | `#86EFAC` | `#BAE6FD` | mint → sky |
| 13 | Business Tourism and Events          | `#A7F3D0` | `#93C5FD` | mint → blue |
| 14 | Emergency Situations and Safety      | `#FCA5A5` | `#BBF7D0` | rose → mint |

Front matter and back matter use the **default** neutral palette
(`#FFE9B0 → #F8D448`, cream → gold) — simply omit the unit class.

## Usage

```html
<body class="unit-3">
  <!-- every .section-banner and .activity-strip on this page
       automatically renders in the Unit 3 orange→yellow gradient -->
</body>
```
