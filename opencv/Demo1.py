import cv2

# Loading image from a file
image = cv2.imread('opencv/img.jpg')

# Displaying an image in a window
# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Converting an image to grayscale form
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Displaying the grayscale image
# cv2.imshow('Gray Image', gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Applying Canny edge detection (a simple edge detection method)
# edges = cv2.Canny(gray_image, 50, 150)
# # Displaying the edge-detected image
# cv2.imshow('Edges', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Resizing the image
# width=500
# height=600
# resized_image = cv2.resize(image, (width, height))

# # Rotating the image by 45 degrees
# rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)
# rotated_image = cv2.warpAffine(resized_image, rotation_matrix, (width, height))

# # Displaying the resized and rotated images
# cv2.imshow('Resized Image', resized_image)
# cv2.imshow('Rotated Image', rotated_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()