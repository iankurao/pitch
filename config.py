import os

class Config:
    '''
    General configuration parent class
    '''
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY='123'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://ian:vionashina@localhost/pitch_test'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ian:vionashina@localhost/pitch'

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
