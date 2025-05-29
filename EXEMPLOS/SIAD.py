import pyautogui
from time import sleep

#1 clicar em cadastros
pyautogui.click(22,34, duration=2)
#2 clicar em produtos
pyautogui.click(56,261, duration=2)
#3 clicar em cadastros
pyautogui.click(284,257, duration=2)
#4 apertar o enter
pyautogui.press('enter')
#5 clicar em código de barra e inserir
pyautogui.click(526,195, duration=2)
pyautogui.write('1234567789')
#6 clicar em descrição de venda e inserir
pyautogui.click(506,233, duration=2)
pyautogui.write('PRODUTO DE VACINA ETC')
#7 clicar em compras
pyautogui.click(505,270, duration=2)
#8 clicar em Marca e inserir
pyautogui.click(701,309, duration=2)
pyautogui.write('TOPVIDA')
#9 clicar em descrição nota fiscal e inserir
pyautogui.click(471,347, duration=2)
pyautogui.write('PRODUTO DE VACINA ETC (TOPVIDA)')
#10 clicar na lupa de unidade
pyautogui.click(1006,381, duration=2)
#11 clicar em inserir UNI
pyautogui.click(691,189, duration=2)
pyautogui.write('%')  # Envia o símbolo '%' normalmente
pyautogui.keyDown('shift')  # Pressiona a tecla Shift
pyautogui.write('UNIDADE')  # Envia a palavra 'UNIDADE' em maiúsculas
pyautogui.keyUp('shift')  # Solta a tecla Shift
#12 APERTAR ENTER
pyautogui.press('enter')
#13 CLICAR EM UNIDADES
# pyautogui.click(593,265, duration=2)
#14 ENTER
pyautogui.press('enter')
#15 grupo de produtos
pyautogui.click(1008,423, duration=2)
pyautogui.click(765,237, duration=2)
pyautogui.write('016.001')
pyautogui.press('enter')
pyautogui.press('enter')
#16 indrustia
pyautogui.click(985,511, duration=2)
pyautogui.click(716,235, duration=2)
pyautogui.write('TOP VIDA')
pyautogui.press('enter')
pyautogui.press('enter')
#17 por produto / Paramêtro
pyautogui.click(426,151, duration=2)
pyautogui.click(599,344, duration=2)
pyautogui.click(435,182, duration=2)
#18 fiscal
pyautogui.click(383,379, duration=2)
pyautogui.click(383,397, duration=2)
pyautogui.click(1000,213, duration=2)
pyautogui.click(604,195, duration=2)
pyautogui.write('%')  # Envia o símbolo '%' normalmente
pyautogui.write('Outros agulhas tubulares de metal')
pyautogui.press('enter')
pyautogui.press('enter')
#19 Diversos
pyautogui.click(478,179, duration=2)
pyautogui.click(395,385, duration=2)
pyautogui.write('9999999999999')
#20 fornecedores
pyautogui.click(537,179, duration=2)
pyautogui.click(1004,237, duration=2)
pyautogui.click(752,236, duration=2)
pyautogui.write('TOP VIDA')
pyautogui.press('enter')
pyautogui.press('enter')
#21 por empresas / diversos
pyautogui.click(502,151, duration=2)
pyautogui.click(483,175, duration=2)
pyautogui.click(753,505, duration=2)
pyautogui.click(642,185, duration=2)
pyautogui.write('PENSO')
pyautogui.press('enter')
pyautogui.press('enter')
#22 fiscais nova
pyautogui.click(679,177, duration=2)
pyautogui.click(416,238, duration=2)
pyautogui.write('1')
pyautogui.press('enter')
pyautogui.click(428,289, duration=2)
pyautogui.write('7')
pyautogui.press('enter')