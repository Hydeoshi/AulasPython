nome = str(input('Insira o seu nome completo: ')).strip()
#Sempre lembrar de usar um strip() quando se pede input, assim evitando problemas com espaços extras no input por parte do usuário.
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
#A string nome foi transformada em maiusculo para evitar problemas onde o usuário digitaria o nome todo em minúsculo. 
#Nesse caso também poderia se usar um lower() para o mesmo efeito, assim realizando a pesquisa pelo nome 'silva'.