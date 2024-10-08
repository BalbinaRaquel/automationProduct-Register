# Projeto: Automação Python

# Use-Case: Automatizar Cadastro de produtos no site da empresa. 



# Step 01: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login 
import time

import pyautogui
pyautogui.PAUSE = 1.0

pyautogui.press('win')

pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(1)

evidencia_01 = pyautogui.screenshot()
evidencia_01.save('evidencia_01.png')

# Step 02: Fazer login

time.sleep(2)

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3)
evidencia_02 = pyautogui.screenshot()
evidencia_02.save('evidencia_02.png')


pyautogui.click(x=460, y=382)
pyautogui.write('powerup_python@mail.com')

pyautogui.press('tab')
pyautogui.write('powerUp1891')

time.sleep(2)
evidencia_03 = pyautogui.screenshot()
evidencia_03.save('evidencia_03.png')

pyautogui.click(x=679, y=530)










# Step 03: Importar a base de dados




# Step 04: Cadastrar o primeiro produto

# Step 05: Repetir o processos de cadastro até finalizar a lista de produtos a serem cadastrados 

