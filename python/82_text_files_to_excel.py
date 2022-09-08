# Program to read the contents of several text file(s) and
# insert each text file content into separate column(s)
import openpyxl
import os

# Folder path containing text file(s)
target_folder = os.getcwd() + "/text_files"

# Loop through target folder to read text file contents
for file_name in os.listdir(target_folder):
    if file_name.endswith(".txt"):
        text_file_obj = open(os.path.join(target_folder, file_name), "r")
        print(text_file_obj.readlines())
        text_file_obj.close()

# Create workbook object
# wb = openpyxl.load_workbook("text_to_excel.xlsx")

# Create worksheet object
# sheet = wb["Sheet1"]

# Save workbook
# wb.save("text_to_excel.xlsx")
