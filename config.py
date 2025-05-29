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
        'cliente': ' ',
        'cfop': ' ',
        'vendedor': ' ',  # Ajuste conforme necessário
        'televenda': ' ',  # Ajuste conforme necessário
        'transportadora': ' ',  # Ajuste conforme necessário
        'naturezaoperacao': ' ',  # Ajuste conforme necessário
        'observacao': ' ',
        'comentario': ' ',  # Ajuste conforme necessário
        'user': ' ',
        'password': '',
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
