from distutils.debug import DEBUG


class Config:               #The main configuration class
    pass
class ProdConfig(Config):   #Applies during production, inherits from class config also
    pass
class DevConfig(Config):    #Applies during production, inherits from class config also
    DEBUG = True