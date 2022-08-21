# Simulating strip() functionality using regex
# whitespaces to be removed from the beginning and end of the string
# if second argument is passed then those characters to be removed from the string
import re


def regex_strip(test_string, opt_arg=""):
    if not opt_arg:
        return re.sub(r" ", "", test_string)


test_string = "   python   "
print(regex_strip(test_string))
