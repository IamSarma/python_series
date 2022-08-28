# Using shutil module
import shutil
import os
from pathlib import Path

# Copying files and folders
path_object = Path.home()
shutil.copy(path_object / "copy_me.txt", path_object / "copy_here")
