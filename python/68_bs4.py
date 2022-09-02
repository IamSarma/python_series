import requests
import bs4

# Creating a beautiful soup object from HTML
res = requests.get("https://nostarch.com")
res.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(no_starch_soup))
