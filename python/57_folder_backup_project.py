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

    # Create the zip file
    print(f"Creating {zip_file_name}...")
    backup_zip = zipfile.ZipFile(zip_file_name, "w")

    # Walk the entire folder tree and compress the files in each folder
    for folder_name, sub_folders, file_names in os.walk(folder):
        print(f"Adding files in {folder_name}...")
        backup_zip.write(folder_name)

        # Add all the files in this folder to the ZIP file
        for file_name in file_names:
            new_base = os.path.basename(folder) + "_"
            if file_name.startswith(new_base) and file_name.endswith(".zip"):
                continue        # don't backup the already backed up file(s)
            backup_zip.write(os.path.join(folder_name, file_name))

    backup_zip.close()
    print("Folder backing up done")


backupToZip("C:\\Users\\MB\\copy_me")
