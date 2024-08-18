from typing import Dict

from flask import Flask
from injector import singleton, Module, Injector, Binder

from app.config import get_config
from app.database.mongo_database import MongoDatabase
from app.error_handler import setup_error_handler
from app.logging_config import setup_logging
from app.repositories.user_repository import UserRepository
from app.routes.user_routes import user_blueprint
from app.services.user_service import UserService


class AppModule(Module):
    __config: Dict

    def __init__(self, config_input: Dict):
        self.__config = config_input

    def configure(self, binder: Binder, **kwargs):
        binder.bind(
            MongoDatabase,
            to=MongoDatabase(self.__config.get("URI"), self.__config.get("DB_NAME")),
            scope=singleton,
        )
        binder.bind(UserService, to=UserService, scope=singleton)
        binder.bind(UserRepository, to=UserRepository, scope=singleton)


def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.config.from_object(get_config())
    app.config["INJECTOR"]: Injector = Injector(
        AppModule(
            {
                "URI": app.config["MONGO_URI"],
                "DB_NAME": app.config["MONGO_DB_NAME"],
            }
        )
    )
    setup_logging(app)
    setup_error_handler(app)

    register_blueprints(app, [user_blueprint])

    return app


def register_blueprints(app, blueprints) -> None:
    for bp in blueprints:
        url_prefix = f"/api/{bp.url_prefix}" if bp.url_prefix else "/api"
        app.register_blueprint(bp, url_prefix=url_prefix)
