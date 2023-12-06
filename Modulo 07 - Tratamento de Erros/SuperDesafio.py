#Desafio:

#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
#O usuário deve informar de qual número ele deseja ver a tabuada.

#Lembre-se de que você já conhece o nível intermediário da linguagem de programação Python, 
#além de conhecer como automatizar dados por meio da programação funcional 
#e programação orientada a objetos. 
print('Vamos Gerar uma Tabuada ...')
dnumero = int(input("Digite seu numero de 1 a 10: "))
vezes = 1
ate =  11

while True:

    for i in range(vezes, ate):
            n = i * vezes
            print(f'{dnumero} X {i} = {n}')

    continuar = input('Deseja gerar outra tabuada?  (s/n)').lower()

    if continuar != 's':
        break