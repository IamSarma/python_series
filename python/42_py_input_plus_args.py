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
# user_response_4 = pyip.inputNum("Enter a number: ", min=5, lessThan=10)
# print(user_response_4)


# Argument to use in case of blank input is allowed
# user_response_4 = pyip.inputNum("Enter a number: ", blank=True)
# print(user_response_4)


# Using limit argument
# user_response_5 = pyip.inputNum("Enter a number: ", limit=2)
# print(user_response_5)


# Using timeout argument
# user_response_6 = pyip.inputNum("Enter a number: ", timeout=3)
# print(user_response_6)


# Using default argument to handle output of limit and timeout gracefully
# user_response_7 = pyip.inputNum("Enter a number: ", limit=2, default="N/A")
# print(user_response_7)


# Using allowRegexes as argument
# user_response_8 = pyip.inputNum("Enter a Roman number: ", allowRegexes=[
#                                 r"(I|V|X|L|C|D|M)+", r"zero"])
# print(user_response_8)


# Using blockRegexes as argument
# user_response_9 = pyip.inputNum("Enter a number: ", blockRegexes=[r"[02468]$"])
# print(user_response_9)


# allowRegexes list will override blockregexes list when used both
# user_response_10 = pyip.inputNum("Enter a word: ", allowRegexes=[
#                                  r"caterpillar", "category"], blockRegexes=[r"cat"])
# print(user_response_10)


# Passing a custom validation function to inputCustom()
def addsUpToTen(numbers):
    numbers_list = list(numbers)
    for i, digit in enumerate(numbers_list):
        numbers_list[i] = int(digit)

    if sum(numbers_list) != 10:
        raise Exception(
            f"The digits must add upto 10, not {sum(numbers_list)}")

    return int(numbers)


user_response_11 = pyip.inputCustom(
    addsUpToTen, "Enter numbers that adds upto ten: ")
