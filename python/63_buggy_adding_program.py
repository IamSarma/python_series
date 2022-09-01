import random

# Debugging a number adding program
# print("Enter the first number to add:")
# first_num = input()
# print("Enter the second number to add:")
# second_num = input()
# print("Enter the third number to add:")
# third_num = input()

# print("The sum is " + first_num + second_num + third_num)


# Breakpoints
heads_count = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads_count += 1
    if i == 500:
        print("Halfway done!")

print(f"Heads came up {str(heads_count)} times")
