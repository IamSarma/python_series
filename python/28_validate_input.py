# Simple progrma to validate user age and password
while True:
    print("Enter your age:")
    age = input()
    if age.isdecimal():
        break
    print("Please enter a number for your age.")


while True:
    print("Select a new password (letters and numbers only):")
    password = input()
    if password.isalnum():
        break
    print("Password can only have lettes and numbers")
