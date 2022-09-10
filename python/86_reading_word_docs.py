import docx

doc = docx.Document("demo.docx")

# Getting the length of the paragraphs in the document
print(len(doc.paragraphs))

# Getting text using index of the paragraphs object
print(doc.paragraphs[0].text)
print(doc.paragraphs[1].text)


# Getting number of runs in the paragraphs object
print(len(doc.paragraphs[1].runs))
