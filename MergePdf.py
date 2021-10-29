import os
from PyPDF2 import PdfFileMerger

pdf_list = []
for pdf_file in list(os.walk("."))[0][2]:
    if not pdf_file.endswith("pdf"):
        continue
    pdf_list.append(pdf_file)
merger = PdfFileMerger()
for pdf in pdf_list:
    merger.append(open(pdf,'rb'))
with open("result.pdf", "wb") as fout:
    merger.write(fout)