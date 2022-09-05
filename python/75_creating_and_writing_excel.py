import openpyxl

# Creating Excel workbook
# wb = openpyxl.Workbook()
# print(wb.sheetnames)
# sheet = wb.active
# print(sheet.title)
# sheet.title = "master_data"
# print(sheet.title)
# print(wb.sheetnames)


# Saving Excel workbook
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "master_data"
wb.save("created_with_python.xlsx")
