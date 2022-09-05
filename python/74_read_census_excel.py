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


# Fill in county_data with each county's population and tracts
print("Reading rows...")
for row in range(2, sheet.max_row + 1):
    state_name = sheet["B" + str(row)].value
    county_name = sheet["C" + str(row)].value
    population = sheet["D" + str(row)].value

    # Make sure the key for this state exists
    county_data.setdefault(state_name, {})

    # Make sure the key for this county for this state exists
    county_data[state_name].setdefault(county_name, {"tracts": 0, "pop": 0})

    # Each row represents one census tract, so increment by 1
    county_data[state_name][county_name]["tracts"] += 1
