# Selective copy
# Program that walks through given folder tree and searched for files
# with given file extension and copy these files from whatever location
# they are into a new folder
import os
from pathlib import Path
import shutil


# Function to search and copy file(s) with user provided file extension
def copySpecificFiles(folder, file_extension):
    base_folder = os.path.abspath(folder)
    target_folder = Path.cwd() / "copy_here"

    # Walk through the user provided directory and find the file(s)
    for folder_name, sub_folders, file_names in os.walk(folder):
        print(
            f"Searching for file(s) with extension {file_extension} in {folder_name}")
        for file_name in file_names:
            if file_name.endswith(".txt"):
                file_full_path = os.path.join(base_folder, file_name)
                shutil.move(file_full_path, target_folder)
                print(
                    f"Moved {file_name} from {base_folder} to {target_folder}")


copySpecificFiles(
    "C:\\Users\\MB\\Documents\\python_series\\search_here", ".txt")
