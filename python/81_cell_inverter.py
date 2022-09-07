# Program to invert row and column of the cells in the spreadsheet
import openpyxl

# Create workbook object
wb = openpyxl.load_workbook("invert_rows_columns.xlsx")

# Create worksheet object
sheet = wb["Sheet1"]

# Save workbook
wb.save("invert_rows_columns.xlsx")
