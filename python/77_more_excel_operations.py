import openpyxl
from openpyxl.styles import Font

# Setting the font style of cells
wb = openpyxl.Workbook()
sheet = wb["Sheet"]
italic_24_font = Font(size=24, italic=True)
sheet["A1"] = "Python is awesome!!!"
sheet["A1"].font = italic_24_font
wb.save("styles.xlsx")
