 #* Crie um programa que vai ler vários números e colocar em uma lista. 
 #* Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
 #* Ao final, mostre o conteúdo das três listas geradas.

numeros = list()
numeros_pares = list()
numeros_impares = list()

while True:
    num_add = int(input('Digite um número: '))
    numeros.append(num_add)
    if num_add % 2 == 0:
        numeros_pares.append(num_add)
    else:
        numeros_impares.append(num_add)
    continuar = str(input('Gostaria de continuar? [S/N]')).lower().strip()[0]
    if continuar not in 'sn':
        continuar = str(input('Resposta inválida. Responda SIM ou NÃO. Gostaria de continuar? [S/N]')).lower().strip()[0]
    if continuar == 'n':
        break

#? Outra forma de fazer essa parte àcima já encaixando a lista de números pares e ímpares.
#* for i, v in enumerate(numeros):
#*     if v % 2 == 0:
#*        numeros_pares.append(v)
#*     elif v % 2 == 1:
#*        numeros_impares.append(v)

print(f'Os números digitados foram: {numeros}')
if numeros_pares == []:
    print(f'Não foram digitados números pares.')
else:
    print(f'Os números pares são: {numeros_pares}')
if numeros_impares == []:
    print('Não foram digitados números ímpares.')
else:
    print(f'Os números ímpares são: {numeros_impares}')