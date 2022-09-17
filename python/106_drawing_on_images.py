from PIL import Image, ImageDraw


# Creating image object
new_image = Image.new("RGBA", (200, 200), "white")


# Creating image draw object
draw_obj = ImageDraw.Draw(new_image)


# Make a thin black outline at the edges of the image
draw_obj.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill="black")


# Draw a blue rectangle
draw_obj.rectangle((20, 30, 60, 60), fill="blue")


# Draw a red ellipse
draw_obj.ellipse((120, 30, 160, 60), fill="red")


# Save the resulting image
new_image.save("drawing_img.png")
