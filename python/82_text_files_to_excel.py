# Program to read the contents of several text file(s) and
# insert each text file content into separate column(s)
import openpyxl

# Create workbook object
wb = openpyxl.load_workbook("text_to_excel.xlsx")

# Create worksheet object
sheet = wb["Sheet1"]

# Save workbook
wb.save("text_to_excel.xlsx")
