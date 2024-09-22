import qrcode
from PIL import Image  # pil file

QRcode = qrcode.QRCode(  # version for error checking
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=5
)
QRcode.add_data("https://github.com/Ramjikumarcom")  # add data
QRcode.make(fit=True)  # checking for given data
img = QRcode.make_image(fill_color="black", back_color="white")  # making image
img.save("Github.png")  # save image
