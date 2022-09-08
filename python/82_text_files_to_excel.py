# Program to read the contents of several text file(s) and
# insert each text file content into separate column(s)
import openpyxl
import os

# Folder path containing text file(s)
target_folder = os.getcwd() + "/text_files"

# Create workbook object
wb = openpyxl.load_workbook("text_to_excel.xlsx")

# Create worksheet object
sheet = wb["Sheet1"]

# Loop through target folder to read text file contents
col_number = 1
for file_name in os.listdir(target_folder):
    if file_name.endswith(".txt"):
        text_file_obj = open(os.path.join(target_folder, file_name), "r")
        text_file_content = text_file_obj.readlines()
        # Write text file content(s) in individual column(s)
        row_number = 1
        for i in range(len(text_file_content)):
            sheet.cell(row=row_number,
                       column=col_number).value = text_file_content[i]
            row_number += 1
        col_number += 1
        text_file_obj.close()

# Save workbook
wb.save("text_to_excel.xlsx")
