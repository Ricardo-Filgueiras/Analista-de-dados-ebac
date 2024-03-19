# Criando script python... 

import os
import pandas as pd
import seaborn as sns

# Abrindo arquivo Csv com pandas 
gs_df = pd.read_csv('/content/da-ebac/gasolina.csv')
gs_df

gs_df.describe()

# Criando grafico gasolinafig.png

with sns.axes_style('whitegrid'):

  gf = sns.lineplot(data=gs_df, x='dia', y='venda')
  gf.set(title='Preço Gasolina Primeiros 10 dias Jun/2021', xlabel='Dias', ylabel='Preço');

  gf.get_figure().savefig('gasolinafig.png')

# add gasolinafig.png ao repositorio com comandos git 
'''
!git add gasolinafig.png
!git status
'''