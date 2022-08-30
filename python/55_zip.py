import zipfile
import os
from pathlib import Path


# Reading zip file(s)
home_path = Path.home()
sample_zip = zipfile.ZipFile(home_path / "test.zip")
# print(sample_zip.namelist())
sample_zip_size = sample_zip.getinfo("test.txt")
print(sample_zip_size)

# Extracting from zip file(s)

# Creating and adding to zip file(s)
