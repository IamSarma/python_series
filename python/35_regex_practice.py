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


# findall() method
phonenum_regex_3 = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
input_string = "Cell: 415-555-9999 Work: 212-555-0000"
match_object_18 = phonenum_regex_3.search(input_string)
print(match_object_18.group())
print(phonenum_regex_3.findall(input_string))

phonenum_regex_4 = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")
print(phonenum_regex_4.findall(input_string))


# The character class example
xmas_regex = re.compile(r"\d+\s+\w+")
xmas_message = "12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"
print(xmas_regex.findall(xmas_message))


# Making your own character class(es)
vowel_regex_1 = re.compile(r"[aeiouAEIOU]")
vowel_string = "Robocop eats baby food. BABY FOOD."
print(vowel_regex_1.findall(vowel_string))


# Making negative character class(es)
vowel_regex_2 = re.compile(r"[^aeiouAEIOU]")
print(vowel_regex_2.findall(vowel_string))


# Use Caret sign to apply starting with pattern
begins_with_hello = re.compile(r"^Hello")
match_object_19 = begins_with_hello.search("Hello, world!")
print(match_object_19.group())

match_object_20 = begins_with_hello.search("He said hello.")
print(match_object_20 == None)


# Use Dollar sign to apply ending with pattern
ends_with_number = re.compile(r"\d$")
match_object_21 = ends_with_number.search("My lucky number is 3")
print(match_object_21.group())

match_object_22 = ends_with_number.search("My lucky number is three")
print(match_object_22 == None)


# Use Caret and Dollar for exact matching pattern
whole_string_is_num = re.compile(r"^\d+$")
match_object_23 = whole_string_is_num.search("123456789")
print(match_object_23.group())

match_object_24 = whole_string_is_num.search("12345xxx6789")
print(match_object_24 == None)

match_object_25 = whole_string_is_num.search("123   456789")
print(match_object_25 == None)


# . (Dot) the wildcard character
at_regex = re.compile(r".at")
at_string = "The cat in the hat sat on the flat mat"
print(at_regex.findall(at_string))


# Matching everything with .*
name_regex = re.compile(r"First Name: (.*) Last Name: (.*)")
name_string = "First Name: Sarma Last Name: Akondi V N M"
match_object_26 = name_regex.search(name_string)
print(match_object_26.group(1))
print(match_object_26.group(2))


# Greedy and Non-greedy using .*
greedy_regex_2 = re.compile(f"<.*>")
search_string = "<To serve man> for dinner.>"
match_object_27 = greedy_regex_2.search(search_string)
print(match_object_27.group())

non_greedy_regex_2 = re.compile(r"<.*?>")
match_object_28 = non_greedy_regex_2.search(search_string)
print(match_object_28.group())


# Matching new lines with .*
no_newline_regex = re.compile(r".*")
newline_string = "Serve the public trust.\nProtect the innocent.\nUphold the law."
match_object_29 = no_newline_regex.search(newline_string)
print(match_object_29.group())

newline_regex = re.compile(r".*", re.DOTALL)
match_object_30 = newline_regex.search(newline_string)
print(match_object_30.group())


# Case-Insensitive matching
robocop_regex = re.compile(r"robocop", re.I)
robocop_string_1 = "Robocop is a part man, part machine, all cop"
robocop_string_2 = "ROBOCOP protects the innocent"
robocop_string_3 = "Why the heck are we taking about robocop so much 🤖"
print(robocop_regex.search(robocop_string_1).group())
print(robocop_regex.search(robocop_string_2).group())
print(robocop_regex.search(robocop_string_3).group())


# Substitution strings with the sub() method
names_regex = re.compile(r"Agent \w+")
secret_message = "Agent Alice gave the secret documents to Agent Bob"
print(names_regex.sub("CENSORED", secret_message))


# Group substitution
agent_names_regex = re.compile(r"Agent (\w)\w*")
agents_secret_message = "Agent Alice told Agent Carol the Agent Eve knew Agent Bob was a double agent."
print(agent_names_regex.sub(r"\1****", agents_secret_message))
