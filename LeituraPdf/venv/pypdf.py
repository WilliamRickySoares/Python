from pypdf import PdfReader


reader = PdfReader(r'D:\Meu Python\LeituraPdf\venv\cert.pdf')
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
