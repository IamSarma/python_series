#! python3
# stop_watch.py - A simple stopwatch program
import time


# Display the program's instructions
print("Press ENTER to begin. Afterward, press ENTER to click the stopwatch")
print("Press CTRL+C to quit")


# Take user input and start the lap
input()
print("Started")
start_time = time.time()
last_time = start_time
lap_num = 1
