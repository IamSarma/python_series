# Program to generate multiplication table basis the user input
# and update the same in Excel
import openpyxl
import sys

table_data = []

# Create workbook
wb = openpyxl.Workbook()

# Create worksheet object
sheet = wb["Sheet"]

# Generate table headers row and column wise
for i in range(2, 8):
    sheet.cell(row=i, column=1).value = i - 1
    sheet.cell(row=1, column=i).value = i - 1

# Save wokbook
wb.save("multiplication_table.xlsx")
