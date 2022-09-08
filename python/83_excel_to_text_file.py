# Program to copy data from spreadhsheet column(s) to individual text file(s)
# column A to one text file, column B to another and so on
import openpyxl
import os

# Folder path containing text file(s)
target_folder = os.getcwd() + "/text_files"

# Create workbook object
wb = openpyxl.load_workbook("text_to_excel.xlsx")

# Create sheet object
sheet = wb["Sheet1"]

# Get last/max row and last/max column to loop through data
last_row = sheet.max_row
last_column = sheet.max_column

# Save workbook
wb.save("text_to_excel.xlsx")
