# Function to check if the input string matches phone number
# without using regular expressions
# American phone number format is 123-123-1234
def isPhoneNumber(text):
    if len(text) != 12:
        return False
