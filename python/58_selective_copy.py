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
        for file_name in file_names:
            if file_name.endswith(".txt"):
                file_full_path = os.path.join(
                    os.path.abspath(folder_name), file_name)
                shutil.move(file_full_path, target_folder)
                print(
                    f"Moved {file_name} from {file_full_path} to {target_folder}")


copySpecificFiles(
    "C:\\Users\\MB\\Documents\\python_series\\search_here", ".txt")
