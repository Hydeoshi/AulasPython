 #* Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 #* Caso o número já exista dentro da lista, ele não será adicionado. 
 #* No final, serão exibidos todos os valores numéricos digitados, em ordem crescente.

numeros = []
while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        print('Valor adicionado com sucesso. ')
        numeros.append(num)
    else:
        print('Valor inválido. Não é possível adicionar números duplicados.')
    sair = str(input('Gostaria de digitar outro número? [S/N] ')).lower().strip()[0]
    if sair not in 'sn':
        sair = str(input('Resposta inválida. Gostaria de digitar outro número? [S/N]')).lower().upper()[0]
    elif sair == 'n':
        break
numeros.sort()
print(f'Os valores digitados em ordem crescente são: {numeros}')