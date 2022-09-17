from PIL import ImageColor, Image


# Getting RGBA values that user want to use
# print(ImageColor.getcolor("red", "RGBA"))
# print(ImageColor.getcolor("black", "RGBA"))
# print(ImageColor.getcolor("chocolate", "RGBA"))
# print(ImageColor.getcolor("aliceblue", "RGBA"))


# Creating image object
# self_img = Image.open("dp.png")


# Working with image data type
# print(self_img.size)
# print(self_img.filename)
# print(self_img.format)
# print(self_img.format_description)


# Save the image
# Conversion only required while saving RGBA file to jpg format
# self_img = self_img.convert("RGB")
# self_img.save("dp.jpg")


# Creating new image
# image_1 = Image.new("RGBA", (100, 200), "purple")
# image_1.save("purple_image.png")


# Creating new transparent image
# image_2 = Image.new("RGBA", (20, 20))
# image_2.save("transparent_image.png")


# Cropping image(s)
cat_image = Image.open("zophie.png")
# cropped_image = cat_image.crop((335, 345, 565, 560))
# cropped_image.save("cropped.png")


# Copying and pasting image(s) onto other image(s)
# cat_face_image = Image.open("cropped.png")
# cat_copy_image = cat_image.copy()
# cat_copy_image.paste(cat_face_image, (0, 0))
# cat_copy_image.paste(cat_face_image, (400, 500))
# cat_copy_image.save("pasted.png")


# Creating tiled image(s)
# cat_copy_image2 = cat_image.copy()
# cat_image_width, cat_image_height = cat_image.size
# cat_face_image_width, cat_face_image_height = cat_face_image.size

# for left in range(0, cat_image_width, cat_face_image_width):
#     for top in range(0, cat_image_height, cat_face_image_height):
#         cat_copy_image2.paste(cat_face_image, (left, top))

# cat_copy_image2.save("tiled.png")


# Resizing an image
# img_width, img_height = cat_image.size
# quarter_sized_img = cat_image.resize((int(img_width / 2), int(img_height / 2)))
# quarter_sized_img.save("quarter_sized.png")
# slender_sized_img = cat_image.resize((img_width, img_height + 300))
# slender_sized_img.save("slender_sized.png")


# Rotating and Flipping image(s)
cat_image.rotate(90).save("rotated_90.png")
cat_image.rotate(180).save("rotated_180.png")
cat_image.rotate(270).save("rotated_270.png")
