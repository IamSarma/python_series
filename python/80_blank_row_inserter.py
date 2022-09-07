# Program to insert user provided number of blank rows
# at user provided row number
import openpyxl
import sys

# Create workbook object
wb = openpyxl.Workbook()

# Save workbook
wb.save("blank_row_inserter.xlsx")
