import openpyxl

# Opening Excel file
wb = openpyxl.load_workbook("example.xlsx")
print(type(wb))
