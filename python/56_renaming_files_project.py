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


# Skip file(s) without a date


# Get the different parts of the filename


# Form the European-style filename


# Get the full, absolute file path(s)


# Rename the file(s)
