# Pig Latin program 🐷
# Translates given input sentence to Pig Latin 🐽
VOWELS = ("a", "e", "i", "o", "u", "y")
pig_latin = []

print("Enter the English message to translate into Pig Latin:")
message = input()

# English to Pig Latin
for word in message.split():
    # Separate the non-letters at the start of the current word
    prefix_non_letters = ""
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]

    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue

    # Separate the non-letters at the end of the current word
    suffix_non_letters = ""
    while not word[-1].isalpha():
        suffix_non_letters += word[-1]
        word = word[:-1]
