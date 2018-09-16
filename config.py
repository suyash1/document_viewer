import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class StagingConfig(Config):
    DEBUG = True


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'some secret key, needs to be fixed'
    SESSION_TYPE = 'filesystem'
    UPLOAD_FOLDER = '/tmp/file_uploads'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'json'])


class TestingConfig(Config):
    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
