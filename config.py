import pandas as pd

# Carregar o arquivo Excel
file_path = 'C:/Users/vitor.santana/Desktop/SystemAutomação 115 - Copia/Dados.xlsx'

# Ler a planilha
df = pd.read_excel(file_path, sheet_name='Planilha1')

# Limpar e organizar os dados para extrair as colunas corretas
df_cleaned = df.iloc[3:]  # Remover as 3 primeiras linhas (cabeçalho incorreto)
df_cleaned.columns = [
    'item', 'codigo', 'lote', 'vencimento', 'cst', 'cfop', 'quantidade', 'preco'
]  # Definir os nomes das colunas corretamente

# Remover qualquer linha com valores nulos
df_cleaned.dropna(inplace=True)

# Estruturar os dados no formato desejado
formularios = [
    {
        'cliente': 'LUZ',
        'cfop': '5102',
        'vendedor': 'TOP VIDA',  # Ajuste conforme necessário
        'televenda': 'TOP VIDA',  # Ajuste conforme necessário
        'transportadora': 'TOP VIDA',  # Ajuste conforme necessário
        'naturezaoperacao': 'VENDA ESTADUAL - BA',  # Ajuste conforme necessário
        'observacao': 'P.E. N. 008/2024 (PENSO) PROC. ADM. N. 026/2024 (LOTE 08) VENC. DO CONTRATO EM 08/10/2025',
        'comentario': 'Confecção a pedido de Adenildes, em 15/05/2025.',  # Ajuste conforme necessário
        'user': '83',
        'password': '220315',
        'produtos': [
            {
                'codigo': str(row['codigo']),
                'lote': row['lote'],
                'data': pd.to_datetime(row['vencimento'], format='%d/%m/%Y').strftime('%d%m%Y'),
                'st_tributaria': row['cst'],
                'cfop2': str(row['cfop']),  # Assegurando que CFOP é tratado como string
                'quantidade': str(row['quantidade']),
                'preco': str(row['preco'])
            }
            for index, row in df_cleaned.iterrows()
        ]
    }
]

# Verificando a estrutura do formulário
print(formularios)
