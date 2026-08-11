import pyautogui
import pytesseract
from PIL import Image
from datetime import datetime

# Agar PATH me nahi hai to ye line uncomment karo
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 👇 Ye line add karo
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def read_screen_text():
    filename = f"screen_{datetime.now().strftime('%H%M%S')}.png"

    path = f"C:/Users/lenovo/astra-assistant/screenshots/{filename}"

    screenshot = pyautogui.screenshot()
    screenshot.save(path)

    text = pytesseract.image_to_string(Image.open(path), lang="eng")

    return text[:4000]