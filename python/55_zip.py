import zipfile
import os
from pathlib import Path


# Reading zip file(s)
home_path = Path.home()
# zip_file_object = zipfile.ZipFile(home_path / "test.zip")
# print(sample_zip.namelist())
# zip_file_info = zip_file_object.getinfo("test.txt")
# print(f"File size is: {zip_file_info.file_size} bytes")
# print(f"File compressed size is: {zip_file_info.compress_size} bytes")
# print(
#     f"Compressed file is {round(zip_file_info.file_size / zip_file_info.compress_size, 2)}x smaller")

# Extracting from zip file(s)
# The below will extract the zip file content to current working directory
# zip_file_object.extractall()
# zip_file_object.close()

# The below will extract the zip file content to specific directory
# zip_file_object.extractall(Path.home())
# zip_file_object.close()

# Creating and adding to zip file(s)
# write mode
# zip_file_object = zipfile.ZipFile(home_path / "new.zip", "w")
# zip_file_object.write(home_path / "test.txt",
#                       compress_type=zipfile.ZIP_DEFLATED)

# append mode
zip_file_object = zipfile.ZipFile(home_path / "new.zip", "a")
zip_file_object.write(home_path / "1.txt",
                      compress_type=zipfile.ZIP_DEFLATED)
zip_file_object.close()
