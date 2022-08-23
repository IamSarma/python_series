# Program to ask users for their sandwich preferences
# and display total cost after the user enters their selection
import pyinputplus as pyip

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
