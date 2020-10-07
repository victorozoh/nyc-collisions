import os

class Config(object):
    SECRET_KEY = os.urandom(24)
    POSTGRESQL_URI = os.environ['DATABASE_URL']
