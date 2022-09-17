import pyautogui
import time

# Pause for 5 seconds
time.sleep(5)

# Click to make the windows active
pyautogui.click()

# Drawing spiral
distance_px = 600
change_px = 40
while distance_px > 0:
    pyautogui.drag(distance_px, 0, duration=0.25)
    distance_px -= change_px
    pyautogui.drag(0, distance_px, duration=0.25)
    pyautogui.drag(-distance_px, 0, duration=0.25)
    distance_px -= change_px
    pyautogui.drag(0, -distance_px, duration=0.25)
