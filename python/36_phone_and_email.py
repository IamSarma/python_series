#! python3
# phone_and_email.py
# Finds phone numbers and email addresses on the clipboard
import re

# Phone number regex
phone_regex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?                  # area code
    (\s|-|\.)?                          # separator
    (\d{3})                             # first 3 digits
    (\s|-|\.)                           # separator
    (\d{4})                             # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
)""", re.VERBOSE)


# Email regex

# Find matches in clipboard tex

# Copy results to the clipboard
