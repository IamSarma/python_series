# Mad libs program
from pathlib import Path

text_file = open(Path.cwd() / "mad_libs.txt")
input_string = text_file.read()
text_file.close()

# Take user input and append the string
adjective_input = input("Enter an adjective:\n")
noun_input = input("Enter a noun:\n")
verb_input = input("Enter a verb:\n")
noun_input = input("Enter a noun:\n")

print(input_string)
