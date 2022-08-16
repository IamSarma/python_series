# Counting number of occurrences if each letter in a string
# Imported pprint module for generating beautiful output 🤩
import pprint


message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
