import os
from PIL import Image

# Location of the files to be converted
folder = ".\\to_convert"

for image in os.listdir(folder):
  # Prevents placeholder file from being read
  if ".empty" not in image:
    try:
      # Location of the image to be converted
      image_convert = Image.open(folder + "\\" + image)

      # Location of the output file
      image_convert.save("./converted/" + os.path.splitext(image)[0] + ".ico")

      print("Success! Converted \"" + image + "\" to \"" + os.path.splitext(image)[0] + ".ico\"")

    except Exception as e:
      print(e)
