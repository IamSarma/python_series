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
