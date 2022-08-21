# Program to detect password strength
# Rules
# Should be at least eight character long
# Should contain both upper and lower case characters
# Should contain at least one digit
# Should contain at least one character form _,@ or $
# Should not contain any space(s)
import re

test_password = "R@vit3ja"
flag = 0

if len(test_password) < 8:
    flag = -1
elif not re.search(r"[a-z]", test_password):
    flag = -1
elif not re.search(r"[A-Z]", test_password):
    flag = -1
elif not re.search(r"[0-9]", test_password):
    flag = -1
elif not re.search(r"[_@$]", test_password):
    flag = -1

# Print message based on the flag status
if flag == -1:
    print("Password didn't meet the safety requirements, try again 🐷")
else:
    print("Detected strong password, kudos!!! 🐍")
