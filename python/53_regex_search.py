# Program to open all text files in a given folder
# and search for any line that matches a user-supplied regex
# and print the result to the screen
import re
import os

target_folder = "C:\\Users\\MB\\Documents\\python_series\\text_files"

# Ask user to input regex
user_regex = input("Enter regex to search and display the result:\n")
user_regex = re.compile(user_regex)


# Loop through all the text file(s) in the target folder
for file_name in os.listdir(target_folder):
    if file_name.endswith(".txt"):
        target_file = open(target_folder + "\\" + file_name)
        target_file.close()
