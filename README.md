⚙️ Sistema de Cadastro Automatizado

📝 Resumo

Este sistema foi desenvolvido para empresas que necessitam realizar muitos cadastros repetitivos. O objetivo principal foi automatizar o processo de preenchimento, reduzindo o tempo necessário para concluir os cadastros. Antes da automação, esse processo levava de 3 a 5 horas para ser feito manualmente, mas com o sistema, ele pode ser concluído em aproximadamente 30 minutos.

O sistema utiliza o módulo PyAutoGUI para controlar o mouse e o teclado, preenchendo automaticamente os campos dos formulários conforme os dados fornecidos em um arquivo Excel.

🛠️ Tecnologias Utilizadas
PyAutoGUI: Para automação de tarefas, movimentando o mouse e preenchendo campos.

Pandas: Para manipulação e leitura dos dados provenientes do Excel.

Tkinter: (Caso o sistema tenha interface gráfica, mas não foi mencionado diretamente no código fornecido).

Keyboard: Para detectar a tecla ESC e permitir a interrupção segura do processo.

Configuração em Arquivo JSON: Para manter variáveis e dados de configuração de forma persistente.

🧑‍💻 Como Funciona o Sistema
Leitura de Dados (Excel): O sistema começa lendo os dados do arquivo Excel (especificamente da planilha Planilha1), que contém os dados a serem preenchidos nos formulários.

Automação de Preenchimento de Formulários: Com os dados lidos, o sistema preenche automaticamente os formulários no sistema-alvo utilizando o PyAutoGUI. O código mapeia as posições de clique para cada campo do formulário e preenche os valores.

Cálculo de Horas: O sistema continua executando enquanto houver produtos para cadastrar. O ciclo de preenchimento se repete até que todos os dados sejam inseridos.

🚀 Instruções para Executar o Sistema
Passo 1: Configuração do Ambiente
Instalar as Dependências:

O sistema requer Python 3.x e as bibliotecas PyAutoGUI, keyboard e pandas. Instale as dependências com o seguinte comando:
```
pip install pyautogui keyboard pandas
```
Arquivo de Dados (Excel):
Certifique-se de que o arquivo Dados.xlsx esteja na pasta correta, contendo a planilha com os dados que serão preenchidos nos formulários.

Configuração (config.py):
As variáveis de configuração, como dados de login ou outros parâmetros específicos, devem ser definidos no arquivo config.py.

Passo 2: Executando o Sistema
Iniciar o Sistema:
Para rodar o sistema, basta executar o script SIADV2.py:
```
python SIADV2.py
```
Processo de Cadastro:
O sistema vai automaticamente começar a preencher os formulários, um a um, com os dados fornecidos.

Caso seja necessário interromper o processo, basta pressionar a tecla ESC no teclado. O sistema será interrompido e uma mensagem de alerta será exibida.

🧮 Funções Principais
preencher_formulario(dados, numero_formulario): Função principal para preencher os formulários com os dados de cada produto. Ela navega através de todos os campos e preenche as informações necessárias.

verificar_esc(numero_formulario): Função para verificar se a tecla ESC foi pressionada. Caso tenha sido, o sistema é interrompido e uma mensagem de alerta é mostrada.

salvar_dados(dados): Função para salvar as informações em um arquivo JSON, permitindo persistir as configurações ou dados críticos.

carregar_dados(): Função que carrega os dados salvos anteriormente, caso seja necessário retomar o processo de preenchimento.

calcular_saldo_horas_na_casa(dados, mes, ano, dia, chegada, saida): Função que calcula o saldo de horas extras ou faltantes, ajustando com base nas horas trabalhadas em cada dia.

📋 Exemplo de Funcionamento
Dados de Produto no Excel:

Os dados a serem preenchidos nos formulários são lidos de um arquivo Excel, onde cada linha contém informações sobre os produtos e seus detalhes.
| item | código | lote | vencimento | cst | cfop | quantidade | preço |
| ---- | ------ | ---- | ---------- | --- | ---- | ---------- | ----- |
| 1    | 12345  | A1   | 01/12/2025 | 01  | 5102 | 10         | 100   |

Ciclo de Preenchimento:
Para cada produto, o sistema:
Clica no campo do formulário.
Preenche o código do produto, lote, quantidade, preço, e outros dados.
Ao final, clica em OK para salvar as informações do produto.

Finalizando o Processo:
O processo de preenchimento é repetido até que todos os dados sejam registrados.
Após o término, o sistema exibe uma mensagem de sucesso.
