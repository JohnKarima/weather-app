import os
import cloudinary

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://qwan:123@localhost/weather'
    WEATHER_API_BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')  
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    cloudinary.config(cloud_name='diwegz7cy', api_key='282176251245691', api_secret='SLIaeAnl4obqx49FYx9FhUbTFxU')



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
