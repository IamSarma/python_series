# Using pyinputplus third part module by passing various agrument(s)
import pyinputplus as pyip

# Using min argument
# user_response = pyip.inputNum("Enter a number: ", min=4)
# print(user_response)


# Using max argument
user_response_1 = pyip.inputNum("Enter a number: ", max=10)
print(user_response_1)
