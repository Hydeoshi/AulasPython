 #* Crie um programa que leia vários números e coloque-os em uma lista. Depois disso mostre:
 #* A: Quantos números foram digitados.
 #* B: A lista dos valores, ordenada de forma decrescente. 
 #* C: Se o valor 5 foi digitado e está ou não na lista.

numeros = list()
while True:
    num_add = int(input('Digite um número: '))
    numeros.append(num_add)
    continuar = str(input('Gostaria de continuar adicionando números? [S/N]')).lower().strip()[0]
    if continuar not in 'sn':
        continuar = str(input('Resposta inválida. Gostaria de continuar adicionando números? [S/N]')).lower().strip()[0]
    elif continuar == 'n':
        break
print(f'Foram digitados {len(numeros)} números nessa lista.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {numeros}')
if 5 in numeros:
    print(f'O valor 5 está na lista.')
else:
    print(f'O valor 5 não está dentro da lista.')