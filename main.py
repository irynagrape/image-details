img=Image.open('ZZZENDOFFILE.png')

# The file format of the source file.

print(img.format) # Output: JPEG



# The pixel format used by the image.

#Typical values are "1", "L", "RGB", or "CMYK."

print(img.mode) # Output: RGB



# Image size, in pixels.

print(img.size) # Output: (1920, 1280)



print(img.palette) # Output: None

