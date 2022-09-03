# Play 2048 game automatically
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Launch the game site
browser = webdriver.Firefox()
browser.get("https://play2048.co/")

# Simulate key up, right, down and left presses to play the game
html_elem = browser.find_element(By.TAG_NAME, "html")
browser.implicitly_wait(3)

for i in range(101):
    html_elem.send_keys(Keys.UP)
    browser.implicitly_wait(1)
    html_elem.send_keys(Keys.RIGHT)
    browser.implicitly_wait(1)
    html_elem.send_keys(Keys.DOWN)
    browser.implicitly_wait(1)
    html_elem.send_keys(Keys.LEFT)
    browser.implicitly_wait(1)
