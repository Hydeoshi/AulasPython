nome = str(input('Qual é o seu nome? ')).strip()
if nome.upper() == 'KLAUSS':
    print('Que nome diferente que você tem.')
elif nome.upper() == 'PEDRO' and nome.upper() == 'MARIA' or nome.upper() == 'PAULO':
    print('O seu nome é muito comum no Brasil.')
elif nome.upper() in 'ANA CLÁUDIA JÉSSICA JULIANA': #Aqui a minha condição busca um desses nomes em 'in' para enviar uma mensagem especial.
    print('Esse nome feminino é bonito.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}.'.format(nome))