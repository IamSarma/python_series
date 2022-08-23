# Usage of pathlib module
from pathlib import Path
import os


# Sample path object(s)
print(Path("projects", "python"))
print(str(Path("projects", "python")))


# Loop through and generate file path
my_files = ["projects.txt", "data.csv", "todo.docx"]
for file_name in my_files:
    print(Path(r"C:\Users\MB", file_name))


# Using the / operator to join paths
print(Path("projects") / "python" / "pathlib")
print(Path("projects") / Path("python/pathlib"))
print(Path("projects") / Path("python", "pathlib"))


# Example of joining parent and sub folder(s) paths
parent_folder = Path("C:/Users/MB")
sub_folder = Path("python_projects")
print(parent_folder / sub_folder)
print(str(parent_folder / sub_folder))


# Current working directory
print(Path.cwd())


# Changing directory path using chdir()
os.chdir("C:/Windows/System32")
print(Path.cwd())
