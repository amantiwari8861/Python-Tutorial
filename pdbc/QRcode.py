import qrcode
from PIL import Image
# The data you want to encode in the QR code
data = "https://github.com/amantiwari8861"

# Generate a QR code instance
qr = qrcode.QRCode(
    version=1,   # QR code version (integer from 1 to 40). Higher versions have more data capacity.
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level ('L', 'M', 'Q', 'H')
    box_size=10,  # Size of each box (pixels)
    border=4,     # Border size around the QR code (boxes)
)

# Add data to the QR code
qr.add_data(data)

# Make the QR code fit the data more efficiently
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("./my_qr_code.png")

# Optionally, you can also show the image using your default image viewer
img.show()

#pip install pillow
#pip install qrcode
