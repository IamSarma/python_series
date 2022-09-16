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
