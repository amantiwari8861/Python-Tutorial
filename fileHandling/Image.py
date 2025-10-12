from PIL import Image

# Open an image file
img = Image.open("C:\\Users\\admin\\Desktop\\cc.jpg")

# Display information about the image
print("Image format:", img.format)
print("Image size:", img.size)
print("Image mode:", img.mode)

# Show the image
img.show()

# Binary
# ASCII -> American standard code for information interchange 
# A -> 65
# B -> 66
# Z -> 90
# a -> 97
# z -> 122
# 0 -> 48
# 9 -> 57
# space -> 32

# from PIL import Image

# # Open an image file
# img = Image.open("image.jpg")

# # Rotate the image by 90 degrees
# img_rotated = img.rotate(90)

# # Save the rotated image to a new file
# img_rotated.save("image_rotated.jpg")
