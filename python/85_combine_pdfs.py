#! python3
# combine_pdfs.py
# Combines all the PDFs in the current working directory into a single PDF
# Exlcudes first page in all the PDFs while combining
import PyPDF2
import os


# Get all the PDF file names in the current working directory
pdf_files = []
for file_name in os.listdir("."):
    if file_name.endswith(".pdf"):
        pdf_files.append(file_name)
