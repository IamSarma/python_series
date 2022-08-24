# Usage of pathlib module
from pathlib import Path
import os


# Sample path object(s)
# print(Path("projects", "python"))
# print(str(Path("projects", "python")))


# Loop through and generate file path
# my_files = ["projects.txt", "data.csv", "todo.docx"]
# for file_name in my_files:
#     print(Path(r"C:\Users\MB", file_name))


# Using the / operator to join paths
# print(Path("projects") / "python" / "pathlib")
# print(Path("projects") / Path("python/pathlib"))
# print(Path("projects") / Path("python", "pathlib"))


# Example of joining parent and sub folder(s) paths
# parent_folder = Path("C:/Users/MB")
# sub_folder = Path("python_projects")
# print(parent_folder / sub_folder)
# print(str(parent_folder / sub_folder))


# Current working directory
# print(Path.cwd())


# Changing directory path using chdir()
# os.chdir("C:/Windows/System32")
# print(Path.cwd())


# The home directory
# print(Path.home())


# Creating new folders using os.makedirs() function
# os.makedirs("D:/test/sample/python")


# Creating singe folder using Path.mkdir() function
# Path(r"D:/test_1").mkdir()


# Handling absolute and relative paths
# print(Path.cwd())
# print(Path.cwd().is_absolute())
# print(Path.cwd() / Path("my/relative/path"))
# print(Path.home() / Path("my/relative/path"))


# Handling absolute and relative paths using os module
# print(os.path.abspath("."))
# print(os.path.abspath(".\scripts"))
# print(os.path.isabs("."))
# print(os.path.isabs(os.path.abspath(".")))
# print(os.path.relpath("C:\\Windows", "C:\\"))
# print(os.path.relpath("C:\\Windows", "C:\\python\\scripts"))


# Extracting part(s) of a folder path
# path_var = Path("C:/Users/MB/python.py")
# print(path_var.anchor)
# print(path_var.parent)
# print(path_var.name)
# print(path_var.stem)
# print(path_var.suffix)
# print(path_var.drive)


# Extracting ancestor folders path using parents method
# print(Path.cwd())
# print(Path.cwd().parents[0])
# print(Path.cwd().parents[1])
# print(Path.cwd().parents[2])
# print(Path.cwd().parents[3])


# Extracting different parts of a folder path using os module
# calc_file_path = "C:\Windows\System32\calc.exe"
# print(os.path.basename(calc_file_path))
# print(os.path.dirname(calc_file_path))
# print(os.path.split(calc_file_path))
# print(calc_file_path.split(os.sep))


# Finding file size
# print(os.path.getsize("C:\Windows\System32\calc.exe"))


# Finding file name(s)
# print(os.listdir("C:\Windows\System32"))


# Finding folder size
# total_size = 0
# for file_name in os.listdir("C:\Windows\System32"):
#     total_size += os.path.getsize(
#         os.path.join("C:\Windows\System32", file_name))
# print(total_size)


# Modifying a list of files using glob patterns
path_var = Path("C:\\Users\\MB\\Documents")
print(list(path_var.glob("*")))
