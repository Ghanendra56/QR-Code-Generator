import qrcode
import image
qr = qrcode.QRCode(
    version= 10,
    box_size= 10,
    border= 5,
)

data = "https://discord.com/users/780327720214069308"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("qrcode.png")