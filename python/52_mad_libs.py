# Mad libs program
from pathlib import Path

text_file = open(Path.cwd() / "mad_libs.txt")
input_string = text_file.read()
text_file.close()

print(input_string)
