# Function to convert input list values to comma separated string
def listToString(input):
    final_string = ""

    if not input:
        return []

    for i in range(len(input)):
        if i == len(input) - 1:
            final_string += "and " + input[i]
        else:
            final_string += input[i] + ", "

    return final_string


food_list = ["apples", "bananas", "oranges", "grapes", "pizza"]
print(listToString(food_list))
