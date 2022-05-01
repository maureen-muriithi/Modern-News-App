


class Config:               #The main configuration class
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}'

class ProdConfig(Config):   #Applies during production, inherits from class config also
    pass

class DevConfig(Config):    #Applies during production, inherits from class config also
    DEBUG = True