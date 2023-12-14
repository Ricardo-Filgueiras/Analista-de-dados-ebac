# Função de tratamento de erros com try e xcept 
# Introdução do "raise" o que coloca a responsabilidade sobre outro
# O método raise é usado para forçar uma exceção a ser gerada em tempo de execução. 
# Isto pode ser usado para indicar erros específicos em um determinado momento, 
# mesmo que a exceção não tenha ocorrido de forma natural. Para utilizar o raise, 
# você precisa especificar o tipo de exceção que deseja lançar, seguido por uma mensagem explicativa.
# Por exemplo, raise ValueError("Valor inválido") irá lançar uma exceção ValueError com a mensagem "Valor inválido".
# As exceções podem ser capturadas usando os métodos try e except.

from functools import reduce

def processar_faturadas (nome_arquivo: str):
    faturas = []
    with open(file=nome_arquivo, mode="r", encoding='utf-8') as arquivo:
        linha = arquivo.readline()
        linha =arquivo.readline()

        while linha:
            try:
                fatura = float(linha.strip().split(sep=",")[3])
            except ValueError as exc:
                raise ValueError (f"Falha ao Processar  as faturas devido ao seguinte erro: '{exc}'")
            else:
                faturas.append(fatura)
            linha = arquivo.readline()
    total_a_pagar = reduce(lambda x,y: x+y , faturas)
    total_a_pagar = round(total_a_pagar,2)

    return total_a_pagar
