import numpy as np
import pandas as pd
import seaborn as sns


data = pd.read_csv('exam.csv')


data.head(n=3)
#print(data.head(n=3))

#teste em de grafico para escrip python não faz parte de excercicio 
'''with sns.axes_style('whitegrid'):

  grafico = sns.scatterplot(x=data['math'], y=data['writing'])
  grafico.set(title='Scatterplot de math by writing', xlabel='math', ylabel='writing');
  grafico.get_figure().savefig('mathOfWriting.png')
'''


data[['ethnicity','lunch','sex']].head()
#print(data[['ethnicity','lunch','sex']].head())

# categoria nominal, separa a categorico do seguinte maneira não levaria 
# ao resultado de que e "M" seria maior que "F", se "f"fosse atribuido a 0 ?
data['sex_norm'] = data['sex'].apply(lambda sex: 1 if sex == 'M' else 0)

data['sex_m'] = data['sex'].apply(lambda sex: 1 if sex == 'M' else 0 )
data['sex_f'] = data['sex'].apply(lambda sex: 1 if sex == 'F' else 0 )


#print(data)

# Ordinal
# Atributos categóricos ordinais.

data[['parental_education', 'preparation_course']].head()
#print(data[['parental_education', 'preparation_course']].head())

data['parental_education'].drop_duplicates()
#print(data['parental_education'].drop_duplicates())

parental_education_mapper = {
    "master's degree": 6,
    "bachelor's degree": 5,
    "associate's degree": 4,
    "some college": 3,
    "high school": 2,
    "some high school": 1,
}

data['parental_education_encoded'] = data['parental_education'].apply(lambda level: parental_education_mapper[level])
#print(data['parental_education_encoded'])


#print(data.head())


# Escala
#A normalização reduz a escala

min  = data['math'].min()
print(min)
max = data['math'].max()
print(max)


data['math_norm'] = data['math'].apply(lambda grade: (grade - min) / (max - min))
#print(data.head())


# Padronização
# A padronização altera a média

media = data['math'].mean()
print(media)

desvio_padrao = data['math'].std()
print(desvio_padrao)


data['math_padr'] = data['math'].apply(lambda nota: (nota - media) / desvio_padrao)
