import docx

doc = docx.Document("demo.docx")
print(len(doc.paragraphs))
