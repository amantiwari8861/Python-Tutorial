import qrcode
# import sys
# sys.path.append("c:\\users\\admin\\appdata\\local\\programs\\python\\python310\\lib\\site-packages")

img = qrcode.make('https://chat.whatsapp.com/HbqH4PyZ5PK7d8cL5kdp7j')
# type(img)  # qrcode.image.pil.PilImage
img.save("MyQrCode.png")
print("Qr code generated")

# pip install qrcode
