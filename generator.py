#
#pip install qrcode Pillow

import qrcode
# Prepare data
data = "https://google.com"
# Generate QR code
image = qrcode.make(data=data)
# Show generate QR code
image.show()
# Save it
image.save("google_qr_code.jpg")
