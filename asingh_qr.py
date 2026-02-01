import qrcode

# URL you want to open when QR is scanned
data = "https://github.com/dashboard"

# Generate QR code
img = qrcode.make(data)

# Save QR code to a fixed location (easy to find)
img.save(r"D:\github_dashboard_qr.png")

print("QR Code generated successfully!")
print("File saved at D:\\github_dashboard_qr.png")
