import pyautogui


# Displaying message boxe(s)
# Alert
# pyautogui.alert("This is a critical message", "Important")

# Confirm
# pyautogui.confirm("Do you want to continue?", "Attention Required")

# Prompt
# user_name = pyautogui.prompt("Enter username: ", "Login")
# print(user_name)

# Password
user_password = pyautogui.password("Enter passowrd: ", "Secret")
print(user_password)
