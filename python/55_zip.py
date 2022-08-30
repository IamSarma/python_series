import zipfile
import os
from pathlib import Path


# Reading zip file(s)
home_path = Path.home()
sample_zip = zipfile.ZipFile(home_path / "test.zip")
# print(sample_zip.namelist())
sample_zip_info = sample_zip.getinfo("test.txt")
print(f"File size is: {sample_zip_info.file_size} bytes")
print(f"File compressed size is: {sample_zip_info.compress_size} bytes")
print(
    f"Compressed file is {round(sample_zip_info.file_size / sample_zip_info.compress_size, 2)}x smaller")

# Extracting from zip file(s)

# Creating and adding to zip file(s)
