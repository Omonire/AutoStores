# STEP 1: Build the browser assets once so Vercel never needs Node at runtime.
from pathlib import Path
import shutil

# STEP 2: fscss is still the source of truth; build.py just compiles it early.
import fscss

ROOT = Path(__file__).resolve().parent
FSCSS_SOURCE = ROOT / "static" / "src" / "style.fscss"
JS_SOURCE = ROOT / "static" / "js" / "main.js"
PUBLIC_DIR = ROOT / "public"


# STEP 3: Compile FSCSS to public/style.css and copy Motion JS to public/main.js.
def build_assets():
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    css_output = fscss.compile_file(FSCSS_SOURCE, PUBLIC_DIR / "style.css")
    shutil.copyfile(JS_SOURCE, PUBLIC_DIR / "main.js")
    return css_output


# STEP 4: Vercel's buildCommand runs this file directly.
if __name__ == "__main__":
    print(build_assets())
