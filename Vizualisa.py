'''
Primeiro programa panda
'''

import pandas as pd  # Importa a biblioteca Pandas

# Carrega dados de um arquivo CSV
df = pd.read_excel("dados_comercio.ods")

# Exibe as primeiras linhas do DataFrame
print(df.head())
