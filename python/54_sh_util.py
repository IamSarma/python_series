# Using shutil module
import shutil
import os
from pathlib import Path

# Copying files
path_object = Path.home()
# shutil.copy(path_object / "copy_me.txt", path_object / "copy_here")
# shutil.copy(path_object / "copy_me.txt",
#             path_object / "copy_here\iam_copied.txt")


# Copying entire directory/folder
# shutil.copytree(path_object / "copy_me", path_object / "copy_me_backup")


# Moving and renaming files and folders
# shutil.move(path_object / "copy_me.txt", path_object / "copy_here")
shutil.move(path_object / "copy_here/copy_me.txt",
            path_object / "copy_here/new_copy_me.txt")
