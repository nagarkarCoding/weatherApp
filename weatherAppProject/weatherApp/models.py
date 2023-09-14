from django.db import models

# Create your models here.
from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=200)
    temperature_value_celsius = models.FloatField()
    temperature_value_fahrenheit = models.FloatField()
    temperature_unit_celsius = models.CharField(max_length=1)
    temperature_unit_fahrenheit = models.CharField(max_length=1)    
    weather_text = models.CharField(max_length=100)