import qrcode
# import sys
# sys.path.append("c:\\users\\admin\\appdata\\local\\programs\\python\\python310\\lib\\site-packages")

img = qrcode.make('https://chat.whatsapp.com/IKbmAx2fplnBTgCoRxW7FW')
# type(img)  # qrcode.image.pil.PilImage
img.save("MyQrCode.png")
print("Qr code generated")

# pip install qrcode
