from django.apps import AppConfig

from django.conf import settings
import requests

class WeatherappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weatherApp'