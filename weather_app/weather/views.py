# weather/views.py
from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    return render(request, 'index.html')

def current_weather(request):
    city = request.POST.get('city', 'DefaultCity')  # Default city if not provided
    unit = request.POST.get('unit', 'metric')  # Default unit if not provided

    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = 'YOUR_API_KEY'
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&lang=ru&appid={api_key}'

    response = requests.get(api_url)
    weather_data = response.json()

    context = {
        'city_name': weather_data['name'],
        'temperature': weather_data['main']['temp'],
        'unit_of_measurement': unit,
        'weather_description': weather_data['weather'][0]['description'],
    }

    return render(request, 'current_weather.html', context)



def current_weather(request):
    city = request.POST.get('city', 'DefaultCity')  # Default city if not provided
    unit = request.POST.get('unit', 'metric')  # Default unit if not provided

    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = 'YOUR_API_KEY'
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&lang=ru&appid={api_key}'

    response = requests.get(api_url)
    weather_data = response.json()

    api_response = {
        'city_name': weather_data['name'],
        'temperature': weather_data['main']['temp'],
        'unit_of_measurement': unit,
        'weather_description': weather_data['weather'][0]['description'],
    }

    return JsonResponse(api_response)
