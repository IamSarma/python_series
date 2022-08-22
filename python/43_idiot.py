# Program to keep an idiot busy for hours 😜🐍
import pyinputplus as pyip

while True:
    user_prompt = "Want to know how to keep an idiot busy for hours?\n"
    user_response = pyip.inputYesNo(user_prompt)

    if user_response == "no":
        break

print("Thank you. Have a nice day.")
