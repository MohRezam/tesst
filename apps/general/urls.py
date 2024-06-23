from django.urls import path
from . import views

urlpatterns = [
    path("weather/full/", views.WeatherAPIView.as_view(), name="weather_api"),
]
