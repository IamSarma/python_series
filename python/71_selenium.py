from selenium import webdriver
from selenium.webdriver.common.by import By

# Finding an element with class name
browser = webdriver.Firefox()
# browser.get("https://www.google.com")
# browser.maximize_window()
# try:
#     class_elem = browser.find_element(By.CLASS_NAME, "lnXdpd")
#     print(f"Found <{class_elem.tag_name}> element with that class name!")
# except:
#     print("Was not able to find an element with that name")


# Performing click operation
# browser.get("https://www.python.org")
# link_elem = browser.find_element(By.ID, "about")
# link_elem.location_once_scrolled_into_view
# link_elem.click()


# Filling out and submitting forms
browser.get("https://login.metafilter.com")
user_elem = browser.find_element(By.ID, "user_name")
user_elem.send_keys("test user")

password_elem = browser.find_element(By.ID, "user_pass")
password_elem.send_keys("test password")

password_elem.submit()
