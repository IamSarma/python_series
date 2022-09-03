# Play 2048 game automatically
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Launch the game site
browser = webdriver.Firefox()
browser.get("https://play2048.co/")

# Simulate key up, right, down and left presses to play the game
