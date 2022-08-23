# Usage of pathlib module
from pathlib import Path


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
