import openpyxl
from openpyxl.styles import Font

# Setting the font style of cells
wb = openpyxl.Workbook()
sheet = wb["Sheet"]
# italic_24_font = Font(size=24, italic=True)
# sheet["A1"] = "Python is awesome!!!"
# sheet["A1"].font = italic_24_font
# wb.save("styles.xlsx")


# Font objecct(s)
font_obj_1 = Font(name="Times New Roman", bold=True)
sheet["A1"] = "Bold Times New Roman"
sheet["A1"].font = font_obj_1
