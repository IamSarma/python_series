import PyPDF2

pdf_file_obj = open("meetingminutes.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
print(pdf_reader.numPages)
