import PyPDF2

# Extracting text from PDF
# pdf_file_obj = open("meetingminutes.pdf", "rb")
# pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
# print(pdf_reader.numPages)

# page_obj = pdf_reader.getPage(0)
# print(page_obj.extractText())
# pdf_file_obj.close()


# Decrypting PDFs
pdf_reader = PyPDF2.PdfFileReader(open("encrypted.pdf", "rb"))
print(pdf_reader.isEncrypted)
