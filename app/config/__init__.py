import os
from typing import Type

DEFAULT_ENVIRONMENT = "dev"


class Config:
    DEBUG = False
    TESTING = False
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
    LOG_LEVEL = "INFO"


class DevelopmentConfig(Config):
    DEBUG = False
    LOG_LEVEL = "DEBUG"


class ProductionConfig(Config):
    LOG_LEVEL = "ERROR"


class TestingConfig(Config):
    TESTING = True
    LOG_LEVEL = "DEBUG"


config = {"prod": ProductionConfig, "dev": DevelopmentConfig, "test": TestingConfig}


def get_config() -> (
        Type[ProductionConfig] | Type[DevelopmentConfig] | Type[TestingConfig]
):
    return config.get(os.getenv("FLASK_ENV", DEFAULT_ENVIRONMENT))
