# Reading and writing files
from pathlib import Path

# txt_file = Path("test.txt")
# txt_file.write_text("Hello MB!")
# print(txt_file.read_text())


# Opening files with the open() function
test_file = open(Path.cwd() / "test.txt")
