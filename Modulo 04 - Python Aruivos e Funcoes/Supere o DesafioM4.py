#print(int(13.235))
#Desafio: 

#Faça um programa que calcule o valor total investido
#por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
#O usuário deverá informar a quantidade de CDs e o valor para cada um.


invetario = []
quantidadeCDs = []


invetario.append(int(input('Digite seu Numero de CDs: ')))
invetario.append(int(input('Digite quanto ele custou?: ')))

total = sum(invetario)
ncds = invetario[0] 
pcds = invetario[1]
media = pcds/ncds
#media = total/len(invetario)
print(f'Toda a sua coleção vale R${total}, o Custo medio deles e R${media} !!!. e esses são os elementos dessa lista {invetario} ')