# Mad libs program
from pathlib import Path

text_file = open(Path.cwd() / "mad_libs.txt")
input_string = str(text_file.read())
text_file.close()

# Take user input
adjective_input = input("Enter an adjective:\n")
noun1_input = input("Enter a noun:\n")
verb_input = input("Enter a verb:\n")
noun2_input = input("Enter a noun:\n")

# Append the string and display to user
output_string = input_string.replace("ADJECTIVE", adjective_input)
output_string = output_string.replace("NOUN", noun1_input, 1)
output_string = output_string.replace("VERB", verb_input)
output_string = output_string.replace("NOUN", noun2_input)

print(output_string)
