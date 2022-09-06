#! python3
# update_produce.py
# Corrects costs in produce sales spreadsheet
import openpyxl

wb = openpyxl.load_workbook("produce_sales.xlsx")
sheet = wb["Sheet"]

# The produce types and their updated prices
PRICE_UPDATES = {
    "Garlic": 3.07,
    "Celery": 1.19,
    "Lemon": 1.27
}
