import qrcode

# GitHub repository URL
data = "https://github.com/AkshaySingh51203/qr-code"

# Generate QR code
img = qrcode.make(data)

# Save QR code image to D drive
img.save(r"D:\github_repo_qr.png")

print("QR Code generated successfully!")
print("File saved at D:\\github_repo_qr.png")
