# Primeiro e preciso ter um aquivo CSV para se trabalhar 
#
#Exemplpo; Extraindo os valores da primeira coluna(idade)

idades_lista = []

with open(file='./Banco.csv', mode='r', encoding='utf-8') as aq:
    cabecalho = aq.readline() # le o cabecalho 
    indice_idade = cabecalho.index('age')
    linha = aq.readline()# le a primeira linha 
    while linha: # loop para ler cada linha do arquivo
        idade_Variavel = linha.strip().split(sep=',')[indice_idade]# separar a coluna pelo indece 'AGe' idade
        idades_lista.append(idade_Variavel) # adicioonar o dado acima a lista 'idades'
        linha = aq.readline()# vollta para o inicio quando ler a primeira linha 
print(idades_lista)




#Exemplo de tipo de dados
tipos_idades = set(map(lambda idade: type(idade_Variavel),idades_lista))