# Program to copy data from spreadhsheet column(s) to individual text file(s)
# column A to one text file, column B to another and so on
import openpyxl
import os

# Create workbook object
wb = openpyxl.load_workbook()

# Create sheet object
sheet = wb["Sheet1"]

# Save workbook
wb.save()
