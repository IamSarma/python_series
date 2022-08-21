#! python3
# phone_and_email.py
# Finds phone numbers and email addresses on the clipboard
import re
import pyperclip


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
# This regex won't match every possible email address
# however, it will match almost any typical email address
email_regex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+                   # username
    @                                   # @ symbol
    [a-zA-Z0-9.-]+                      # domain name
    (\.[a-zA-Z]{2,4})                   # dot-something
)""", re.VERBOSE)


# Get text from the clipboard
text = str(pyperclip.paste())

# Find matches in the text
matches = []
# Phone number match
for groups in phone_regex.findall(text):
    phone_num = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phone_num += " x" + groups[8]
        matches.append(phone_num)
# Email address match
for groups in email_regex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard
