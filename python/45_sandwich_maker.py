# Program to ask users for their sandwich preferences
# and display total cost after the user enters their selection
import pyinputplus as pyip

food_items_price = {
    "wheat": 2,
    "white": 1,
    "sourdough": 2,
    "chicken": 3,
    "turkey": 4,
    "ham": 3,
    "tofu": 2,
    "cheddar": 1,
    "swiss": 2,
    "mozzarella": 1,
    "toppings": 1
}

# Ask user for bread type
user_bread_pref = pyip.inputMenu(
    ["wheat", "white", "sourdough"], "Bread type:\n")


# Ask user for protein type
user_protein_pref = pyip.inputMenu(
    ["chicken", "turkey", "ham", "tofu"], "Protein type:\n")


# Ask user if they want cheese or not
is_cheese_required = pyip.inputYesNo("Do you want cheese? (Yes/No)\n")


# Is user want cheese, then check their preference
if is_cheese_required.lower() == "yes":
    user_cheese_pref = pyip.inputMenu(
        ["cheddar", "swiss", "mozzarella"], "Cheese type:\n")


# Ask user if they want the topping(s)
is_toppings_required = pyip.inputYesNo(
    "Do you want mayo, mustard, lettuce or tomato? (Yes/No)\n")


# Ask how many sandwiches are required, ensure it's either 1 or more
num_of_sandwiches = pyip.inputInt("How many sandwiches do you want?\n", min=1)
