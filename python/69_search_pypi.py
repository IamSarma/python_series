#! python3
# search_pypi.py
# Open several search results
import requests
import sys
import webbrowser
import bs4

# Display text while downloading the search result page
print("Searching...")
res = requests.get(
    "https://google.com/search?q=" "https://pypi.org/search/?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()


# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for each result
link_elems = soup.select(".eZt8xd")
num_open = min(5, len(link_elems))

for i in range(num_open):
    url_to_open = "https://www.pypi.org" + link_elems[i].get("href")
    print("Opening", url_to_open)
    webbrowser.open(url_to_open)
