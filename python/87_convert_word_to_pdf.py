# This script runs on Windows only and Word must be installed
import win32com.client
import docx

# Assinging file name(s) to word and pdf file(s)
word_file_name = "word_to_pdf.docx"
pdf_file_name = "pdf_from_word.pdf"

# Create and save word document
doc = docx.Document()
doc.add_paragraph(
    "This word document is created and converted to PDF using Python 🐍🤩")
doc.save(word_file_name)

# Convert word to PDF
word_format_pdf = 17        # Word's numeric code for PDF
word_obj = win32com.client.Dispatch("Word.Application")
