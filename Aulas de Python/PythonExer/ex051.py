cons = int(input('Digite a constante: '))
r = int(input('Digite a razão: '))
décimo = cons + (11 -1) * r
for termo in range(cons, décimo, r):
    print('{}'.format(termo), end=' - ')
print('Fim')