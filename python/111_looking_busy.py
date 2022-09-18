# Program to nudge mouse cursor slightly every 10 seconds to look busy
import pyautogui
import time

# Nudge mouse cursor every 10 seconds till user interrupts the script
print("Press CTRL+C in the terminal window to stop/interrupt the script")
current_position = 100
while True:
    pyautogui.moveTo(current_position + 1, 100)
    current_position += 1
    time.sleep(10)
