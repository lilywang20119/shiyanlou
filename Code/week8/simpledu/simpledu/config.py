
class BaseConfig(object):
    """config base class"""
    SECRET_KEY = 'makesure to set a very secret key'

class DevelopmentConfig(BaseConfig):
    """development config"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8'

class ProductionConfig(BaseConfig):
    """production config"""
    pass

class TestingConfig(BaseConfig):
    """test config"""
    pass

configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing':TestingConfig
}