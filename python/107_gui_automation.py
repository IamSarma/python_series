import time
import pyautogui
import subprocess


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
# pyautogui.middleClick(800, 500)
# pyautogui.doubleClick(600, 500)


# Scrolling the mouse
# pyautogui.scroll(200)
# pyautogui.scroll(-200)


# Get mouse movement's x and y co-ordinates (use in interactive shell preferably)
# pyautogui.mouseInfo()


# Take screenshot
# time.sleep(3)
# screen_shot = pyautogui.screenshot()
# screen_shot.save("paint_screenshot.png")


# Getting pixel's RGBA info at given x and y co-ordiantes
# time.sleep(3)
# print(pyautogui.pixel(1872, 13))


# Matching pixel's RGBA with color
# print(pyautogui.pixelMatchesColor(1872, 13, (100, 255, 0)))
# print(pyautogui.pixelMatchesColor(1872, 13, (35, 38, 46)))


# Image Recognition
# time.sleep(3)
# try:
#     screen_position = pyautogui.locateOnScreen("windows_update.png")
# except:
#     print("Image not found")
# print(screen_position)


# Perform mouse click based on the image recognition
# pyautogui.click(screen_position)


# Windows
# Obtaining the active window
# time.sleep(3)
# active_window = pyautogui.getActiveWindow()
# print(active_window)
# print(active_window.title)
# print(active_window.size)
# print(active_window.left, active_window.top,
#       active_window.right, active_window.bottom)
# print(active_window.topleft)
# print(active_window.area)
# pyautogui.click(active_window.left + 100, active_window.top + 50)

# Other way(s) of obtaining windows
# print(pyautogui.getAllWindows())
# print(pyautogui.getWindowsAt(100, 100))
# print(pyautogui.getWindowsWithTitle("Paint"))


# Manipulating windows
# time.sleep(2)
# active_window = pyautogui.getActiveWindow()
# print(active_window.width)
# print(active_window.topleft)
# active_window.width = 1000
# active_window.topleft = (120, 75)


# More ways of manipulating windows
# time.sleep(2)
# paint_window = pyautogui.getWindowsWithTitle("Paint")[0]
# # Check and maximize the window
# if not paint_window.isMaximized:
#     paint_window.maximize()
# # Check and minimize the window
# if not paint_window.isMinimized:
#     paint_window.minimize()
# # Check the minimized window and restore
# if paint_window.isMinimized:
#     paint_window.restore()
# # Closing the window
# time.sleep(2)
# paint_window.close()


# Controlling the keyboard
# Sending a string from the keyboard
subprocess.Popen("notepad.exe")
time.sleep(1)
# pyautogui.write("Python is awesome!!!")
# pyautogui.write("Python is awesome!!!", interval=0.05)

# Passing keyboard key string(s)
# pyautogui.write(["a", "b", "left", "left", "X", "Y"], interval=0.05)

# Pressing and releasing the keyboard
# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# Hotkey combination(s)
# Pressing ctrl+v (copy some text before) - normal and difficult way
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("v")
# pyautogui.keyUp("v")
# pyautogui.keyUp("ctrl")
# Pressing ctrl+v using hotkey combination
pyautogui.hotkey("ctrl", "v")
