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
    comic_elem = soup.select("#comic img")
    if comic_elem == []:
        print("Couldn't find comic image")
    else:
        comic_url = "https:" + comic_elem[0].get("src")

    # Download the image
    print(f"Downloading image {comic_url}")
    res = requests.get(comic_url)
    res.raise_for_status()

    # Save the image to ./xkcd

    # Get the Prev button's URL

print("Done")
