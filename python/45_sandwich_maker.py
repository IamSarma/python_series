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
    "cheddar": 2,
    "swiss": 2,
    "mozzarella": 3,
    "toppings": 1
}

# Ask user for bread type
user_bread_pref = pyip.inputMenu(
    ["wheat", "white", "sourdough"], "Bread type:\n")
bread_cost = food_items_price[user_bread_pref]

# Ask user for protein type
user_protein_pref = pyip.inputMenu(
    ["chicken", "turkey", "ham", "tofu"], "Protein type:\n")
protein_cost = food_items_price[user_protein_pref]


# Ask user if they want cheese or not
is_cheese_required = pyip.inputYesNo("Do you want cheese? (Yes/No)\n")


# Is user want cheese, then check their preference
if is_cheese_required.lower() == "yes":
    user_cheese_pref = pyip.inputMenu(
        ["cheddar", "swiss", "mozzarella"], "Cheese type:\n")
    cheese_cost = food_items_price[user_cheese_pref]
else:
    cheese_cost = 0


# Ask user if they want the topping(s)
is_toppings_required = pyip.inputYesNo(
    "Do you want mayo, mustard, lettuce or tomato? (Yes/No)\n")
if is_toppings_required.lower() == "yes":
    toppings_cost = food_items_price["toppings"]
else:
    toppings_cost = 0


# Ask how many sandwiches are required, ensure it's either 1 or more
num_of_sandwiches = pyip.inputInt("How many sandwiches do you want?\n", min=1)


# Show total cost to the user
total_cost = (bread_cost + protein_cost + cheese_cost +
              toppings_cost) * num_of_sandwiches
print(f"Total cost of {num_of_sandwiches} sandwiches is {total_cost}")
