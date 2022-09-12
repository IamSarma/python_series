import csv

# Reader Object(s)
text_file = open("example.csv")
text_file_reader = csv.reader(text_file)
text_file_data = list(text_file_reader)
print(text_file_data)

# Accessing data from the generated list
print(text_file_data[0][1])
print(text_file_data[1][0])
print(text_file_data[2][1])
print(text_file_data[3][2])
