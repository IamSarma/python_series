# Program that goes to a photo-sharing site
# Searches for categories of photos
# Downloads all the resulting images
from selenium import webdriver
import sys

# Open the site and search for the category
browser = webdriver.Firefox()
browser.get("https://unsplash.com/s/photos/" + " ".join(sys.argv[1:]))
