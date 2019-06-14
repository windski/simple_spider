#!/usr/bin/env python3


import os
from connectdb import db_path
base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"

    @staticmethod
    def init_app(self):
        pass


class DevelopmentConfig(Config):
    Debug = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_path


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
