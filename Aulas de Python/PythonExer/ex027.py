nome = str(input('Por favor, digite o seu nome completo: '))
sep = nome.split()
#print('Olá {}. É um prazer te conhecer.'.format(sep[0]))
#print('O seu sobrenome é {}.'.format(sep[len(sep)-1]))
print('Olá {}. É um prazer te conhecer.\nO seu sobrenome é {}, correto?'.format(sep[0], sep[len(sep)-1]))