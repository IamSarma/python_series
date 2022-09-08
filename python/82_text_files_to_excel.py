# Program to read the contents of several text file(s) and
# insert each text file content into separate column(s)
import openpyxl
import os

# Folder path containing text file(s)
target_folder = os.getcwd() + "/text_files"

# Loop through target folder to read text file contents
for file in os.listdir(target_folder):
    if file.endswith(".txt"):
        print(file)

# Create workbook object
# wb = openpyxl.load_workbook("text_to_excel.xlsx")

# Create worksheet object
# sheet = wb["Sheet1"]

# Save workbook
# wb.save("text_to_excel.xlsx")
