# Excel practice question(s)
import openpyxl
from openpyxl.utils import column_index_from_string, get_column_letter


# Open/load workbook
wb = openpyxl.load_workbook("excel_practice.xlsx")

# Sheetnames
print(wb.sheetnames)

# Retrieve worksheet object
sheet = wb["Sheet1"]
print(sheet)

# Retrieve worksheet object for activesheet
act_sheet = wb.active
print(act_sheet)

# Set cell value
sheet["A1"] = "Python"

# Get cell value
print(sheet["A1"].value)

# Retrieve cell's row and column as integers
c = sheet["A1"]
print("Selected cell is A1")
print(f"Row number: {c.row}")
print(f"Column number: {c.column}")

# Get last row
print(f"Last/Max row: {sheet.max_row}")
print(f"The data type of sheet.max_row is: {type(sheet.max_row)}")

# Get last column
print(f"Last/Max column: {sheet.max_column}")
print(f"The data type of sheet.max_column is: {type(sheet.max_column)}")

# Get column index as integer value
col_int_index = column_index_from_string("C")
print(f"The index of column C is: {col_int_index}")

# Get column letter/string name from integer index
col_index = 8
col_str_letter = get_column_letter(col_index)
print(f"The string letter for column index {col_index} is: {col_str_letter}")

# Save workbook
wb.save("excel_practice.xlsx")
