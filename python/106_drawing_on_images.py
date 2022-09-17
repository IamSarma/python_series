from PIL import Image, ImageDraw


# Creating image object
new_image = Image.new("RGBA", (200, 200), "white")


# Creating image draw object
draw_obj = ImageDraw.Draw(new_image)


# Make a thin black outline at the edges of the image
draw_obj.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill="black")


# Save the resulting image
new_image.save("drawing_img.png")
