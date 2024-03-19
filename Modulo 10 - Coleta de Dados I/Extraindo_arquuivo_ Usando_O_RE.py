# O extraindo o emails com o 'RE' regex uma feramenta que torna o python 
# muito util para o ETL.

import csv
import re # regex biblioteca para estruturar aqruivos de texto nao estruturados 


with open(file='./Nubank.txt', mode='r', encoding='utf8') as aq:
    texto = aq.read()
emails_extraidos = re.findall('\S+@\S+',texto)  # @\S+ só quero texto depois do @ \S+ e depois do @

print(emails_extraidos)

# agora escrevendo um arquivo CSV
with open(file='./nubank_emails_extraidos.csv', mode='w', encoding='utf8') as aq:
    escritor_csv = csv.writer(aq, delimiter=',')
    escritor_csv.writerows([['email']] + list(map(lambda email_extraido: [email_extraido],emails_extraidos)))
