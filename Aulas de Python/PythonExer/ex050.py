cont = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite o {}° número: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você digitou {} números pares e a soma é {}.'.format(cont, soma))