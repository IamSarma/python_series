from PIL import Image, ImageDraw, ImageFont
import os


# Creating image object
new_image = Image.new("RGBA", (200, 200), "white")

# Creating image draw object
# draw_obj = ImageDraw.Draw(new_image)

# Make a thin black outline at the edges of the image
# draw_obj.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill="black")

# Draw a blue rectangle
# draw_obj.rectangle((20, 30, 60, 60), fill="blue")

# Draw a red ellipse
# draw_obj.ellipse((120, 30, 160, 60), fill="red")

# Draw a brown polygon
# draw_obj.polygon(((57, 85), (79, 62), (94, 85),
#                  (120, 90), (103, 113)), fill="brown")

# Drawing a pattern of green lines using loop
# for i in range(100, 200, 10):
#     draw_obj.line([(i, 0), (200, i - 100)], fill="green")

# Save the resulting image
# new_image.save("drawing_img.png")


# Drawing Text
draw_obj = ImageDraw.Draw(new_image)
draw_obj.text((20, 150), "Hello", fill="purple")

# Applying font(s) to the text
fonts_folder = "C:\\Windows\\Fonts"
dank_mono_font = ImageFont.truetype(
    os.path.join(fonts_folder, "Arial.ttf"), 30)
draw_obj.text((100, 150), "Python", fill="gray", font=dank_mono_font)

# Save the resulting image
new_image.save("text_on_image.png")
