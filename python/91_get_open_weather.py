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
weather_url = f"http://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3&APPID={APPID}"
response = requests.get(weather_url)
response.raise_for_status()
