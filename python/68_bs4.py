import requests
import bs4

# Creating a beautiful soup object from HTML
# res = requests.get("https://nostarch.com")
# res.raise_for_status()
# no_starch_soup = bs4.BeautifulSoup(res.text, "html.parser")
# print(type(no_starch_soup))


# Using example HTML file
example_file = open("example.html")
example_soup = bs4.BeautifulSoup(example_file.read(), "html.parser")
# print(type(example_soup))

# Extracting author details
elems = example_soup.select("#author")
# print(type(elems))
# print(len(elems))
# print(type(elems[0]))
# print(str(elems[0]))
# print(elems[0].getText())
# print(elems[0].attrs)

# Extracting all the <p> elements
p_elems = example_soup.select("p")
print(str(p_elems[0]))
print(str(p_elems[1]))
print(str(p_elems[2]))
print(p_elems[0].getText())
print(p_elems[1].getText())
print(p_elems[2].getText())
