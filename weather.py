#  API SOURCE : https://openweathermap.org/api
import requests
import pygame
from gtts import gTTS
from geopy.geocoders import Nominatim
from datetime import datetime

def talk(Command):
    tts = gTTS(Command, lang="te")
    tts.save("weather.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("weather.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

def get_location():
    try:
        # Using the freegeoip.app API to get IP-based location
        response = requests.get("https://freegeoip.app/json/") # this will take your ip adderess and get your location well it is accurate i am working on it.
        location_info = response.json()
        city = location_info.get("city", "")
        return city
    except Exception as e:
        print(f"Error getting location: {e}")
        return None
def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {"q": city, "appid": api_key, "units": "metric"}

    # Get current weather
    response = requests.get(base_url, params=params)
    data = response.json()

    # Get forecast data
    forecast_params = {"q": city, "appid": api_key, "units": "metric", "cnt": 5 * 8}  # 5 days * 8 timestamps per day
    forecast_response = requests.get(forecast_url, params=forecast_params)
    forecast_data = forecast_response.json()

    if response.status_code == 200 and forecast_response.status_code == 200:
        # Current weather
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = int(data["wind"]["speed"])

        print(f"{city} లో ప్రస్తుత వాతావరణ వివరాలు:\nDescription: {weather_description}\nఉష్ణోగ్రత: {temperature}°C\nతేమ శాతం: {humidity}%\nగాలి వేగం: {wind_speed} meter per second")
        talk(f"{city} లో ప్రస్తుత వాతావరణ వివరాలు:\nDescription: {weather_description}\nఉష్ణోగ్రత: {temperature}°C\nతేమ శాతం: {humidity}%\nగాలి వేగం: {wind_speed} meter per second")

        # Forecast well this is 5 day forcast and it is not sorted well and annoying when it is printed you can include them if you want
        # print("5-Day Forecast:")
        # for forecast in forecast_data["list"]:
        #     forecast_date = datetime.strptime(forecast["dt_txt"], "%Y-%m-%d %H:%M:%S")
        #     forecast_time = forecast_date.strftime("%I:%M %p")
        #     forecast_weather = forecast["weather"][0]["description"]
        #     forecast_temp = forecast["main"]["temp"]
        #     # talk("here is the weather forcast for 5 days")
        #     print(f"Time: {forecast_time}, Weather: {forecast_weather}, Temperature: {forecast_temp}°C")
        #     # talk(f"Time: {forecast_time}, Weather: {forecast_weather}, Temperature: {forecast_temp}°C")

    else:
        print(f"Error retrieving weather data: {data.get('message', '')}")
        talk(f"Error retrieving weather data: {data.get('message', '')}")

# Example usage
api_key = "u r api key here"
user_city = get_location()

if user_city:
    get_weather(api_key, user_city)
else:
    print("Unable to determine location.")
