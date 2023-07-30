from PyPDF2 import PdfWriter, PdfReader
from getpass import getpass


file = "encrypt_pdf/cz.pdf"

pdfwriter = PdfWriter()
pdf = PdfReader(file)

for page in range(len(pdf.pages)):
    pdfwriter.add_page(pdf.pages[page])

password = getpass(prompt="Enter a password: ")
pdfwriter.encrypt(password)

with open(file, "wb") as f:
    pdfwriter.write(f)
