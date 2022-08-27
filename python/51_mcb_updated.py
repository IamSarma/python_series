#! python3
# mcb.py - Saved and loads pieces of text to the clipboard
# Usage :
# py.exe <file_name> save <keyword> - Saves clipboard to keyword
# py.exe <file_name> <keyword> - Loads keyword to clipboard
# py.exe <file_name> list - Loads all keywords to clipboard
# Adding additional functionality
# py.exe <file_name> delete <keyword> - Deletes specific keyword
# py.exe <file_name> delete - Delete all the keywords
import shelve
import pyperclip
import sys

mcb_shelf = shelve.open("mcb")

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == "delete":
    del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1].lower() == "delete":
        mcb_shelf.clear()
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
