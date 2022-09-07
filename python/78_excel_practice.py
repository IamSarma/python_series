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

# Save workbook
wb.save
