from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os

ROOT_DIR = os.path.abspath(os.curdir)

# Path of the pdf
PDF_file = "D:\Meu Python\LeituraPdf\cert.pdf"
# D:\Meu Python\LeituraPdf\pdf\ARQUIVO.pdf
''' 
Part #1 : Converting PDF to images 
'''

# Store all the pages of the PDF in a variable
pages = convert_from_path(PDF_file, 500, poppler_path = r'C:\poppler-0.68.0\bin')

image_file_list = []

text_file = out_directory / Path("out_text.txt")

