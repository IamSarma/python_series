#! python3
# read_census_excel.py
# Tabulates population and number of census tracts for each county
import openpyxl
import pprint

# Read the spreadsheet data
print("Opening workbook...")
wb = openpyxl.load_workbook("censuspopdata.xlsx")
sheet = wb["Population by Census Tract"]
county_data = {}
