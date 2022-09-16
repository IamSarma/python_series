#! python 3
# send_dues_reminders.py
# Send payment reminder email(s) based on payment status in spreadsheet
import openpyxl
import smtplib
import sys


# open the spreadsheet and get the latest dues status
wb = openpyxl.load_workbook("dues_records.xlsx")
sheet = wb["Sheet1"]
last_col = sheet.max_column
latest_month = sheet.cell(row=1, column=last_col).value
