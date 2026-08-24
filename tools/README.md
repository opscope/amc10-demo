# Build tools

Static site generators for the AMC 10 demo and crash course. Run from the
repo root: `python3 tools/build_algebra.py`, `python3 tools/build_practice_pdf.py`.

## Naming convention (project rule)

- All file and folder names are **native English, kebab-case** (`practice-test.pdf`,
  `diagnostics.html`, `course/`). No transliterated Russian in names.
- When a page or asset exists in two languages, the **English file takes the
  clean name** and the Russian file takes the same name with the `-ru` suffix:
  `algebra.html` (EN) / `algebra-ru.html` (RU), `algebra-test.pdf` /
  `algebra-test-ru.pdf`.
- Pages that currently exist only in Russian still get clean English names
  (`diagnostics.html`); when an English version appears, it takes over the
  clean name and the Russian page moves to `-ru`.
- Python sources use snake_case with the same base words (`algebra_data_a.py`,
  `build_algebra.py`).
- Old URLs that were ever published must keep working: leave a redirect stub
  at the old path (see `kurs/*.html`).
- **Index exception**: the two landing pages (`index.html`, `course/index.html`)
  stay Russian at their clean, already-published URLs; their English mirrors are
  `index-en.html` and `course/index-en.html`.
- **Bilingual invariant**: every page has a version in both languages; navigation
  never switches language (RU pages link only to RU pages, EN to EN); the only
  cross-language link is the switcher marked `class="langlink"` that points to
  the same page in the other language. The feedback form posts a `lang` field
  and the worker redirects to the matching thanks page.

## Files

- `algebra_data_{a,b,c}.py` — Block 1 lesson/test content, RU+EN, single source.
- `build_algebra.py` — builds `course/algebra-ru.html`, `course/algebra.html`,
  and the four algebra PDFs.
- `build_practice_pdf.py` — builds the printable practice test PDFs (RU/EN)
  from the problems on the overview page (`index.html`).
- `course-style.css`, `course-index-body.html` — master styles and landing body.

Future blocks (geometry, number theory, counting, strategy) follow the same
pattern: `geometry_data_*.py` → `build_geometry.py` → `course/geometry-ru.html`,
`course/geometry.html`, `course/geometry-*.pdf`.
