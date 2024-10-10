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

time.sleep(2)
evidencia_04 = pyautogui.screenshot()
evidencia_04.save('evidencia_04.png')

time.sleep(2)

# Step 03: Importar a base de dados
import pandas as pd

tabela_dados = pd.read_csv('produtos.csv')


# Step 04: Cadastrar o primeiro produto
# Step 05: Repetir o processos de cadastro até finalizar a lista de produtos a serem cadastrados 


for linha in tabela_dados.index:
    time.sleep(1)
    pyautogui.click(x=499, y=283)
    time.sleep(1)

    codigo = tabela_dados.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    time.sleep(1)

    pyautogui.write(str(tabela_dados.loc[linha, "marca"]))
    pyautogui.press('tab')
    time.sleep(1)

    pyautogui.write(str(tabela_dados.loc[linha, 'tipo']))
    pyautogui.press('tab')
    time.sleep(1)

    pyautogui.write(str(tabela_dados.loc[linha, 'categoria']))
    pyautogui.press('tab')
    time.sleep(2)
   
    evidencia_05 = pyautogui.screenshot()
    evidencia_05.save('evidencia_05.png')

    pyautogui.write(str(tabela_dados.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    time.sleep(1)

    pyautogui.write(str(tabela_dados.loc[linha, 'custo']))
    pyautogui.press('tab')
    time.sleep(1)

    obs = tabela_dados.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press('tab')
    time.sleep(2)

    pyautogui.press('enter')
    pyautogui.scroll(5000)


time.sleep(2)
evidencia_06 = pyautogui.screenshot()
evidencia_06.save('evidencia_06.png')

pyautogui.scroll(-1000)

time.sleep(2)
evidencia_07 = pyautogui.screenshot()
evidencia_07.save('evidencia_06.png')










