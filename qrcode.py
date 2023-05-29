import qrcode

def generate_qr_code(link,name):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)
    qr.add_data(link)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save(name+".png")
    return True

# Example usage
link= input("Enter ur url which u want to qrcode!")
name=input("Enter the name for QR code!")
if generate_qr_code(link,name)==True:
    print("QR code generated successfully!")
else:
    print("Occurring Error while creating QR code!")