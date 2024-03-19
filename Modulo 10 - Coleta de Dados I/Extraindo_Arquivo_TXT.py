# agora trabanlhando  com arquivos tipos txt

with open(file='./Nubank.txt', mode='r', encoding='utf-8') as aq:
    linhas = aq.readlines()


#print(linhas)

# Agora Limpando as linha de Caracteres.

linhas = filter(lambda linha:linha != '\n',linhas)
linhas = map(lambda linha: linha.strip(), linhas)
linhas = list(linhas)

#print(linhas)


# Agora Limpando as linha de Caracteres '.COM'

Linhas_com_emails = filter(lambda linha: '.com' in linha ,linhas)
Linhas_com_emails = list(Linhas_com_emails)

print(Linhas_com_emails)


# Agora Limpando as linha de Caracteres '@'

Emails_extraidos = []

for Linhas_com_emails in Linhas_com_emails:
    palavras = Linhas_com_emails.split(sep= ' ')
    emails = filter(lambda palavra: '@' in palavra, palavras)
    Emails_extraidos = Emails_extraidos + list(emails)

print(Emails_extraidos)

#de todas maneiras o tal do 'press@nubank' foiu esquecido !