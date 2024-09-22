from flask import Flask
from flask_injector import FlaskInjector
from injector import singleton, Module, Binder
from mongoengine import connect

from app.config import get_config
from app.error_handler import setup_error_handler
from app.logging_config import setup_logging
from app.repositories.user_repository import UserRepository
from app.routes.user_routes import user_blueprint
from app.services.user_service import UserService


class AppModule(Module):
    def configure(self, binder: Binder):
        binder.bind(UserService, to=UserService, scope=singleton)
        binder.bind(UserRepository, to=UserRepository, scope=singleton)


def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.config.from_object(get_config())
    connect(app.config.get("MONGO_DB_NAME"), host=app.config.get("MONGO_URI"))
    register_blueprints(app, [user_blueprint])
    setup_logging(app)
    setup_error_handler(app)
    FlaskInjector(app=app, modules=[AppModule()])
    return app


def register_blueprints(app, blueprints) -> None:
    for bp in blueprints:
        url_prefix = f"/api/{bp.url_prefix}" if bp.url_prefix else "/api"
        app.register_blueprint(bp, url_prefix=url_prefix)


__all__ = ["create_app"]
