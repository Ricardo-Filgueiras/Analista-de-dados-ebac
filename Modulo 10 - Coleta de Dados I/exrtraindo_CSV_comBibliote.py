# agora Fazendo o mesmo proceso usandoa biblioteca CSV
import csv

from functools import reduce


saldos = None
with open(file='./Banco.csv', mode='r', encoding='utf-8') as aq:
    leitor_csv_iter = csv.reader(aq,delimiter=',')
    cabecalho = next(leitor_csv_iter)
    indice_saldo = cabecalho.index('balance')
    saldos = [linha[indice_saldo] for linha in leitor_csv_iter]

print(saldos)


# Para calcular a media do saldo 
soma_saldos = reduce(lambda saldo_a, saldo_b: saldo_a + saldo_b,map(lambda saldo:int(saldo),saldos))
qtd_saldos_indice =len(saldos)
media_saldos = soma_saldos/qtd_saldos_indice


print(f'A média dos saldos é de {media_saldos}')