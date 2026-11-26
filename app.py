import os

from flask import Flask, jsonify, render_template
import fscss

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    fscss.init_flask(app)

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/about")
    def about():
        return render_template("about.html")

    @app.get("/health")
    def health():
        return jsonify(status="ok", service=app.config["APP_NAME"])

    @app.errorhandler(404)
    def not_found(_error):
        return render_template("errors/404.html"), 404

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
