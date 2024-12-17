
import pyautogui
import time

# Esperar um pouco antes de iniciar para o usuário se preparar
time.sleep(2)

# Apertar a tecla Windows
pyautogui.press("win")

# Esperar um pouco para o menu Iniciar aparecer
time.sleep(1)

# Digitar "Google"
pyautogui.write("Google")

# Esperar um instante para os resultados carregarem
time.sleep(1)

# Pressionar Enter
pyautogui.press("enter")
