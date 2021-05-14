from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\barai\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
text_from_image = pytesseract.image_to_string(Image.open('test_image2.png'))
print(text_from_image)