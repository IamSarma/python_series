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
    "This text is written in notepad using pyautogui, subprocess and time modules and copied using pyperclip")

# Copy all the content from notepad window
time.sleep(0.5)
pyautogui.hotkey("ctrl", "a")
time.sleep(0.5)
pyautogui.hotkey("ctrl", "c")
