# Program to generate multiplication table basis the user input
# and update the same in Excel
import openpyxl
import sys

table_data = []

# Create workbook
wb = openpyxl.Workbook()

# Create worksheet object
sheet = wb["Sheet"]

# Save wokbook
wb.save("multiplication_table.xlsx")
