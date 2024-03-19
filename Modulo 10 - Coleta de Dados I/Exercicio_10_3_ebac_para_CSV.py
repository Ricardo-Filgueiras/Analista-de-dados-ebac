# 3. Extraindo numero de contato de arquivo texto 
import csv

#abrindo o arquivo txt
with open(file='./ebac.txt', mode='r', encoding='utf8') as aq:
    linha = aq.readlines()

#filtra as informações desejadas 

linha = filter(lambda linha: linha != '\n',linha)
linha = map(lambda linha: linha.strip(),linha)
linha = list(linha)

#print(linha)

#Vamos pegar so itens "whatsapp e numero"

dados_linhas = filter(lambda linha: '+' in linha, linha)
dados_linhas = list(dados_linhas)

#print(dados_linhas)

#Vamos separar os numeros do tipos de contato
numero = []
tipo = []

for linha_conteudo in dados_linhas:
    palavras = linha_conteudo.split(sep='+')
    tipo.append(palavras[0])
    numero.append(palavras[1].lower())
    
#print(tipo)
#print(numero)

# criando uma lista com os dados formatados 

dados_formatados = []
dados_formatados.append(['tipo','numero'])
for i in range(len(numero)):
    dados_formatados.append([tipo[i],numero[i]])

#print(dados_formatados)

#Criando um arquivo CSV como no modelo 

with open('result03.csv','w',newline='') as file:
    escrever = csv.writer(file,delimiter=';')
    escrever.writerows(dados_formatados)


for dados in dados_formatados:
    print(dados[0] + ';' + dados[1])