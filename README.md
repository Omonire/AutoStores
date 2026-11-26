# AutoStore

A Flask + FSCSS + Motion marketplace landing page, deployable on Vercel.

AutoStore connects students, individual sellers and store owners with buyers in one central marketplace. Sellers list products with images, descriptions, prices and categories; buyers browse, search, filter and contact sellers.

## Stack

- Flask 3, detected by Vercel as a Python/Flask deployment
- Jinja templates
- FSCSS as the complete visual system, compiled via `build.py`
- Motion vanilla JS for Framer-style reveals, parallax, counters and tilt
- Google Fonts: Playfair Display + Manrope
- Pytest smoke tests

## Requirements

- Python 3.10+
- Node.js 20+ on `PATH` for local FSCSS compilation
- Internet access for Google Fonts and Motion CDN

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python build.py
python app.py
# or
flask --app app run --debug
```

Open http://127.0.0.1:5000. `create_app()` also calls `build.py` automatically when `VERCEL` is not set, so the manual build step is only needed before a static inspect.

## Structure

```
app.py                     Flask app factory + routes
build.py                   compiles FSCSS and copies Motion JS into public/
config.py                  configuration
PROMPT.md                  AI prompt for the landing page brief
vercel.json                Vercel build command + function config
templates/
  base.html                shared layout + font/CSS/JS links
  index.html               premium AutoStore landing page
  about.html               vision + MVP scope
  errors/404.html          custom not-found page
static/src/
  style.fscss              complete FSCSS design system
static/js/
  main.js                  Motion source
public/
  style.css                generated from FSCSS (gitignored)
  main.js                  generated copy of Motion source (gitignored)
  og-image.html            source design for the home link preview
  og-image.png             1200x630 home social preview
  og-about.html            source design for the about link preview
  og-about.png             1200x630 about social preview
  favicon.svg              brand favicon
tests/test_app.py          route smoke tests
```

## How FSCSS is wired

`build.py` compiles `static/src/style.fscss` to `public/style.css` and copies `static/js/main.js` to `public/main.js`. Templates request `/style.css` and `/main.js`, which works locally through Flask's static folder and on Vercel through the `public/` CDN.

On Vercel, `vercel.json` runs `python build.py` after dependencies install. The Flask runtime skips compilation because Vercel sets `VERCEL=1`, so Node is only needed at build time.

Example from `style.fscss`:

```fscss
$accent: #f68b1e;

.btn-primary {
  background: linear-gradient(120deg, $accent, #ffb13b);
  border-radius: 999px;
  px: 28px;
  py: 14px;
}
```

## Deploy to Vercel

```bash
npm i -g vercel
vercel login
vercel deploy --prod
```

The CLI is already authenticated in this workspace. `vercel.json` handles the build command, so no dashboard configuration is required.

## Social previews

`templates/base.html` emits canonical, Open Graph, Twitter Card, JSON-LD and favicon metadata. Child templates override the copy; `about.html` points to its own preview image.

The 1200x630 PNGs are generated from the matching HTML designs in `public/`. Regenerate with Edge or Chrome:

```bash
msedge --headless=new --window-size=1200,630 --screenshot=public/og-image.png "file:///path/to/AutoStores/public/og-image.html"
msedge --headless=new --window-size=1200,630 --screenshot=public/og-about.png "file:///path/to/AutoStores/public/og-about.html"
```

Deployed preview assets are served at `https://autostores.vercel.app/og-image.png` and `https://autostores.vercel.app/og-about.png`.

## Motion interactions

- Hero elements cascade in with blur and vertical motion.
- Sections reveal as they enter the viewport.
- Stats count up on scroll.
- Listing cards tilt subtly with the pointer.
- Buttons have a small magnetic pull.
- All movement is disabled under `prefers-reduced-motion: reduce`.

## Routes

| Route | Description |
| --- | --- |
| `/` | AutoStore landing page |
| `/about` | Vision and MVP scope |
| `/health` | JSON health check |

## Tests

```bash
pytest
```
