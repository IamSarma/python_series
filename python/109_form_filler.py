#! python 2
# form_filler.py - Automatically fills in the form
import pyautogui
import time


# Static form data
form_data = [
    {'name': 'Alice',
     'fear': 'eavesdroppers',
     'source': 'wand',
     'robocop': 4, 'comments':
     'Tell Bob I said hi.'},
    # {'name': 'Bob',
    #  'fear': 'bees',
    #  'source': 'amulet',
    #  'robocop': 4,
    #  'comments': 'n/a'},
    # {'name': 'Carol',
    #  'fear': 'puppets',
    #  'source': 'crystal ball',
    #  'robocop': 1,
    #  'comments': 'Please take the puppets out of thebreak room.'},
    # {'name': 'Alex Murphy',
    #  'fear': 'ED-209',
    #  'source': 'money',
    #  'robocop': 5,
    #  'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
]

# Adding global pause and displaying instruction to the user
pyautogui.PAUSE = 0.5
print("Ensure that the browser window is active and the form is loaded!")

# Give the user a chance to kill the script
# Wait until the form page has loaded
for person in form_data:
    print(">>> 5 SECOND PAUSE TO LET USER PRESS CTRL+C <<<")
    time.sleep(5)

    print(f"Entering {person['name']}")
    pyautogui.write(["\t", "\t", "\t", "\t"])

    # Fill out the Name field
    pyautogui.write(person['name'] + "\t")

    # Fill out the Greatest Fear(s) field

    # Fill out the Source of Wizard Powers field

    # Fill out the Robocop field

    # Fill out the Additional Comments field

    # Click Sumbit

    # Wait until form page has loaded

    # Click the Submit another response link
