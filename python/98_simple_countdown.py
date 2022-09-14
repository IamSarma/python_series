#! python 3
# simple_countdown.py - A simple countdown script
import time
import subprocess

time_left = 10
while time_left > 0:
    print(time_left, end="")
    time.sleep(1)
    time_left -= 1

# Play sound at the end of the countdown
