from utils import is_leetcode_open, enviar_para_clipboard
from problem_reader import copy_problem_text
from gpt_solver import gerar_solucao
import keyboard
import time
import ctypes

# Oculta o console
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def on_trigger():
    if not is_leetcode_open():
        return

    print("Capturando problema...")
    problema = copy_problem_text()
    print("Enviando para GPT...")
    resposta = gerar_solucao(problema)
    print("Copiando resposta para clipboard.")
    enviar_para_clipboard(resposta)
    print("Feito!")

keyboard.add_hotkey('ctrl+alt+l', on_trigger)
keyboard.wait()
