#! python3
# remove_csv_header.py
# Remove the header from all the CSV file(s) in the current working directory
import csv
import os

# Create folder to save the header removed CSV file(s)
os.makedirs("header_removed", exist_ok=True)

# Loop through every file in the current working directory
for csv_file_name in os.listdir("."):
    if not csv_file_name.endswith(".csv"):
        continue

    print(f"Removing header from {csv_file_name} ...")

    # Read the CSV file (skipping the first row)
    csv_rows = []
    csv_file_obj = open(csv_file_name)
    csv_reader_obj = csv.reader(csv_file_obj)
    for row in csv_reader_obj:
        if csv_reader_obj.line_num == 1:
            continue
        csv_rows.append(row)
        
    csv_file_obj.close()

    # Write out the CSV file
