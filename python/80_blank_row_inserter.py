# Program to insert user provided number of blank rows
# at user provided row number
import openpyxl
import sys

# Create workbook object
wb = openpyxl.load_workbook("insert_blank_row.xlsx")

# Create worksheet object
sheet = wb["Sheet1"]

# User input - row number
row_number = int(sys.argv[1])

# User input - number of blank rows
blank_rows_num = int(sys.argv[2])

# Inserting blank row(s)
sheet.insert_rows(row_number + 1, amount=blank_rows_num)

# Save workbook
wb.save("insert_blank_row.xlsx")
