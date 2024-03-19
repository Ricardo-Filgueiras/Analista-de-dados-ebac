# Nesse parte vamos extrair e transforma um arquivo xlsx ou EXCEL
# e precisso importa o modulo 'pip install openpyxl' na maquina


from openpyxl import load_workbook # modulo importadoo

planilhas = load_workbook(filename='banco.xlsx') #Abrindo o Arquivo xlsx no python 
planilha1 = planilhas.active  # essa linha pega a primeira planinha de um arquivo excel  ou xlsx 



# depois de abrido o processo segui normal no python 

saldos = []

cabecalho = next(planilha1.values)
indice_saldo = cabecalho.index('balance')
saldos = [linha[indice_saldo] for linha in planilha1.values if linha[indice_saldo] != 'balance']

print(saldos)


#df.loc[df['default']==1][df['estado_civil']=='solteiro']