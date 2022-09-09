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
# pdf1_file = open("meetingminutes.pdf", "rb")
# pdf2_file = open("meetingminutes2.pdf", "rb")

# pdf1_reader = PyPDF2.PdfFileReader(pdf1_file)
# pdf2_reader = PyPDF2.PdfFileReader(pdf2_file)
# pdf_writer = PyPDF2.PdfFileWriter()

# for page_num in range(pdf1_reader.numPages):
#     page_obj = pdf1_reader.getPage(page_num)
#     pdf_writer.addPage(page_obj)

# for page_num in range(pdf1_reader.numPages):
#     page_obj = pdf2_reader.getPage(page_num)
#     pdf_writer.addPage(page_obj)

# pdf_output_file = open("combinedminutes.pdf", "wb")
# pdf_writer.write(pdf_output_file)
# pdf_output_file.close()
# pdf1_file.close()
# pdf2_file.close()


# Rotating pages
# minutes_file = open("meetingminutes.pdf", "rb")
# pdf_reader = PyPDF2.PdfFileReader(minutes_file)
# page = pdf_reader.getPage(0)
# page.rotateClockwise(90)

# pdf_writer = PyPDF2.PdfFileWriter()
# pdf_writer.addPage(page)

# result_pdf_file = open("rotated_page.pdf", "wb")
# pdf_writer.write(result_pdf_file)
# result_pdf_file.close()
# minutes_file.close()


# Overlaying pages
minutes_file = open("meetingminutes.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(minutes_file)
minutes_first_page = pdf_reader.getPage(0)

pdf_watermark_reader = PyPDF2.PdfFileReader(open("watermark.pdf", "rb"))
minutes_first_page.mergePage(pdf_watermark_reader.getPage(0))

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(minutes_first_page)

for page_num in range(1, pdf_reader.numPages):
    page_obj = pdf_reader.getPage(page_num)
    pdf_writer.addPage(page_obj)

result_pdf_file = open("watermarked_cover.pdf", "wb")
pdf_writer.write(result_pdf_file)
result_pdf_file.close()
minutes_file.close()
