from PIL import Image, ImageDraw


# Creating image object
new_image = Image.new("RGBA", (200, 200), "white")


# Creating image draw object
img_draw_obj = ImageDraw.Draw(new_image)
