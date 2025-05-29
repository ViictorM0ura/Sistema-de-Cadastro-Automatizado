import pyautogui
import time
import keyboard
import sys
import config  # Importando as variáveis de configuração

def alerta(msg):
    pyautogui.alert(msg)

def verificar_esc(numero_formulario):
    if keyboard.is_pressed('esc'):
        alerta(f"O sistema foi interrompido no formulário número {numero_formulario}")
        sys.exit()

def preencher_formulario(dados, numero_formulario):
    try:
        # Início do cadastro
        pyautogui.click(414,119, duration=1.5)  # 1 - Incluir
        pyautogui.click(851,413, duration=1.5)  # 2 - clicar em sim
        pyautogui.click(847,226, duration=1.5)  # 3 - clicar em cliente/fornecedor
        pyautogui.click(473,192, duration=1.5)  # 4 - clicar em pesquisar
        pyautogui.write('%')  #5 Envia o símbolo '%'
        pyautogui.write(dados['cliente'])  #6 Digitar o nome do cliente
        pyautogui.press('enter')  #7 - Aperta enter
        pyautogui.press('enter')  #8 - Aperta enter

        pyautogui.click(413,271, duration=1.5)  #9 CFOP1
        pyautogui.write(dados['cfop'])  #10 Digitar CFOP
        pyautogui.press('enter')  #11 - Aperta enter

        pyautogui.click(505,392, duration=1.5)  #12 Clicar em vendedor
        pyautogui.click(748,234, duration=1.5)  #13 clicar em pesquisar
        pyautogui.write(dados['vendedor'])  #14 Digitar
        pyautogui.press('enter')  #15 - Aperta enter
        pyautogui.press('enter')  #16 - Aperta enter
        pyautogui.press('enter')  #17 - Aperta enter

        pyautogui.click(727,394, duration=1.5)  #18 Clicar em Televenda
        pyautogui.click(750,236, duration=1.5)  #19 clicar em pesquisar
        pyautogui.write(dados['televenda'])  #20 Digitar
        pyautogui.press('enter')  #21 - Aperta enter
        pyautogui.press('enter')  #22 - Aperta enter
        pyautogui.press('enter')  #23 - Aperta enter

        pyautogui.click(1025,393, duration=1.5)  #24 Clicar em transportadora
        pyautogui.click(567,188, duration=1.5)  #25 clicar em pesquisar
        pyautogui.write(dados['transportadora'])  #26 Digitar
        pyautogui.press('enter')  #27 - Aperta enter
        pyautogui.press('enter')  #28 - Aperta enter

        pyautogui.click(410,552, duration=1.5)  #29 Clicar em frete
        pyautogui.click(396,582, duration=1.5)  #30 Clicar em CIF

        pyautogui.click(510,176, duration=1.5)  #31 Clicar em Dados complementares
        pyautogui.click(368,313, duration=1.5)  #32 Clicar em natureza da operação
        pyautogui.write(dados['naturezaoperacao'])  #33 Digitar

        pyautogui.click(732,175, duration=1.5)  #34 observações/messagens
        pyautogui.click(456,223, duration=1.5)  #35 observação/mensagem 1
        pyautogui.write(dados['observacao'])  #36 Digitar
        pyautogui.click(630,181, duration=1.5)  #37 clicar em itens

        # Início de cadastro dos produtos
        for produto in dados['produtos']:  # Loop para cadastrar todos os produtos
            pyautogui.click(406,219, duration=1.5)  #38 clicar em inserir cod
            pyautogui.write(produto['codigo'])  #39 Digitar código do produto
            pyautogui.press('enter')  #40 - Aperta enter
            pyautogui.press('enter')  #41 - Aperta enter
            pyautogui.write(produto['lote'])  #42 Digitar lote
            pyautogui.press('enter')  #43 - Aperta enter
            pyautogui.press('enter')  #44 - Aperta enter
            pyautogui.write(produto['data'])  #45 Digitar data
            pyautogui.press('enter')  #46 - Aperta enter
            pyautogui.write(produto['st_tributaria'])  #47 Digitar ST tributária
            pyautogui.press('enter')  #48 - Aperta enter
            pyautogui.write(produto['cfop2'])  #49 Digitar CFOP
            pyautogui.press('enter')  #50 - Aperta enter
            pyautogui.press('enter')  #51 - Aperta enter
            pyautogui.write(produto['quantidade'])  #52 Digitar quantidade
            pyautogui.press('enter')  #53 - Aperta enter
            pyautogui.write(produto['preco'])  #54 Digitar preço
            pyautogui.press('enter')  #55 - Aperta enter
            pyautogui.click(997,295, duration=1.5)  #56 Clicar em ok
        # Fim do cadastro de produtos

        # Movimentos finais
        pyautogui.click(458,123, duration=1.5)  #57 clicar
        pyautogui.click(772,412, duration=1.5)  #58 clicar
        pyautogui.click(363,123, duration=1.5)  #59 clicar
        pyautogui.click(564,369, duration=1.5)  #60 clicar
        pyautogui.click(637,406, duration=1.5)  #61 clicar
        pyautogui.click(491,400, duration=1.5)  #62 clicar
        pyautogui.write(dados['comentario'])  #63 Digitar

        pyautogui.click(500,481, duration=1.5)  #64 clicar
        pyautogui.write(dados['user'])  #63 Digitar
        pyautogui.click(567,476, duration=1.5)  #66 clicar
        pyautogui.write(dados['password'])  #63 Digitar
        pyautogui.click(684,508, duration=1.5)  #68 clicar

    except Exception as e:
        alerta(f"Ocorreu um erro no formulário {numero_formulario}")
        sys.exit()

# Loop para preencher todos os formulários
for numero_formulario, formulario in enumerate(config.formularios, start=1):
    preencher_formulario(formulario, numero_formulario)
    time.sleep(2)  # Aguarda 2 segundos antes de preencher o próximo formulário
