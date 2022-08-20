# Example(s) of regex use cases
# Identifying valid phone number
import re

# Basic phone number search
phonenum_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
match_object = phonenum_regex.search("My number is 123-456-7788")
print(f"Found number found: {match_object.group()}")
