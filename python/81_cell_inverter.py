# Program to invert row and column of the cells in the spreadsheet
import openpyxl

cells_data = []
items_data = []

# Create workbook object
wb = openpyxl.load_workbook("invert_rows_columns.xlsx")

# Create worksheet object
sheet = wb["Sheet1"]

# Read data from spreadsheet
for i in range(1, sheet.max_column+1):
    for j in range(1, sheet.max_row+1):
        items_data.append(sheet.cell(row=j, column=i).value)
    cells_data.append(list(items_data))
    items_data = []

# Save workbook
wb.save("invert_rows_columns.xlsx")
