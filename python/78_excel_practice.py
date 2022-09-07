# Excel practice question(s)
import openpyxl


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

# Save workbook
wb.save("excel_practice.xlsx")
