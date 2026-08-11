import pyautogui
from datetime import datetime

def take_screenshot():
    filename = f"screenshot_{datetime.now().strftime('%H%M%S')}.png"
    path = f"C:/Users/lenovo/astra-assistant/screenshots/{filename}"

    pyautogui.screenshot(path)
    return path