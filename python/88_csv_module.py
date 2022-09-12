import csv

# Reader Object(s)
text_file = open("example.csv")
text_file_reader = csv.reader(text_file)
text_file_data = list(text_file_reader)
print(text_file_data)
