# Date detection program
import re


date_regex = re.compile(r"\b(1|31)\b/\b(1|12)\b")
input_date = input()
match_object = date_regex.search(input_date)
if match_object != None:
    print(match_object.group())
else:
    print("Invalid number")
