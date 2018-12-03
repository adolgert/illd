"""This is the main that starts the web server."""
import logging
import os
from pathlib import Path

from flask import Flask, render_template
from illd import db, natural

LOGGER = logging.getLogger(__name__)


def create_app(test_configuration=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=f"dev",
        DATABASE=os.path.join(app.instance_path, f"illd.sqlite")
    )

    if test_configuration is None:
        app.config.from_pyfile(f"config.py", silent=True)
    else:
        app.config.from_mapping(test_configuration)

    try:
        Path(app.instance_path).mkdir(parents=True, exist_ok=True)
        LOGGER.warning(f"app instance is {app.instance_path}")
    except OSError:
        LOGGER.warning(f"Failed to create path {app.instance_path}")

    @app.route(f"/hello")
    def index():
        return f"Base directory"

    db.init_app(app)
    app.register_blueprint(natural.NATURAL_BP)
    #app.add_url_rule("/", endpoint="natural.natural")

    return app


def entry():
    create_app()


if __name__ == "__main__":
    entry()
