# Program to generate multiplication table basis the user input
# and update the same in Excel
import openpyxl

# Create workbook
wb = openpyxl.Workbook()

# Save wokbook
wb.save("multiplication_table.xlsx")
