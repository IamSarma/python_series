# Program to read text from notepad (gets text from clipboard)
import pyautogui
import pyperclip
import subprocess
import time


# Open Notepad application
subprocess.Popen("notepad.exe")
time.sleep(1)

# Create notepad window object and maximize the window
notepad_window = pyautogui.getActiveWindow()
notepad_window.maximize()

# Write some text in to the notepad window
time.sleep(1)
pyautogui.write(
    "This text is written in notepad using pyautogui, subprocess and time module(s) and copied using pyperclip module")

# Copy all the content from notepad window
time.sleep(0.5)
pyautogui.hotkey("ctrl", "a")
time.sleep(0.5)
pyautogui.hotkey("ctrl", "c")

# Print the copied content from notepad
notepad_content = pyperclip.paste()
print(notepad_content)

# Close notepad without saving changes
notepad_window.close()
time.sleep(0.5)
pyautogui.hotkey("alt", "n")
