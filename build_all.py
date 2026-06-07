#!/usr/bin/env python3
"""Build book/all.html — single-file print version of the whole book.

Concatenates every page in reading order, keeps one global <head>,
rewrites relative asset/page paths to be valid from book/, preserves
each page's unit gradient by wrapping its content in <div class="unit-N">,
and inserts page-break dividers between source files.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent

UNIT_DIRS = [
    "unit-01-tourism-industry", "unit-02-hotel-accommodation",
    "unit-03-reservations", "unit-04-check-in-out", "unit-05-food-beverage",
    "unit-06-directions", "unit-07-complaints", "unit-08-telephone",
    "unit-09-tour-guiding", "unit-10-attractions", "unit-11-culture-etiquette",
    "unit-12-promoting", "unit-13-business-events", "unit-14-emergencies",
]
UNIT_FILES = [
    "01-opener.html", "02-warmup-vocabulary.html", "03-vocabulary.html",
    "04-grammar.html", "05-listening.html", "06-reading.html",
    "07-speaking-writing.html", "08-hometask.html",
]

reading_order = [ROOT / "front" / f for f in
                 ("01-cover.html", "02-title.html", "03-preface.html", "04-contents.html")]
for d in UNIT_DIRS:
    reading_order += [ROOT / "units" / d / f for f in UNIT_FILES]
reading_order += [ROOT / "back" / f for f in
                  ("answer-key.html", "glossary.html", "references.html", "lesson-plans.html",
                   "05-credits.html")]

missing = [p for p in reading_order if not p.exists()]
if missing:
    raise SystemExit("MISSING FILES:\n" + "\n".join(str(m) for m in missing))

def extract(path: Path) -> str:
    html = path.read_text(encoding="utf-8")
    # body inner content
    m = re.search(r"<body([^>]*)>(.*)</body>", html, re.S)
    if not m:
        raise SystemExit(f"No <body> in {path}")
    attrs, inner = m.group(1), m.group(2)
    # carry over any page-specific <style> from the head (cover/title layout)
    head_styles = "\n".join(re.findall(r"<style[^>]*>.*?</style>", html[:m.start()], re.S))
    # drop nav footers (their relative targets break in the merged file)
    inner = re.sub(r"<nav class=\"page-nav\".*?</nav>", "", inner, flags=re.S)
    # rewrite relative paths so they resolve from book/
    for pat, rep in (
        (r"\.\./\.\./shared/", "shared/"), (r"\.\./shared/", "shared/"),
        (r"\.\./\.\./assets/", "assets/"), (r"\.\./assets/", "assets/"),
        (r"\.\./\.\./front/", "front/"),   (r"\.\./front/", "front/"),
        (r"\.\./\.\./back/", "back/"),     (r"\.\./back/", "back/"),
        (r"\.\./\.\./units/", "units/"),   (r"\.\./units/", "units/"),
        (r"\.\./unit-", "units/unit-"),
    ):
        inner = re.sub(pat, rep, inner)
        head_styles = re.sub(pat, rep, head_styles)
    # prefix remaining same-directory links with the source dir
    prefix = str(path.parent.relative_to(ROOT)).replace("\\", "/") + "/"
    def _local(m):
        url = m.group(2)
        if re.match(r"^(?:shared/|assets/|front/|back/|units/|https?:|#|mailto:|data:)", url):
            return m.group(0)
        return f'{m.group(1)}="{prefix}{url}"'
    inner = re.sub(r'(href|src)="([^"]+)"', _local, inner)
    # preserve the unit gradient scope
    cm = re.search(r'class="([^"]*)"', attrs)
    cls = cm.group(1).strip() if cm else ""
    wrapped = f'<div class="{cls}">\n{head_styles}\n{inner}\n</div>' if cls or head_styles \
              else f"{head_styles}\n{inner}"
    return wrapped

parts = []
for path in reading_order:
    parts.append(f"<!-- ════ {path.relative_to(ROOT)} ════ -->")
    parts.append(extract(path))

doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>A Complete Guide to Tourism English — full book (print version)</title>
<link rel="stylesheet" href="shared/styles.css">
<style>
/* in the merged file every sheet breaks exactly once — the source pages are
   wrapped in unit-N divs, so the per-file :last-child suppression must not apply */
@media print {{
  .page, .page:last-child {{ page-break-after: always !important; break-after: page !important; }}
}}
</style>
</head>
<body>
{chr(10).join(parts)}
</body>
</html>
"""
out = ROOT / "all.html"
out.write_text(doc, encoding="utf-8")
pages = doc.count('class="page ') + doc.count('class="page"')
print(f"all.html written: {len(doc):,} bytes, {len(reading_order)} source files, {pages} .page sheets")
