#! python3
# renaming_files_project.py
# Renames filename(s) with American MM-DD-YYYY date format to European DD-MM-YYYY
import shutil
import os
import re


# Create a regex that matches the file(s) with the American date format
date_pattern = re.compile(r"""
    ^(.*?)                          # all text before the date
    (1[0-2]|0?[1-9])-               # one or two digits for the month
    (3[01]|[12][0-9]|[1-9])-        # one or two digits for the dayq
    ([0-9]{4})                      # four digits for the year
    (.*?)$                          # all text after the date
    """, re.VERBOSE)


# Loop over the files in the working directory
for american_file_name in os.listdir("."):
    match_object = date_pattern.search(american_file_name)

    # Skip file(s) without a date
    if match_object == None:
        continue

    # Get the different parts of the filename
    before_part = match_object.group(1)
    month_part = match_object.group(2)
    day_part = match_object.group(3)
    year_part = match_object.group(4)
    after_part = match_object.group(5)

    # Form the European-style filename
    european_file_name = f"{before_part}{day_part}-{month_part}-{year_part}{after_part}"

    # Get the full, absolute file path(s)
    absolute_directory = os.path.abspath(".")
    american_file_name = os.path.join(absolute_directory, american_file_name)
    european_file_name = os.path.join(absolute_directory, european_file_name)

    # Rename the file(s)
    print(f"Renaming '{american_file_name}' to '{european_file_name}'")
