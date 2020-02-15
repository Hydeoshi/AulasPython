from random import randint
from time import sleep
print('{:=^40}'.format(' JOKENPÔ! '))
print(''' Vamos jogar um jogo de Jokenpô.\n Você vai escolher uma das opções a seguir e vamos ver quem ganha: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura.''')
item = ('Pedra','Papel','Tesoura')
escolha = int(input('Qual a sua escolha? '))
print('JO!')
sleep(1)
print('Ken!')
sleep(1)
print('PÔ!')
print('='*64)
computador = randint(0, 2)
if computador == 0 and escolha == 0 or computador == 1 and escolha == 1 or computador == 2 and escolha == 2:
    print('Nós empatamos! Nós dois escolhemos \033[31m{}\033[m.'.format(item[computador]))
elif computador == 0 and escolha == 2 or computador == 2 and escolha == 1 or computador == 1 and escolha == 0:
    print('Parece que eu ganhei! Eu escolhi \033[32m{}\033[m e você escolheu \033[31m{}\033[m.'.format(item[computador], item[escolha]))
elif escolha == 0 and computador == 2 or escolha == 2 and computador == 1 or escolha == 1 and computador == 0:
    print('Parabéns, você ganhou! Você escolheu \033[32m{}\033[m e eu escolhi \033[31m{}\033[m.'.format(item[escolha], item[computador]))
else:
    print('Jogada inválida!')
print('='*64)
