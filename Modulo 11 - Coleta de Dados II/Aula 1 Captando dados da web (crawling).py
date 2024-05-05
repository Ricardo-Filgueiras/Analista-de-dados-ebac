# Aula 1: Captando dados da web (crawling)

import requests # requerimento 
from requests.exceptions import HTTPError
resposta = requests.get('https://www.google.com.br/') # get e tag pegar tem como sentido acessare o link entre aspas 

print(resposta.status_code) # retorna o codigo de status da operação

conteudo =  None
URL =  'https://www.google.com.br/'


try :
    respostas = requests.get(URL)
    resposta.raise_for_status()
except HTTPError as exc:
    conteudo = respostas.text
    
print(conteudo)