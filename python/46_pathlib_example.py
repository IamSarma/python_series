# Usage of pathlib module
from pathlib import Path

print(Path("projects", "python"))
print(str(Path("projects", "python")))


my_files = ["projects.txt", "data.csv", "todo.docx"]
for file_name in my_files:
    print(Path(r"C:\Users\MB", file_name))
