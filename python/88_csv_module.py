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
output_file = open("output.csv", "w", newline="")
output_writer = csv.writer(output_file)
output_writer.writerow(["Python", "Java", "C++", "Ruby"])
output_writer.writerow(["Hello, World!!!", "Hi Mom", "Python is awesome"])
output_writer.writerow([1, 3, 5.67, 9])
output_file.close()
