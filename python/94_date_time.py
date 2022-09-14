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
# # Addition
# dt = datetime.datetime.now()
# thousand_days = datetime.timedelta(days=1000)
# print(dt + thousand_days)
# # Subtraction
# sep_14 = datetime.datetime(2022, 9, 14, 0, 0, 0)
# thirty_years = datetime.timedelta(days=365 * 30)      # Approximate value
# print(sep_14 - thirty_years)
# # Multiplication
# print(sep_14 - 2 * thirty_years)


# Pause program until a specific time
# current_time = datetime.datetime.now()
# plus_ten_seconds = current_time + datetime.timedelta(seconds=10)
# while current_time < plus_ten_seconds:
#     time.sleep(1)
#     current_time = datetime.datetime.now()
# print("Done")


# Converting datetime object(s) into string(s)
# current_date = datetime.datetime.now()
# print(current_date.strftime("%Y/%m/%d %H:%M:%S"))
# print(current_date.strftime("%I:%M %p"))
# print(current_date.strftime("%B of '%y"))


# Converting string(s) into datetime object(s)
print(datetime.datetime.strptime("September 14, 2022", "%B %d, %Y"))
print(datetime.datetime.strptime("2022/09/14 9:59:00","%Y/%m/%d %H:%M:%S"))
print(datetime.datetime.strptime("September of '21", "%B of '%y"))
print(datetime.datetime.strptime("February of '87", "%B of '%y"))
