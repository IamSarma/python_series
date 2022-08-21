import re


# Substitution example
item_string = "12 drummers, 11 pipers, five rings, 3 hens"
num_regex = re.compile(r"\d+")
print(num_regex.sub("X", item_string))
