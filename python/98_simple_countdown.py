#! python 3
# simple_countdown.py - A simple countdown script
import time
import subprocess

time_left = 10
while time_left > 0:
    print(f"time left: {time_left}")
    time.sleep(1)
    time_left -= 1

# Play sound at the end of the countdown
subprocess.Popen(["start", "beep.mp3"], shell=True)
