####################################################################
#
#     Melissa Holmes, Fall 2025
#     Experimenting with Pillow for introductory Python classes
#
####################################################################

from PIL import Image
from PIL import ImageEnhance  #needed for color enhancement


# Location of the image
# Your python file should be saved in the same location
img = Image.open("waterfall01.jpg")

# this opens the default image viewer installed on your computer
img.show()

# print some info about the image file
print(img.size)   # size of the image
print(img.format) # format of the image

# save image size in variables
width, height = img.size

# set points for cropping.  You can calculate, as shown below.
left = 600
top = height / 5
right = 1000
bottom = 3 * height / 5

# Crop the image.  This creates a new image and
# will not modify the original image.
im1 = img.crop((left, top, right, bottom))

# Resize the new image.
newsize = (300, 300)
im1 = im1.resize(newsize)
im1.show()

# Color enhancement - brightness
curr_bri = ImageEnhance.Brightness(im1)
new_bri = 2.5

# Brightness enhanced by a factor of 2.5
im1 = curr_bri.enhance(new_bri)

# Save the new image.  You will see a new image in your folder.
# Caution:  the extension must represent a valid image type.
im1.save("resized_im1.jpg")

im1.show()
