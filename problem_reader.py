import pyautogui
import time
import pyperclip

def copy_problem_text():
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    texto = pyperclip.paste()
    return texto
