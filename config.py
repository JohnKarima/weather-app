import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://qwan:123@localhost/weather'
    WEATHER_API_BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
    cloud_name = os.environ.get('CLOUD_NAME')
    api_key_cloud = os.environ.get('CLOUD_API_KEY')
    api_secret_cloud = os.environ.get('CLOUD_API_SECRET')
    secure = True

    CLOUD_NAME='dccpekr5r'
    CLOUD_API_KEY='383943634483382'
    CLOUD_API_SECRET='vKtoKMDMMvW5PFp6nhQzlV8CvOA'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass



class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
