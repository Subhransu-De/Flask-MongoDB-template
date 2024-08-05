import os

from dotenv import load_dotenv

load_dotenv()


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


def get_config(config_name=None):
    if config_name is None:
        config_name = os.getenv("FLASK_ENV", "dev")
    return config.get(config_name, config["dev"])
