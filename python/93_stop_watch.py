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


# Start tracking the lap time(s) and display to the user
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print(f"Lap #{lap_num}: {total_time} {lap_time}", end="")
        lap_num += 1
        last_time = time.time()     # Reset the lap time
except KeyboardInterrupt:
    print("\nDone")
