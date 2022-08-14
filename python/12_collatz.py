import sys


# Collatz sequence || Magic 🤩🐍😍
def collatz(number):
    result = 0
    # If number is even, then print and return number // 2
    # If number is odd, then print and return (3 * number) + 1
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = (3 * number) + 1
        print(result)
        return result


# Take user input (must be integer) and pass it to collatz
# Loop calling collatz until the function returned value is 1
while True:
    try:
        print("Enter positive integer only: ", end="")
        user_input = int(input())
        final_result = collatz(user_input)
        while True:
            if final_result == 1:
                sys.exit()
            else:
                final_result = collatz(final_result)
    except ValueError:
        print("Input must be a positive integer!!!")
