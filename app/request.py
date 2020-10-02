import urllib.request, json
from .models import City
import requests

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ city }&units=metric&appid=784580038401b570ded56b3166db5511'
    r = requests.get(url).json()
    return r