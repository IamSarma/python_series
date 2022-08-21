# Using pyinputplus third part module by passing various agrument(s)
import pyinputplus as pyip

# Using min argument
# user_response = pyip.inputNum("Enter a number: ", min=4)
# print(user_response)


# Using max argument
# user_response_1 = pyip.inputNum("Enter a number: ", max=10)
# print(user_response_1)


# Using greaterThan argument
# user_response_2 = pyip.inputNum("Enter a number: ", greaterThan=10)
# print(user_response_2)


# Using lessThan argument
# user_response_3 = pyip.inputNum("Enter a number: ", lessThan=10)
# print(user_response_3)

# Using combination of argument(s)
user_response_4 = pyip.inputNum("Enter a number: ", min=5, lessThan=10)
print(user_response_4)
