#! python3
# folder_backup_project.py
# Copies and entire folder and its contents into a ZIP file whose filename increments
import zipfile
import os


# Backup the entire contents of specific folder into a ZIP file
def backupToZip(folder):
    print("Folder backed up")
