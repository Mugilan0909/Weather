import urllib.request
from flask import request

def post_weather():
    api='f0f57e3e4aad24a68928ff7d8c7b5994'
    lat = request.args.get('lat')
    lon=request.args.get('lon')
    source=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?lat=' + lat +'&lon=' + lon + '&appid='+ api ).read()

    return source