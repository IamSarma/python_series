import openpyxl

# Creating and saving Excel file(s)
wb = openpyxl.Workbook()
print(wb.sheetnames)
sheet = wb.active
print(sheet.title)
sheet.title = "master_data"
print(sheet.title)
print(wb.sheetnames)
