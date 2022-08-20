# Function to check if the input string matches phone number
# without using regular expressions
# American phone number format is 123-123-1234
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True


message = "Call me at 426-444-2011 tomorrow. 426-444-1025 is my office"

for i in range(len(message)):
    chunk_of_text = message[i:i+12]
    if isPhoneNumber(chunk_of_text):
        print(f"Phone number found: {chunk_of_text}")
