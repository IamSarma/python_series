import csv

# Reader Object(s)
# text_file = open("example.csv")
# text_file_reader = csv.reader(text_file)
# text_file_data = list(text_file_reader)
# print(text_file_data)

# Accessing data from the generated list
# print(text_file_data[0][1])
# print(text_file_data[1][0])
# print(text_file_data[2][1])
# print(text_file_data[3][2])

# Reading data from reader object(s) in a for loop
# Looping over the reader object works only once, create reader object again to loop second time 
# for row in text_file_reader:
#     print(f"Row # {text_file_reader.line_num} {row}")

# Writer object(s)
# output_file = open("output.csv", "w", newline="")
# output_writer = csv.writer(output_file)
# output_writer.writerow(["Python", "Java", "C++", "Ruby"])
# output_writer.writerow(["Hello, World!!!", "Hi Mom", "Python is awesome"])
# output_writer.writerow([1, 3, 5.67, 9])
# output_file.close()

# The delimeter and lineterminator
# output_file = open("example.tsv", "w", newline="")
# output_writer = csv.writer(output_file, delimiter="\t", lineterminator="\n\n")
# output_writer.writerow(["Apples", "Oranges", "Grapes"])
# output_writer.writerow(["Python", "JavaScript"])
# output_writer.writerow(["The Atomic Habits", "Greek Mythology"])
# output_file.close()

# Using DictReader Object with file containing header
# example_file = open("example_with_header.csv")
# example_dict_reader = csv.DictReader(example_file)
# for row in example_dict_reader:
#     print(row["Timestamp"], row["Fruit"], row["Quantity"])

# Using DictReader Object with file without header
# example_file = open("example.csv")
# example_dict_reader = csv.DictReader(example_file, ["time", "name", "amount"])
# for row in example_dict_reader:
#     print(row["time"], row["name"], row["amount"])

# Using DictWriter Object to create CSV file(s)
output_file = open("created_using_dictwriter.csv", "w", newline="")
output_dict_writer = csv.DictWriter(output_file, ["Name", "Proficiency", "Rating"])
output_dict_writer.writeheader()
output_dict_writer.writerow({"Name": "Python", "Proficiency": "Intermediate", "Rating": 4.5})
output_dict_writer.writerow({"Name": "HTML&CSS", "Rating": 3.5})
output_dict_writer.writerow({"Name": "Vue", "Proficiency": "Beginner"})
output_file.close()
