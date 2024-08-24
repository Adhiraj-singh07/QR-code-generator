import qrcode
import os

# Create a folder named 'images' if it doesn't exist
os.makedirs("images", exist_ok=True)

while True:
    # Prompt user for URL
    url = input("Enter a URL (or type 'exit' to quit): ")
    
    # Check if the user wants to exit
    if url.lower() == 'exit':
        break

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Save the image with a unique name
    file_name = f"images/qr_code_{url.replace('://', '_').replace('/', '_')}.png"
    qr_image.save(file_name)
    print(f"QR code saved as: {file_name}")
