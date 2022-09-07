# Program to invert row and column of the cells in the spreadsheet
import openpyxl

# Create workbook object
wb = openpyxl.load_workbook("invert_rows_columns.xlsx")

# Save workbook
wb.save("invert_rows_columns.xlsx")
