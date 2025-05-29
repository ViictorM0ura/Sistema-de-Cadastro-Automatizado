import pyautogui
from time import sleep

# 1 - Clicar e digitar meu usuário
pyautogui.click(686,386, duration=2)  # Coordenadas do campo de usuário
pyautogui.write('vitor')  # Digitar meu usuário
# 2 - Clicar e digitar minha senha
pyautogui.click(697,410, duration=2)  # Coordenadas do campo de usuário
pyautogui.write('123456')  # Digitar meu usuário
# 3 - Clicar em entrar
pyautogui.click(581,443, duration=2)  # Coordenadas do campo de usuário
# 4 - Extrair cada produto
with open ('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        # 1- clicar e digitar produto
        pyautogui.click(424,370, duration=2)  # Coordenadas do campo de usuário
        pyautogui.write(produto)  # Digitar meu usuário
        # 2- clicar e digitar quantidade
        pyautogui.click(424,397, duration=2)  # Coordenadas do campo de usuário
        pyautogui.write(quantidade)  # Digitar meu usuário
        # 3- clicar e digitar preço
        pyautogui.click(423,425, duration=2)  # Coordenadas do campo de usuário
        pyautogui.write(preco)  # Digitar meu usuário
        # 4- clicar em registrar
        pyautogui.click(315,588, duration=2)  # Coordenadas do campo de usuário
        sleep(1)  # Esperar 1 segundos para o registro ser feito