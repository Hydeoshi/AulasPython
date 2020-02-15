#nome = str(input('Qual é o seu nome? ')).strip()
#if nome == nome.upper() == 'KLAUSS':
#if nome == 'Klauss':
    #print('Que nome bonito você tem!')
#else:
    #print('Que nome normal você tem.')
#print('Boa tarde, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}.'.format(m))
#Abaixo o uso de uma condição:
#if m >= 6.0:
    #print('Parabéns! A sua nota de {:.1f} ficou acima da média.'.format(m))
#else:
    #print('Sua nota de {:.1f} ficou abaixo da média. Estude um pouco mais na próxima!'.format(m))
print('Parabéns!' if m >=6 else 'Estude um pouco mais.')
#Está é uma condição simplificada.