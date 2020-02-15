 #* Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
 #! A: Quantas vezes apareceu o valor 9.
 #! B: Em que posição foi digitado o valor 3.
 #! C: Quais foram os números pares.


num1 = int(input('Digite um número entre 1 e 9: '))
num2 = int(input('Digite outro número entre 1 e 9: '))
num3 = int(input('Digite outro número entre 1 e 9: '))
num4 = int(input('Digite mais um número entre 1 e 9: '))

numeros = (num1, num2, num3, num4)
print(f'Os números digitados foram: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
print(f'O número 3 aparecêu na {numeros.index(3)+1}ª posição.')

for n in numeros:
    if n % 2 == 0:
        print(n)