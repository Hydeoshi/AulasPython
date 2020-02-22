 #* Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
 #* O programa vai perguntar quantos jogos serão gerados e vai sortear seis números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

numeros_mega = list()
valores = [[6, 4.50], [7, 31.50], [8, 126.00], [9, 378.00], [10, 945.00], [11, 2.079], [12, 4.158], [13, 7.772], [14, 13.513], [15, 22.522]]
jogos = list()
total = 1
apostas = int(input('Quantos jogos você gostaria de fazer? '))
numeros = int(input('Quantos números gostaria de apostar em cada jogo? [Max 15] '))
while numeros > 15 or numeros < 6:
    numeros = int(input('Quantidade máxima de 15 números por aposta. Escolha quantos números gostaria de apostar: '))
else:
    while total <= apostas:
        contador = 0
        while True:
            numeros_sorteados = randint(1, 60)
            if numeros_sorteados not in numeros_mega:
                numeros_mega.append(numeros_sorteados)
                contador = contador + 1
            if contador >= numeros:
                break
        numeros_mega.sort()
        jogos.append(numeros_mega[:])
        numeros_mega.clear()
        total = total + 1
print('=' * 10, f' SORTEANDO {apostas} JOGOS ', '=' * 10)
print()
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice + 1} - {lista}')
    sleep(1)
print()
if numeros in valores:
    print(f'O valor dos seus jogos é de R${valores}')
print('=' * 10, f' BOA SORTE! ', '=' * 10)