import pygetwindow as gw
import pyperclip

def is_leetcode_open():
    try:
        win = gw.getActiveWindow()
        return "LeetCode" in win.title
    except:
        return False

def enviar_para_clipboard(texto):
    pyperclip.copy(texto)
