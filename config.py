# STEP 1: os.getenv lets us read deployment settings without hardcoding them.
import os


# STEP 2: One config class is enough for a starter; add subclasses as the app grows.
class Config:
    # STEP 2.1: Secret key comes from the environment, with a safe dev-only fallback.
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-change-me")

    # STEP 2.2: APP_NAME is reused in templates and the /health JSON response.
    APP_NAME = "AutoStore"

    # STEP 2.3: Reload templates while developing so edits show up immediately.
    TEMPLATES_AUTO_RELOAD = True
