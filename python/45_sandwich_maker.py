# Program to ask users for their sandwich preferences
# and display total cost after the user enters their selection
import pyinputplus as pyip

# Ask user for bread type
user_bread_pref = pyip.inputMenu(
    ["wheat", "white", "sourdough"], "Bread type:\n")
