nome = str(input('Insira o seu nome: ')).strip()
print('O seu nome todo em maisculo é:{}'.format(nome.upper()))
print('O seu nome todo em minúsculo é: {}'.format(nome.lower()))
print('O seu nome possui {} caracteres.'.format(len(nome)-nome.count(' ')))
div = nome.split()
#print('Seu primeiro nome é: {}. Ele possui {} caracteres.'.format(div[0], nome.find(' ')))
print('Seu primeiro nome é {}. Ele possui {} caracteres.'.format(div[0], len(div[0])))

