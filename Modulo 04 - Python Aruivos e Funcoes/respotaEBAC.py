#respotra da EBAC 



cds = int(input("Digite a quantidade de CDs: "))
preco = 0

for i in range(cds):

    preco += float(input(f"Digite o preço do CD {i+1}: "))

print(f"Preço total: R${preco:.2f}\nMédia de custo por CD: R${preco/cds:.2f}")