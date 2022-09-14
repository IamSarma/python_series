import threading
import time

# Dispalying start message
print("Start of the program")

# Function that sleeps for a while and displays message
def takeANap():
    time.sleep(5)
    print("Wake up!!!")

# Creating and starting a new thread
thread_obj = threading.Thread(target=takeANap)
thread_obj.start()

# Dispalying end message
print("End of the program")
