 #* Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
 #* No final, mostre qual foi o maior e o menor valor digitado e as suas posições na lista.

num = []
num_maior = []
num_menor = []
for n in range(5):
    num.append(int(input(f'Digite um número para a posição {n}: ')))
print(f'Os valores digitados foram {num}\nO maior número digitado é o {max(num)} nas posições ', end='')
for i, v in enumerate(num):
    if v == max(num):
        print(f'{i}... ', end='')
print()
print(f'O menor número digitado é o {min(num)} nas posições ', end='')
for i, v in enumerate(num):
    if v == min(num):
        print(f'{i}... ', end='')
