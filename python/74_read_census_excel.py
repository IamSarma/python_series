#! python3
# read_census_excel.py
# Tabulates population and number of census tracts for each county
import openpyxl
import pprint
import census_2010


# # Read the spreadsheet data
# print("Opening workbook...")
# wb = openpyxl.load_workbook("censuspopdata.xlsx")
# sheet = wb["Population by Census Tract"]
# county_data = {}


# # Fill in county_data with each county's population and tracts
# print("Reading rows...")
# for row in range(2, sheet.max_row + 1):
#     state_name = sheet["B" + str(row)].value
#     county_name = sheet["C" + str(row)].value
#     population = sheet["D" + str(row)].value

#     # Make sure the key for this state exists
#     county_data.setdefault(state_name, {})

#     # Make sure the key for this county for this state exists
#     county_data[state_name].setdefault(
#         county_name, {"tracts": 0, "population": 0})

#     # Each row represents one census tract, so increment by 1
#     county_data[state_name][county_name]["tracts"] += 1

#     # Increase the county population by the population in this census tract
#     county_data[state_name][county_name]["population"] += int(population)


# # Open a new text file and write the contents of county_data to it
# print("Writing results...")
# result_file = open("census_2010.py", "w")
# result_file.write("all_data = " + pprint.pformat(county_data))
# result_file.close()
# print("Done")


# Reading data from the generated file
print(census_2010.all_data["AK"]["Anchorage"])
anchorage_pop = census_2010.all_data["AK"]["Anchorage"]["population"]
print(f"The 2010 population of Anchorage was {anchorage_pop}")
