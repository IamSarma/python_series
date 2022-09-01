#! python3
# map_it.py
# Launches a map in the browser using an address from the command line or clipboard

import webbrowser
import sys

# webbrowser.open("https://www.inventwithpython.com/")
# Get address from command line
if len(sys.argv) > 1:
    web_address = " ".join(sys.argv[1:])
