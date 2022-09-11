import docx
import read_docx

doc = docx.Document("demo.docx")

# # Getting the length of the paragraphs in the document
# print(len(doc.paragraphs))

# # Getting text using index of the paragraphs object
# print(doc.paragraphs[0].text)
# print(doc.paragraphs[1].text)

# # Getting number of runs in the paragraphs object
# print(len(doc.paragraphs[1].runs))

# # Getting text from the runs object using index and text
# print(doc.paragraphs[1].runs[0].text)
# print(doc.paragraphs[1].runs[1].text)
# print(doc.paragraphs[1].runs[2].text)
# print(doc.paragraphs[1].runs[3].text)
# print(doc.paragraphs[1].runs[4].text)


# Extract and display full text from the given word document
# print(read_docx.getText("demo.docx"))


# Applying style(s)
print(doc.paragraphs[0].text)
print(doc.paragraphs[0].style)
doc.paragraphs[0].style = "Normal"

print(doc.paragraphs[1].text)
print(doc.paragraphs[1].runs[0].text,
      doc.paragraphs[1].runs[1].text,
      doc.paragraphs[1].runs[2].text,
      doc.paragraphs[1].runs[3].text,
      doc.paragraphs[1].runs[4].text)
doc.paragraphs[0].style = "QuoteChar"
doc.paragraphs[2].underline = True
doc.paragraphs[4].underline = True
