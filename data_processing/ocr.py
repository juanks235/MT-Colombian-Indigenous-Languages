import matplotlib.pyplot as plt
import numpy as np
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

letters = {
    "Contenido_nasa":[8,11],
    "Presidente_nasa":[13],
    "Resguardo_nasa":[14],
    "Traductor_nasa":[15],
    "Coordinador_nasa":[16,18],
    "AntesEmpezar_nasa":[19],
    "Contenido_spanish":[47,48],
    "Presidente_spanish":[50],
    "Resguardo_spanish":[52],
    "Traductor_spanish":[53],
    "Coordinador_spanish":[54,55],
    "AntesEmpezar_spanish":[56]
}

pdf_path = 'constitucion_5.pdf'

def get_letters(letters,path):
    # Convert the pages of the PDF 

    for key in letters:
        print(key)
        if len(letters[key]) == 1:
            pag = letters[key][0]
            # The letter is longer than 1 page
            pages = convert_from_path(path, first_page=pag, last_page=pag)
        else:
            init = letters[key][0]
            end = letters[key][1]
            pages = convert_from_path(path, first_page=init, last_page=end)
        
        text = [pytesseract.image_to_string(image=page, lang='spa') for page in pages]
        # Change file text according to pages
        with open("letters/" + key + ".txt", 'w') as f:
            for item in text:
                if "\n\n" in item:
                    final = item.replace("\n\n","")
                f.write("%s"% final)
        
def get_articles(path):

    articles_pages = {
        "Art1-2-3-11-12-17-18-19-24-27-30-43-44_nasa":[21,26],
        "Art7-8-10-63-72-40_nasa":[29,32],
        "Art246_nasa":[35],
        "Art287-329-330_nasa":[37,41],
        "Art1-2-3-11-12-17-18-19-24-27-30-43-44_spanish":[58,59],
        "Art7-8-10-63-72-40-246-287-329-330_spanish":[61,65]

    }
    for key in articles_pages:
        if len(articles_pages[key])==1:
            pag = articles_pages[key][0]
            # The letter is longer than 1 page
            pages = convert_from_path(path, first_page=pag, last_page=pag)
        else:
            init = articles_pages[key][0]
            end = articles_pages[key][1]
            pages = convert_from_path(path, first_page=init, last_page=end)

        text = [pytesseract.image_to_string(image=page, lang='spa') for page in pages]
        # Change file text according to pages
        with open("articles/"+key+".txt", 'w') as f:
            for item in text:
                if "\n\n" in item:
                    final = item.replace("\n\n","")
                f.write("%s"% final)

#get_letters(letters)
get_articles(pdf_path)
