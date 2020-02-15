cidade = str(input('Digite o nome da sua cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')
#O :5 serve para procurar entre as cinco primeiras letras. 0:5 procuraria do zero ao cinco, mas nesse caso :5 procura tudo para trás da quinta letra.
#O .upper() foi usado para evitar erros onde o usuário digitaria o nome em minúsculo e voltaria um false.
