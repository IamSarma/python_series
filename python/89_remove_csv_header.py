#! python3
# remove_csv_header.py
# Remove the header from all the CSV file(s) in the current working directory
import csv
import os

# Create folder to save the header removed CSV file(s)
os.makedirs("header_removed", exist_ok=True)
