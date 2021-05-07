import PyPDF2
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(BASE_DIR, "Data")
pdf_filepath = os.path.join(files_dir, "Aubut_botin_2020.pdf")

pdf_file = open(pdf_filepath, 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
print (page_content)