# Example(s) of regex use cases
# Identifying valid phone number
import re

# Basic phone number search
phonenum_regex_1 = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
match_object_1 = phonenum_regex_1.search("My number is 123-456-7788")
print(f"Phone number found: {match_object_1.group()}")


# Validation of phone number containing paranthesis
# also helpful to extract country code and number separately
phonenum_regex_2 = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
match_object_2 = phonenum_regex_2.search("My number is (123) 456-7890")
print(f"Country code found : {match_object_2.group(1)}")
print(f"Phone number found : {match_object_2.group(2)}")
