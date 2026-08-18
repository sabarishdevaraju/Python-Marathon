import img2pdf

image_path="/home/sabarix/selfmade-ninja/python-marathon-july-2026/image1.jpg"
pdf_path="/home/sabarix/selfmade-ninja/python-marathon-july-2026/image1.pdf"

with open(pdf_path, "wb") as f:
    f.write(img2pdf.convert(image_path))