import zipfile
import os
from pathlib import Path


# Reading zip file(s)
home_path = Path.home()
sample_zip = zipfile.ZipFile(home_path / "copy_me.zip")
print(sample_zip.namelist())

# Extracting from zip file(s)

# Creating and adding to zip file(s)
