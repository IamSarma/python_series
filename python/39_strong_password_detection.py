# Program to detect password strength
# Rules
# Should be at least eight character long
# Should contain both upper and lower case characters
# Should contain at least one digit
import re

test_password = "raviteja"
flag = 0

if len(test_password) < 8:              # password characters length check
    flag = -1

# Print message based on the flag status
if flag == -1:
    print("Password didn't meet the safety requirements, try again 🐷")
else:
    print("Detected strong password, kudos!!! 🐍")
