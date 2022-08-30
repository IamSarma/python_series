import zipfile
import os
from pathlib import Path


# Reading zip file(s)
home_path = Path.home()
zip_file_object = zipfile.ZipFile(home_path / "test.zip")
# print(sample_zip.namelist())
zip_file_info = zip_file_object.getinfo("test.txt")
print(f"File size is: {zip_file_info.file_size} bytes")
print(f"File compressed size is: {zip_file_info.compress_size} bytes")
print(
    f"Compressed file is {round(zip_file_info.file_size / zip_file_info.compress_size, 2)}x smaller")

# Extracting from zip file(s)

# Creating and adding to zip file(s)
