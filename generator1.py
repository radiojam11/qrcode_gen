#
#pip install qrcode Pillow

import qrcode
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=3,
)
# Content
data = 'https://www.baidu.com/'
qr.add_data(data=data)
# Set color
qr.make(fit=True)
image = qr.make_image(fill_color='blue', back_color='white')
# Display QR code
image.show()
# Save it
image.save()
