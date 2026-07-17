import qrcode

data = input("Enter text: ")

img = qrcode.make(data)
img.save("qrcode.png")

print("QR Code Generated Successfully")