# STEP 1: Read the PORT environment variable when running the dev server.
import os

# STEP 2: Import Flask helpers: the app object, JSON responses, and template rendering.
from flask import Flask, jsonify, render_template

# STEP 3: Import our own settings class from config.py.
from config import Config


# STEP 5: Build the app inside a factory so tests can create fresh instances.
def create_app(config_class=Config):
    # STEP 5.1: Serve CSS and JS from public/ so Vercel can cache them on the CDN.
    app = Flask(__name__, static_folder="public", static_url_path="")

    # STEP 5.2: Copy settings from the config class into app.config.
    app.config.from_object(config_class)

    # STEP 5.3: Locally compile FSCSS into public/style.css before serving.
    # On Vercel the build command already did this, so runtime skips Node.
    if not os.getenv("VERCEL"):
        from build import build_assets

        build_assets()

    # STEP 6: Home route renders the landing page template.
    @app.get("/")
    def index():
        # STEP 6.1: Jinja fills in the blocks defined in templates/index.html.
        return render_template("index.html")

    # STEP 7: About route renders the second page to prove routing works.
    @app.get("/about")
    def about():
        # STEP 7.1: Same base layout, different content block.
        return render_template("about.html")

    # STEP 8: Health route returns machine-readable JSON for monitoring.
    @app.get("/health")
    def health():
        # STEP 8.1: Read APP_NAME from config so the response matches deployment.
        return jsonify(status="ok", service=app.config["APP_NAME"])

    # STEP 9: Custom 404 handler keeps errors inside the same design system.
    @app.errorhandler(404)
    def not_found(_error):
        # STEP 9.1: Return the template AND the correct HTTP status code.
        return render_template("errors/404.html"), 404

    # STEP 10: Hand the configured app back to the caller.
    return app


# STEP 11: Create a module-level app so "flask --app app run" finds it.
app = create_app()


# STEP 12: Allow "python app.py" to start the development server directly.
if __name__ == "__main__":
    # STEP 12.1: Bind to all interfaces and use PORT or default to 5000.
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
