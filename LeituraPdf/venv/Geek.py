
from PyPDF2 import PdfReader

reader = PdfReader('D:\\Meu Python\\LeituraPdf\\venv\\check.pdf')
page = reader.pages[0]
# print(page.values())
# print(page.extract_text())
# print(page.extractText())
print(page._extract_text(pdf = reader))
