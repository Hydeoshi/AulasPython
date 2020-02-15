 #* Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 #! Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while num < 0 or num > 20:
    num = int(input('Número inválido. Digite um número entre 0 e 20: '))
else:
    print(f'Você digitou o número {extenso[num]}!')