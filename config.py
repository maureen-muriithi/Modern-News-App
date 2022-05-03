import os

class Config:               #The main configuration class
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):   #Applies during production, inherits from class config also
    pass

class DevConfig(Config):    #Applies during production, inherits from class config also
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}