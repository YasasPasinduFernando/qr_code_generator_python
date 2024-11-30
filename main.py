import qrcode

# Function to generate QR code
def generate_qrcode(data, filename="qrcode.png"):
  
    # Create QR Code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 is smallest).
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction.
        box_size=10,  # Size of each box in the QR Code grid.
        border=4,  # Thickness of the border (minimum is 4).
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(filename)
    print(f"QR Code saved as {filename}")

# Example usage
if __name__ == "__main__":
    data = input("Enter the data to encode in the QR Code: ")
    filename = input("Enter the filename to save the QR Code (e.g., 'my_qrcode.png'): ") or "qrcode.png"
    generate_qrcode(data, filename)
