# Using shutil module
import shutil
import os
from pathlib import Path
import send2trash

# Copying files
path_object = Path.home()
# shutil.copy(path_object / "copy_me.txt", path_object / "copy_here")
# shutil.copy(path_object / "copy_me.txt",
#             path_object / "copy_here\iam_copied.txt")


# Copying entire directory/folder
# shutil.copytree(path_object / "copy_me", path_object / "copy_me_backup")


# Moving and renaming files and folders
# shutil.move(path_object / "copy_me.txt", path_object / "copy_here")
# shutil.move(path_object / "copy_here/copy_me.txt",
#             path_object / "copy_here/new_copy_me.txt")


# FileNotFoundError in case of target path doesn't exist
# shutil.move(path_object / "copy_here/new_copy_me.txt",
#             path_object / "C:/does_not_exist/result/in/error")


# Permanently deleting files and folders
# Delete the file at given path
# os.unlink(r"C:\Users\MB\copy_here\iam_copied.txt")

# Deleting folder (empty folder only)
# os.rmdir(r"C:\Users\MB\empty_folder")

# Deleting folder and containing sub-folder(s) and file(s)
# shutil.rmtree(r"C:\Users\MB\copy_me_backup")

# It's better to print the filename(s) and validate before deleting
# for file_name in Path.home().glob("*.txt"):
#     print(file_name)
#     # os.unlink(file_name)


# Safe delete with the send2trash module
# send2trash.send2trash(r"C:\Users\MB\dont_delete.txt")


# Walking a directory tree
# how to walk through folder(s) -> sub-folder(s) -> file(s)
for folder_name, sub_folders, file_names in os.walk(r"C:\Users\MB\copy_me"):
    print(f"The current folder is {folder_name}")
    print()
