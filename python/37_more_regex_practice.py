import re


# Substitution example
item_string = "12 drummers, 11 pipers, five rings, 3 hens"
num_regex = re.compile(r"\d+")
print(num_regex.sub("X", item_string))


# Regex that matches a number with commas for every 3 digits
num_string = "1234"
comma_regex = re.compile(r"^\d{1,2}(,\d{3})*$")
match_object_1 = comma_regex.search(num_string)
print(match_object_1 != None)
