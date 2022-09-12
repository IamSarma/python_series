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
