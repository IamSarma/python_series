# Reading and writing files
from pathlib import Path
import shelve

# txt_file = Path("test.txt")
# txt_file.write_text("Hello MB!")
# print(txt_file.read_text())


# Opening files with the open() function
# test_file = open(Path.cwd() / "test.txt")


# Reading the contents of the file using read() method
# file_content = test_file.read()
# print(file_content)


# Reading multiple lines of file content using readlines() method
# sonnet_file = open(Path.cwd() / "sonnet29.txt")
# print(sonnet_file.readlines())


# Writing to file(s)
# Write
# test_file = open(Path.cwd() / "ome_more.txt", "w")
# test_file.write("Hello MB!\n")
# test_file.close()
# Append
# test_file = open(Path.cwd() / "ome_more.txt", "a")
# test_file.write("Manog is a fruit :P")
# test_file.close()
# Read
# test_file = open(Path.cwd() / "ome_more.txt")
# file_content = test_file.read()
# test_file.close()
# print(file_content)


# Storing variable values to hard drive using shelve module
shelf_file = shelve.open("my_data")
courses = ["python", "DSA", "React", "Vue"]
shelf_file["courses"] = courses
shelf_file.close()
