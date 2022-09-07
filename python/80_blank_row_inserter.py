# Program to insert user provided number of blank rows
# at user provided row number
import openpyxl
import sys

# Create workbook object
wb = openpyxl.load_workbook("insert_blank_row.xlsx")

# Create worksheet object
sheet = wb["Sheet1"]

# Save workbook
wb.save("insert_blank_row.xlsx")
