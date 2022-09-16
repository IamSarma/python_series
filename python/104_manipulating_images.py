from PIL import ImageColor, Image


# Getting RGBA values that user want to use
# print(ImageColor.getcolor("red", "RGBA"))
# print(ImageColor.getcolor("black", "RGBA"))
# print(ImageColor.getcolor("chocolate", "RGBA"))
# print(ImageColor.getcolor("aliceblue", "RGBA"))


# Creating image object
self_img = Image.open("dp.png")


# Working with image data type
print(self_img.size)
print(self_img.filename)
print(self_img.format)
print(self_img.format_description)


# Save the image
# Conversion only required while saving RGBA file to jpg format
self_img = self_img.convert("RGB")
self_img.save("dp.jpg")
