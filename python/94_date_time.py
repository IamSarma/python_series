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


# Comparing datetime object(s)
halloween_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyear_2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
dob = datetime.datetime(1987, 2, 27, 0, 0, 0)

print(halloween_2019 == dob)
print(halloween_2019 > newyear_2020)
print(newyear_2020 > dob)
print(newyear_2020 != halloween_2019)
