from PIL import Image

# Location of image to convert
png_image = Image.open("clippy - scaled.png")

# Name of output .ico file
png_image.save("clippy - scaled.ico")