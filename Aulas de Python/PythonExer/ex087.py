 #* Aprimore o exercício anterior, mostrando no final:
 #* A: A soma de todos os valores pares digitados.
 #* B: A soma dos valores da terceira coluna.
 #* C: O maior valor da segunda linha. 

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
numeros_pares = 0
numeros_coluna3 = []
maior_valor = []
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a matriz na posição [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            numeros_pares = numeros_pares + matriz[l][c]
    print()
print()
print(f'A soma dos números pares digitados na matriz é: {numeros_pares}')
numeros_coluna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é: {numeros_coluna3}.')
maior_valor = matriz[1][0]
if matriz[1][1] > maior_valor:
    maior_valor = matriz[1][1]
elif matriz[1][2] > maior_valor:
    maior_valor = matriz[1][2]
print(f'O maior valor da segunda linha é: {maior_valor}')


