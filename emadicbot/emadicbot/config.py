import os

class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = os.urandom(12)
    DATABASE_URL = os.getenv('DATABASE_URL', '').replace('postgres:', 'postgresql:')
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', 50 * 1024 * 1024))    # 50 Mb limit
    REDIS_URL = os.getenv('REDIS_URL')

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False