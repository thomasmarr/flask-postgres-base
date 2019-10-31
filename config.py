import os


class Config:
    """
    Set default config values here
    e.g. CONFIG_VALUE = os.environ.get('CONFIG_VALUE_ENV_VAR') or 'default value'
    """

    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevConfig(Config):
    """
    Set dev specific config here
    """

    DEBUG = True


class TestConfig(Config):
    """
    Set test specific config here
    """

    TESTING = True


class ProdConfig(Config):
    """
    Set prod specific config here
    """


config = {
    "dev": DevConfig,
    "test": TestConfig,
    "prod": ProdConfig,
    "default": ProdConfig,
}
