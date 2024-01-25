# weather/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('currentweather/', views.current_weather, name='current_weather'),
     path('api/currentweather/', views.current_weather, name='api_current_weather'),
]
