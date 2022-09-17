import pyautogui


# Obtaining the screen resolution
screen_width, screen_height = pyautogui.size()
print(f"The current display's width is: {screen_width} pixels")
print(f"The current display's height is: {screen_height} pixels")
