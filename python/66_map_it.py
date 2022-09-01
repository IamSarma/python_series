#! python3
# map_it.py
# Launches a map in the browser using an address from the command line or clipboard

import webbrowser
import sys
import pyperclip


if len(sys.argv) > 1:
    # Get address from command line
    web_address = " ".join(sys.argv[1:])
else:
    # Get address from clipboard
    web_address = pyperclip.paste()


webbrowser.open("https://www.google.com/maps/place/" + web_address)
