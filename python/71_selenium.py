from selenium import webdriver
from selenium.webdriver.common.by import By

# Finding an element with class name
browser = webdriver.Firefox()
browser.get("https://www.google.com")
try:
    class_elem = browser.find_element(By.CLASS_NAME, "lnXdpd")
    print(f"Found <{class_elem.tag_name}> element with that class name!")
except:
    print("Was not able to find an element with that name")
