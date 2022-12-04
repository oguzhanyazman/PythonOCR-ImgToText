import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
###https://www.softpedia.com/get/Programming/Other-Programming-Files/Tesseract-OCR.shtml
#
# #download bunu indirip kurun

from PIL import Image

img = Image.open('3.png')
text = tess.image_to_string(img)

print(text)
