from PIL import Image

# Open an image file
img = Image.open("image.jpg")

# Display information about the image
print("Image format:", img.format)
print("Image size:", img.size)
print("Image mode:", img.mode)

# Show the image
img.show()

from PIL import Image

# Open an image file
img = Image.open("image.jpg")

# Rotate the image by 90 degrees
img_rotated = img.rotate(90)

# Save the rotated image to a new file
img_rotated.save("image_rotated.jpg")
