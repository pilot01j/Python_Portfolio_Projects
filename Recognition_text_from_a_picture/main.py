# 1. pip install pytesseract
# 2. download and install Tesseract OCR from https://github.com/UB-Mannheim/tesseract/wiki
import pytesseract
from PIL import Image

# 3. open the image using opem func from Image pack
img_name = input("Write the img name: ")
img = Image.open(img_name)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 4. write config for image_to_string func, https://help.ubuntu.ru/wiki/tesseract
# all suported languages : https://github.com/tesseract-ocr/tessdata
# custom_config = r'--oem 3 --psm 13'

text_language = input('Write the text language (ex: fra, rus, rom: ')
text = pytesseract.image_to_string(img, lang=text_language)
print(text)

# 5.
file_name = img.filename
file_name = file_name.split('.')[0]
with open(f'{file_name}.txt', 'w') as text_file:
    text_file.write(text)
