#! python3
# threaded_download_xkcd.py
# Downloads XKCD comics using multiple threads
import requests
import os
import bs4
import threading

url = "https://www.xkcd.com"
os.makedirs("xkcd", exist_ok=True)


def downloadXkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # Download the page
        print(f"Downloading the page {url}/{url_number}")
        res = requests.get(f"{url}/{url_number}")
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
        image_file = open(os.path.join("xkcd", os.path.basename(comic_url)), "wb")

        for chunk in res.iter_content(100000):
            image_file.write(chunk)

        image_file.close()

        # Create and start the thread object(s)
    
        # Wait for all threads to end
