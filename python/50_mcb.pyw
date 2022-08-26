#! python3
# mcb.pyw - Saved and loads pieces of text to the clipboard
# Usage :
# py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard
# py.exe mcb.pyw list - Loads all keywords to clipboard
from ast import arg
import shelve
import pyperclip
import sys

mcb_shelf = shelve.open("mcb")

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.arg) == 2:
    # List keywords and load content

mcb_shelf.close()
