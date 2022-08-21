# Third party module to handle various input field's validation
import pyinputplus as pyip

user_response = pyip.inputInt(prompt="Enter your lucky number: ")
print(f"Your lucky number is {user_response}")
