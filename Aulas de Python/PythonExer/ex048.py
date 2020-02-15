soma = 0
cont = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        cont = cont + 1
        soma = soma + num
        #No Python é possível usar += ao invés de repetir o valor. Exemplo: soma += 1, ao invés de soma = soma + 1.
print('A soma de {} resultados é igual a {}.'.format(cont, soma))
