# Exemplo de "try" e "except" 



Anos_Listas = [2019,2020,2021,2022]
Anos_Set ={2019,2020,2021,2022}
# ano_atual = 2023

try:
    ano_atual = Anos_Listas[5]
    print(ano_atual)
except IndexError:
    print("lista de anos menor que valor escolhido, esperase um valor entre 0 " + str(len(Anos_Listas) -1))
except Exception as exc:
    print(exc)
finally:
    ...