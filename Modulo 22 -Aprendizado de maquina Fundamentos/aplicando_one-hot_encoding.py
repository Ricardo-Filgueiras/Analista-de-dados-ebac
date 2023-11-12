# Aplicando  o one-hot encoding 
# lembrando esse script não faz parte do exercicios 
# estou apenas excercitando.

import pandas as pd
import numpy as np
import random


# cria um dataframe com uma variável categórica 
# criando df cores 

cor_df = pd.DataFrame({'cor': ['vermelho', 'verde', 'azul', 'vermelho', 'verde', 'azul', 'vermelho', 'azul', 'vermelho', 'verde', 'azul']})
print(cor_df)

# aplica o one-hot encoding 
one_hot = pd.get_dummies(cor_df['cor'])
print(one_hot)

# adiciona as novas variáveis binárias ao dataframe original 
cor_df = pd.concat([cor_df, one_hot], axis=1)

print(cor_df)


# Considere a criação de variáveis binárias para cada valor 
# cria um dataframe com uma variável categórica com muitos valores únicos 
frutas_df = pd.DataFrame({'fruta': ['maçã', 'banana', 'laranja', 'abacaxi', 'banana', 'maçã']})
print(frutas_df)


# cria as variáveis binárias 
frutas = pd.get_dummies(frutas_df['fruta']) 
frutas.columns = ['fruta_' + str(col) for col in frutas.columns]


# adiciona as novas variáveis binárias ao dataframe original 
frutas_df = pd.concat([frutas_df, frutas], axis=1)


print(frutas_df)