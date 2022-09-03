#! python3
# download_xkcd.py
# Downloads every single XKCD comic
import requests
import os
import bs4

url = "https://www.xkcd.com"
os.makedirs("xkcd", exist_ok=True)

while not url.endswith("#"):
    # Download the page
    print(f"Downloading the page {url}")
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Find the URL of the comic image

    # Download the image

    # Save the image to ./xkcd

    # Get the Prev button's URL

print("Done")
