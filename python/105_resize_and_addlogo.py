#! python3
# resize_and_addlogo.py
# Resizes all image(s) in the current working directory to 300X300 square
# and adds catlogo.png to the lower-right corner
import os
from PIL import Image


# Instantiating required variable(s)
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = "catlogo.png"
logo_image = Image.open(LOGO_FILENAME)
logg_width, logo_height = logo_image.size


# Loop over all the file(s) in the working directory
for file_name in os.listdir("."):
    if not (file_name.endswith(".png") or file_name.endswith(".jpg")) or file_name == LOGO_FILENAME:
        continue
    target_img = Image.open(file_name)
    target_img_width, target_img_height = target_img.size

    # Check if image needs to be resized
    if target_img_width > SQUARE_FIT_SIZE and target_img_height > SQUARE_FIT_SIZE:
        # Calculate the new height and width to resize to
        if target_img_width > target_img_height:
            target_img_height = int(
                (SQUARE_FIT_SIZE / target_img_width) * target_img_height)
            target_img_width = SQUARE_FIT_SIZE
        else:
            target_img_width = int(
                (SQUARE_FIT_SIZE / target_img_height) * target_img_width)
            target_img_height = SQUARE_FIT_SIZE
        # Resize the image
        print(f"Resizing {file_name}")
        target_img = target_img.resize((target_img_width, target_img_height))
