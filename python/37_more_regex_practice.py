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


# Regex that matches full name of someone whose last name is Watanabe
# First name's first letter should be capitalized
# Preceding word shouldn't contain a nonletter character
# First name should exist
# First character of last name should be capitalized
full_name = "Haruto Watanabe"
first_name_regex = re.compile(r"^[A-Z]\w+ Watanabe")
match_object_2 = first_name_regex.search(full_name)
if match_object_2 != None:
    print(match_object_2.group())
else:
    print(match_object_2 != None)


# Regex that matches a sentence
# where the first word is either Alice, Bob or Carol
# where the second word is either eats, pets or throws
# where the thrid word is eithe apples, cats or baseballs
# and the sentecne ends with a period
# regex should be case-insensitive
input_sentence = "Alice throws apples."
sentence_regex = re.compile(
    r"^(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.$", re.I)
match_object_3 = sentence_regex.search(input_sentence)
if match_object_3 != None:
    print(match_object_3.group())
else:
    print(match_object_3 != None)
