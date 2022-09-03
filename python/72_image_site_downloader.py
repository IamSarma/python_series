# Program that goes to a photo-sharing site
# Searches for categories of photos
# Downloads all the resulting images
import sys
import os
import requests
import bs4

# Create a local folder to save the downloaded photos
os.makedirs("photos", exist_ok=True)

# Generate target url
url = "https://unsplash.com/s/photos/" + " ".join(sys.argv[1:])
