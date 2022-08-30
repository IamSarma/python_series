#! python3
# folder_backup_project.py
# Copies and entire folder and its contents into a ZIP file whose filename increments
import zipfile
import os


# Backup the entire contents of specific folder into a ZIP file
def backupToZip(folder):
    target_folder = os.path.abspath(folder)

    # Figure out the filename that should be used based on what files already exist
    file_number = 1
    while True:
        zip_file_name = os.path.basename(
            folder) + "_" + str(file_number) + ".zip"
        if not os.path.exists(zip_file_name):
            break
        file_number += 1

    print("Folder backed up")
