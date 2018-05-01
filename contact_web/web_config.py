class Config(object):
    DEBUG = False
    TESTING = False
    API_URL = "http://api_url:5008"
    CONTACT_URI = "/contact-api/contacts"
    SECRET_KEY = "mykey"

class ProductionConfig(Config):
    API_URL = "http://api_product_url:5008"


class DevelopmentConfig(Config):
    DEBUG = True
    API_URL = "http://127.0.0.1:5008"


class TestingConfig(Config):
    TESTING = True


config = {
    "product": "web_config.ProductionConfig",
    "development": "web_config.DevelopmentConfig",
    "testing": "web_config.TestingConfig",
    "default": "web_config.DevelopmentConfig"
}