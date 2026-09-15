# cigartale.app

Static site for CigarTale, served by GitHub Pages at https://cigartale.app (CNAME in this repository; DNS at GoDaddy).

Pages: `index.html` (English landing), `ru/index.html` (Russian landing), `privacy.html`, `terms.html`, `support.html`, `404.html`.

The HTML is generated: edit `tools/legal.py` (shared CSS, page shell, legal and support texts) or `tools/landing.py` (landing copy in both languages; the story list is read from the app repository's `scripts/catalog/dubai-pilot.json`, path at the top of the file), then run from the repository root:

```sh
python3 tools/legal.py && python3 tools/landing.py
```

Commit the regenerated HTML together with the tool change. No build step runs on GitHub; Pages serves the files as committed.
