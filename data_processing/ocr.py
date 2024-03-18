import matplotlib.pyplot as plt
import numpy as np
import pytesseract
from pdf2image import convert_from_path
from PIL import Image


# Convert the pages of the PDF 
pdf_path = 'constitucion_5.pdf'
pages = convert_from_path(pdf_path, first_page=56, last_page=56)

text = [pytesseract.image_to_string(image=page, lang='spa') for page in pages]

# Change file text according to pages
with open('carta_antes_empezar_constitucion_spanish.txt', 'w') as f:
    for item in text:
        f.write("%s\n" % item)
        