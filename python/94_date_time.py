import datetime
import time


# Displaying current date and time
# print(datetime.datetime.now())


# Displaying year, month, day, hour, minute and seconds
# current_date = datetime.datetime.now()
# print(current_date.year, current_date.month, current_date.day)
# print(current_date.hour, current_date.minute, current_date.second)


# Converting Unix epoch timestamp to a datetime object
# print(datetime.datetime.fromtimestamp(1_000_000))
# print(datetime.datetime.fromtimestamp(time.time()))


# Comparing datetime object(s)
# halloween_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
# newyear_2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
# dob = datetime.datetime(1987, 2, 27, 0, 0, 0)

# print(halloween_2019 == dob)
# print(halloween_2019 > newyear_2020)
# print(newyear_2020 > dob)
# print(newyear_2020 != halloween_2019)


# The timedelta date type
# delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# print(str(delta))


# Performing arithmetic operation(s) on datetime values
# Addition
dt = datetime.datetime.now()
thousand_days = datetime.timedelta(days=1000)
print(dt + thousand_days)
