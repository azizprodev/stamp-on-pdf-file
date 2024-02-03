# import pdf library PyPDF2
import PyPDF2

# read and open the pdf file
template = PyPDF2.PdfReader(open("pdf_files/sample.pdf", "rb"))
stamp = PyPDF2.PdfReader(open("pdf_files/stamp.pdf", "rb"))

# write the file
output = PyPDF2.PdfWriter()

# loop do following tasks:
# 1. iterate every page of template
# 2. add stamp on each page of template
# 3. finally add stamp pages to ouput file


for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(stamp.pages[0])
    output.add_page(page)

with open("pdf_files/sample_stamp.pdf", "wb") as file:
    output.write(file)




