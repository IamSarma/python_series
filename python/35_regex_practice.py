# Example(s) of regex use cases
# Identifying valid phone number
import re

# Basic phone number search
phonenum_regex_1 = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
match_object_1 = phonenum_regex_1.search("My number is 123-456-7788")
print(f"Phone number found: {match_object_1.group()}")


# Validation of phone number containing paranthesis
# also helpful to extract country code and number separately
# escape the backslash using "\(and\)"
phonenum_regex_2 = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
match_object_2 = phonenum_regex_2.search("My number is (123) 456-7890")
print(f"Country code found : {match_object_2.group(1)}")
print(f"Phone number found : {match_object_2.group(2)}")


# Matching multiple groups with Pipe
hero_regex = re.compile(r"Batman|Tina Fey")
match_object_3 = hero_regex.search("Batman and Tina Fey")
print(match_object_3.group())

match_object_4 = hero_regex.search("Tina Fey and Batman")
print(match_object_4.group())
