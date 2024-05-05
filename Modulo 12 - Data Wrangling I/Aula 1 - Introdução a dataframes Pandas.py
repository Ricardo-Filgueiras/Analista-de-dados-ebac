# Para trabalhar o Data Wrangling vamos usar o pacote pandas 
# O que e um df ou dataFrame ?
# E um tipo de estrutura de dados 

import pandas as pd



transacoes = dict(
id= [571,572,573],
data=['19-01-2021','19-01-2021','23-01-2021'],
valor=[371.30,57.19,101.21],
categoria=['supermercado','farmacia','outros']
)

transacoes_df = pd.DataFrame(transacoes)

#transacoes_df
#print(transacoes_df) #retona o dataframe
print(type(transacoes_df)) # o tipo do nosso arquivo 
print(transacoes_df.columns)# retorna os nomes das colunas = Index 
print(transacoes_df.dtypes)# retorna os tipos de cada coluna  no dataframe 
print(transacoes_df.index)# 
print(transacoes_df.head(n=2)) # esse metodo tra as primeira linha 
print(transacoes_df.tail(n=1)) # esse metodo tras as ultimas linha de baixo pra cima 





