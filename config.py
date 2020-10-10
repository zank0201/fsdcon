
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost/fsdcon"

class ProductionConfig(BaseConfig):
    DEBUG = False


class StagingConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
