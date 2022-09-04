import openpyxl

# Opening Excel file
wb = openpyxl.load_workbook("example.xlsx")
# print(type(wb))


# Getting sheets from the workbook
# print(wb.sheetnames)
# sheet = wb["Sheet3"]
# print(sheet)
# print(type(sheet))
# print(sheet.title)
# active_sheet = wb.active
# print(active_sheet)


# Getting cells from the sheets
sheet = wb["Sheet1"]
print(sheet["A1"])
print(sheet["A1"].value)
