print('Progressão Aritimética.')
cons = int(input('Digite a constante: '))
r = int(input('Digite a razão da PA: '))
termo = cons
cont = 1
while cont <= 10:
    print(f'{termo} - ', end='')
    termo = termo + r
    cont = cont + 1
print('Fim.')