 #* Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
 #* O programa vai perguntar quantos jogos serão gerados e vai sortear seis números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

#! Continuar a ideia dos valores dos jogos usando um dicionário.

numeros_mega = list()
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
print('=' * 10, f' BOA SORTE! ', '=' * 10)