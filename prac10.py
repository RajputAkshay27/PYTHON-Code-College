import img2pdf 
from PIL import Image
img_path = "result.jpeg"
pdf_path = "20cs069result.pdf"
image = Image.open(img_path)
pdf_bytes = img2pdf.convert(image.filename)
file = open(pdf_path, "wb")
file.write(pdf_bytes)
image.close()

file.close()
print("Successfully made pdf file")