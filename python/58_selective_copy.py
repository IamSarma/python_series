# Selective copy
# Program that walks through given folder tree and searched for files
# with given file extension and copy these files from whatever location
# they are into a new folder
import os
from pathlib import Path


def copySpecificFiles(folder, file_extension):
    base_folder = os.path.abspath(folder)
    target_folder = Path.cwd() / "copy_here"


copySpecificFiles(
    "C:\\Users\\MB\\Documents\\python_series\\search_here", ".txt")
