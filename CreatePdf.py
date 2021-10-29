from fpdf import FPDF
import img2pdf
import PIL.Image
import os

for jpg_file in list(os.walk("."))[0][2]:
    if not jpg_file.endswith("jpg"):
        continue
    image = PIL.Image.open(jpg_file)
    pdf_bytes = img2pdf.convert(image.filename)
    pdf_file = jpg_file.replace(".jpg", ".pdf")
    file = open(".\\{}".format(pdf_file), "wb")
    file.write(pdf_bytes)
    image.close()
    file.close()