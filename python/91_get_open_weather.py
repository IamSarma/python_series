#! python3
# get_open_weather.py
# Prints the weather for a location from the command line
import sys
import requests
import json

APPID = "YOUR_APPID_HERE"

# Compute location from command line arguments
if len(sys.argv) < 2:
    print("Usage: get_open_weather.py city_name, two_letter_country_code")
    sys.exit()

location = " ".join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={APPID}"
response = requests.get(weather_url)
response.raise_for_status()

# Load JSON data into a Python variable
weather_data = json.loads(response.text)

# Print weather data
w = weather_data["weather"]
print("Weather today:")
print(w[0]["main"], "-", w[0]["description"])
