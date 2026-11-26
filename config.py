import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-change-me")
    APP_NAME = "Flask + FSCSS boilerplate"
    TEMPLATES_AUTO_RELOAD = True
