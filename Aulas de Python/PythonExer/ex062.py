print('Progressão Aritimética')
cons = int(input('Digite a constante: '))
razao = int(input('Digite a razão da PA: '))
termo = cons
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} - ', end='')
        termo = termo + razao
        cont = cont + 1
    print('...')
    mais = int(input('Quantos termos a mais você gostaria de ver? '))
print(f'Progressão finalizada com {total} termos.')
