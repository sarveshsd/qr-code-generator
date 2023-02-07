
import qrcode 
import image
qr = qrcode.QRCode(
    version = 23,
    box_size = 10,
    border = 5
)
data = input("enter anything:")
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color="white")
img.save("test1.png")

