import datetime
import time


# Displaying current date and time
print(datetime.datetime.now())


# Displaying year, month, day, hour, minute and seconds
current_date = datetime.datetime.now()
print(current_date.year, current_date.month, current_date.day)
print(current_date.hour, current_date.minute, current_date.second)


# Converting Unix epoch timestamp to a datetime object
print(datetime.datetime.fromtimestamp(1_000_000))
print(datetime.datetime.fromtimestamp(time.time()))
