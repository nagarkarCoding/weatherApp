from django.shortcuts import render

import requests
from django.shortcuts import render,redirect
from weatherApp.models import WeatherData
from django.conf import settings
from weatherApp.forms import WeatherSearchForm
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from aiohttp import ClientError, ClientSession

def display(request):
    return HttpResponse("Welcome to weather APP!")

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'
    #template = loader.get_template('login.html')
    #return HttpResponse(template.render())

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render

def login(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('search')

    return render(request, 'login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('login')

@csrf_protect
def fetch_weather_data(request):
    # set default city 
    #city = "delhi"
    if request.method == 'POST':
        city = request.POST['city']
        print("City selected :",city)

        api_key = settings.WEATHER_APP_API_KEY
        location_search_url  = 'http://dataservice.accuweather.com/locations/v1/cities/search'
        # Create a dictionary of query parameters
        params = {
            'q': city,
            'apikey': api_key,
        }

        # Make the API request
        try:
            resp = requests.get(location_search_url , params=params)

            data = resp.json()
            location_key = str(data[0]['Key'])
            current_conditions_url = f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}'

            # Create a dictionary of query parameters
            params = {
                'apikey': api_key, 
            }
            try:
                resp = requests.get(current_conditions_url, params=params)
                if resp.status_code == 200:
                    data = resp.json()

                    # Parse the JSON data
                    parsed_data = data

                    # Access the temperature details
                    temperature_metric = parsed_data[0]["Temperature"]["Metric"]
                    temperature_imperial = parsed_data[0]["Temperature"]["Imperial"]

                    # Access specific temperature values
                    temperature_value_celsius = temperature_metric["Value"]
                    temperature_value_fahrenheit = temperature_imperial["Value"]

                    # Access temperature units
                    temperature_unit_celsius = temperature_metric["Unit"]
                    temperature_unit_fahrenheit = temperature_imperial["Unit"]

                    weather_text = parsed_data[0]['WeatherText']

                    weather_data = WeatherData(city=city, temperature_value_celsius=temperature_value_celsius, 
                                            temperature_value_fahrenheit=temperature_value_fahrenheit, 
                                            temperature_unit_celsius=temperature_unit_celsius,
                                            temperature_unit_fahrenheit=temperature_unit_fahrenheit,
                                            weather_text=weather_text)
                    #weather_data.save()

                    # Print temperature details
                    print(f"Temperature (Celsius): {temperature_value_celsius} {temperature_unit_celsius}")
                    print(f"Temperature (Fahrenheit): {temperature_value_fahrenheit} {temperature_unit_fahrenheit}")
                    print(f"weatherText: {weather_text}")

                    context = {'city':city, 'temperature_value_celsius':temperature_value_celsius, 
                                            'temperature_value_fahrenheit':temperature_value_fahrenheit, 
                                            'temperature_unit_celsius':temperature_unit_celsius,
                                            'temperature_unit_fahrenheit':temperature_unit_fahrenheit,
                                            'weather_text':weather_text,
                                }

                    return render(request, 'results.html', context)
            except Exception as e:
                print(f"An error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    template = loader.get_template('search.html')
    return HttpResponse(template.render(request=request))