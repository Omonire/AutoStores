# Flask + FSCSS boilerplate

A minimal Flask server with [FSCSS](https://fscss.devtem.org/) (Figured Shorthand CSS) compiled automatically into plain CSS.

## Stack

- Flask 3
- Jinja templates
- `fscss` Python wrapper (vendored Node compiler)
- Pytest smoke tests

## Requirements

- Python 3.10+
- Node.js 20+ on `PATH` (the FSCSS compiler runs through Node)

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python app.py
# or
flask --app app run --debug
```

Open http://127.0.0.1:5000.

## Structure

```
app.py                     app factory + routes
config.py                  configuration
templates/
  base.html                shared layout
  index.html               landing page
  about.html               second route demo
  errors/404.html          custom not-found page
static/src/
  style.fscss              FSCSS source
  style.css                generated (gitignored)
tests/test_app.py          route smoke tests
```

## How FSCSS is wired

`create_app()` calls `fscss.init_flask(app)`. On startup it compiles every `.fscss` file under `static/` into a sibling `.css` file. In debug mode, a watcher recompiles on changes. Browsers only receive the generated CSS, so production needs no FSCSS runtime.

Example from `style.fscss`:

```fscss
$accent: #8f6bff;

.btn {
  bg: $accent!;
  px: 20px;
  py: 12px;
  rounded: 12px;
}
```

## Routes

| Route | Description |
| --- | --- |
| `/` | Landing page |
| `/about` | Structure overview |
| `/health` | JSON health check |

## Tests

```bash
pytest
```
