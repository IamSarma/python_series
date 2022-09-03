from selenium import webdriver

browser = webdriver.Firefox(
    executable_path=r"C:\Users\MB\Downloads\gecko\geckodriver.exe")

browser.get("https://inventwithpython.com")
