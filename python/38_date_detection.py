# Date detection program
import re


date_regex = re.compile(r"^(3[01]|[12][0-9]|[1-9])/(1[0-2]|0?[1-9])/[0-9]{4}$")
input_date = input()
match_object = date_regex.search(input_date)
if match_object != None:
    print("Valid date")
else:
    print("Invalid date")
