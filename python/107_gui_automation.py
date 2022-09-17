import pyautogui


# Obtaining the screen resolution
# screen_width, screen_height = pyautogui.size()
# print(pyautogui.size())
# print(f"The current display's width is: {screen_width} pixels")
# print(f"The current display's height is: {screen_height} pixels")


# Moving the mouse in square pattern from fixed start position
# for i in range(5):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)


# Moving the mouse in square pattern from mouse's current position
# for i in range(5):
#     pyautogui.move(100, 0, duration=0.25)
#     pyautogui.move(0, 100, duration=0.25)
#     pyautogui.move(-100, 0, duration=0.25)
#     pyautogui.move(0, -100, duration=0.25)


# Getting the mouse cursor's current position
# print(pyautogui.position())
# mouse_position = pyautogui.position()
# print(f"Mouse cursor's current position is: {mouse_position}")
# print(f"Getting cursor's x-axis position using index 0: {mouse_position[0]}")
# print(f"Getting cursor's y-axis position using index 1: {mouse_position[1]}")
# print(f"Getting cursor's x-axis position using 'x': {mouse_position.x}")
# print(f"Getting cursor's y-axis position using 'y': {mouse_position.y}")


# Clicking the mouse
# pyautogui.click(500, 500)
# pyautogui.rightClick(1000, 500)
pyautogui.middleClick(800, 500)
