import PyPDF2

# Extracting text from PDF
# pdf_file_obj = open("meetingminutes.pdf", "rb")
# pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
# print(pdf_reader.numPages)

# page_obj = pdf_reader.getPage(0)
# print(page_obj.extractText())
# pdf_file_obj.close()


# Decrypting PDFs
# pdf_reader = PyPDF2.PdfFileReader(open("encrypted.pdf", "rb"))
# print(pdf_reader.isEncrypted)
# # print(pdf_reader.getPage(0))
# pdf_reader.decrypt("rosebud")
# print(pdf_reader.getPage(0))


# Copying pages
pdf1_file = open("meetingminutes.pdf", "rb")
pdf2_file = open("meetingminutes2.pdf", "rb")

pdf1_reader = PyPDF2.PdfFileReader(pdf1_file)
pdf2_reader = PyPDF2.PdfFileReader(pdf2_file)
pdf_writer = PyPDF2.PdfFileWriter()

for page_num in range(pdf1_reader.numPages):
    page_obj = pdf1_reader.getPage(page_num)
    pdf_writer.addPage(page_obj)
