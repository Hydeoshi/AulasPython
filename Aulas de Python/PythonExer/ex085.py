 #* Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma única lista
 #* que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

dados = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        dados[0].append(valor)
    else:
        dados[1].append(valor)
print(f'Os números pares são: {dados[0]}.')
print(f'Os números ímpares são: {dados[1]}.')
