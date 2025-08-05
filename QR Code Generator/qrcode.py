
import pyqrcode

method = input("Do you want want encode Text or URL?: ").strip()

if method == 'URL':
	# Prompt user to enter a URL
	url_input = input("Enter a URL (starting with http:// or https://): ").strip()

	# Basic validation to ensure it's a URL
	if not url_input.startswith(("http://", "https://")):
	    print("Invalid URL. Please include http:// or https://")
	else:
	    # Create QR code from the URL
	    qr = pyqrcode.create(url_input)
	    
	    # Show the QR code image (requires pypng)
	    qr.show()
	    
	    # Prompt user for filename (without extension)
	    filename = input("Enter a name to save the QR code image (without extension): ").strip()
	    qr.png(filename + ".png", scale=6)
	    
	    print(f"QR code saved as {filename}.png")

elif method == 'Text':
	# Creating QR code after given text "input"
	url = pyqrcode.create(input("Enter text to convert: "))
	# Saving QR code as a png file
	url.show()
	# Name of QR code png file "input"
	url.png(input("Enter image name to save: ") + ".png", scale=6)

	# Prompt user for filename (without extension)
  	filename = input("Enter a name to save the QR code image (without extension): ").strip()
    qr.png(filename + ".png", scale=6)
	    
