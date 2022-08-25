# Reading and writing files
from pathlib import Path

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
# Writing
test_file = open(Path.cwd() / "ome_more.txt", "w")
test_file.write("Hello MB!\n")
test_file.close()
# Append
test_file = open(Path.cwd() / "ome_more.txt", "a")
test_file.write("Manog is a fruit :P")
test_file.close()
