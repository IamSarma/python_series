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

# Load JSON data into a Python variable
weather_data = json.loads(response.text)

# Print weather data
w = weather_data["List"]
print(f"Current weather in {location}")
print(w[0]["weather"][0]["main"], "-", w[0]["weather"][0]["description"])
print()

print("Tomorrow:")
print(w[1]["weather"][0]["main"], "-", w[1]["weather"][0]["description"])
print()

print("Day after tomorrow:")
print(w[2]["weather"][0]["main"], "-", w[2]["weather"][0]["description"])
