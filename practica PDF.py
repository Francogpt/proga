import PyPDF2

with open('archivo.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)

