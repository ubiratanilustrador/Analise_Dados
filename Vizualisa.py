'''
Primeiro programa panda
'''
# Importa a biblioteca Pandas
import pandas as pd 

# Carrega dados de um arquivo de planilha de dados
df = pd.read_excel("dados_comercio.ods")

# Exibe as primeiras linhas do DataFrame
print(df.head())
