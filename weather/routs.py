from flask import Blueprint
from .controller import post_weather


weather_bp = Blueprint('weather_bp',__name__)

@weather_bp.route('/weather',methods=['GET'])
def weather():
    return post_weather()