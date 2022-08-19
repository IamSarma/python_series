#! python 3
# bullet_point_adder.py - Adds Wikipedia bullet point to the start
# of each line of text on the clipboard.
import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split("\n")
for i in range(len(lines)):
    lines[i] += "* "

pyperclip.copy(text)
