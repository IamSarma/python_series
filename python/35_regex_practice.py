# Example(s) of regex use cases
# Identifying valid phone number
import re

# Basic phone number search
phonenum_regex_1 = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
match_object_1 = phonenum_regex_1.search("My number is 123-456-7788")
print(f"Phone number found: {match_object_1.group()}")


# Validation of phone number containing paranthesis
# also helpful to extract country code and number separately
# escape the backslash using "\(and\)"
phonenum_regex_2 = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
match_object_2 = phonenum_regex_2.search("My number is (123) 456-7890")
print(f"Country code found : {match_object_2.group(1)}")
print(f"Phone number found : {match_object_2.group(2)}")


# Matching multiple groups with Pipe
hero_regex = re.compile(r"Batman|Tina Fey")
match_object_3 = hero_regex.search("Batman and Tina Fey")
print(match_object_3.group())

match_object_4 = hero_regex.search("Tina Fey and Batman")
print(match_object_4.group())


# Matching one of several patterns with Pipe and paranthesis
bat_regex_1 = re.compile(r"Bat(man|mobile|copter|bat)")
match_object_5 = bat_regex_1.search("Batmobile lost a wheel")
print(match_object_5.group())
print(match_object_5.group(1))


# Optional pattern matching with the Question mark
bat_regex_2 = re.compile(r"Bat(wo)?man")
match_object_6 = bat_regex_2.search("The Adventures of Batman")
print(match_object_6.group())

match_object_7 = bat_regex_2.search("The Adventures of Batwoman")
print(match_object_7.group())


# Matching zero or more pattern occurrences with Star *
bat_regex_3 = re.compile(r"Bat(wo)*man")
match_object_8 = bat_regex_3.search("The Adventures of Batman")
print(match_object_8.group())

match_object_9 = bat_regex_3.search("The Adventures of Batwoman")
print(match_object_9.group())

match_object_10 = bat_regex_3.search("The Adventures of Batwowowowowoman")
print(match_object_10.group())


# Matching one or more pattern occurences with Plus +
bat_regex_4 = re.compile(r"Bat(wo)+man")
match_object_11 = bat_regex_4.search("The Adventures of Batwoman")
print(match_object_11.group())

match_object_12 = bat_regex_4.search("The Adventures of Batwowowoman")
print(match_object_12.group())

match_object_13 = bat_regex_4.search("The Adventures of Batman")
print(match_object_13 == None)


# Matching specific repititions with braces
ha_regex = re.compile(r"(Ha){3}")
match_object_14 = ha_regex.search("HaHaHa")
print(match_object_14.group())

match_object_15 = ha_regex.search("Ha")
print(match_object_15 == None)


# Greedy and Non-greedy (lazy) match
greedy_regex = re.compile(r"(Ha){3,5}")
match_object_16 = greedy_regex.search("HaHaHaHaHa")
print(match_object_16.group())

non_greedy_regex = re.compile(r"(Ha){3,5}?")
match_object_17 = non_greedy_regex.search("HaHaHaHaHa")
print(match_object_17.group())
