n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = n1 + n2 / 2
if m >= 7:
    print('Parabéns, a sua média foi de {:.1f} e você está \033[32mAPROVADO\033[m.'.format(m))
elif m <= 5:
    print('A sua nota foi de {:.1f} e você está \033[32mREPROVADO\033[m.'.format(m))
else:
    print('A sua nota foi de {:.1f} e você está de \033[33mRECUPERAÇÃO\033[m.'.format(m))