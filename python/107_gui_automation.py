import pyautogui


# Obtaining the screen resolution
# screen_width, screen_height = pyautogui.size()
# print(pyautogui.size())
# print(f"The current display's width is: {screen_width} pixels")
# print(f"The current display's height is: {screen_height} pixels")


# Moving the mouse in square pattern from fixed start position
for i in range(5):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
