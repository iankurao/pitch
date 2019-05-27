import  os

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://ian:vionashina@localhost/pitch_test'
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://ian:vionashina@localhost/pitch'
    DEBUG=True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


config_options={
'development':DevConfig,
"production":ProdConfig,
'test':TestConfig
}
