from flask import Flask

from app.config import get_config
from .database import init_db
from .error_handler import setup_error_handler
from .loggin_config import setup_logging


def create_app(config_name):
    app = Flask(__name__)
    config = get_config(config_name)
    app.config.from_object(config)
    init_db(app)
    setup_logging(app)
    setup_error_handler(app)

    from app.routes.user_routes import user_blueprint

    register_blueprints(app, [user_blueprint])

    return app


def register_blueprints(app, blueprints):
    for bp in blueprints:
        url_prefix = f"/api/{bp.url_prefix}" if bp.url_prefix else "/api"
        app.register_blueprint(bp, url_prefix=url_prefix)
