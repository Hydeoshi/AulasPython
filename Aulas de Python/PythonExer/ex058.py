from random import randint
from time import sleep

print('='*61)
print('='*20, 'Jogo da Adivinhação', '='*20)
print('='*61)

tentativa = 0

sleep(1)
print('Seja bem-vindo ao jogo de adivinhação.\nNesse jogo eu vou pensar em um número entre 1 e 10 e você precisa adivinhar qual número eu pensei.\n', end='')
print('Você vai tentar adivinhar até acertar e ao fim eu vou dizer quantas tentativas você precisou para acertar o número.')

começar = str(input('Vamos jogar? [Y/N]')).strip().upper()[0]
while começar not in 'YyNn':
    começar = str(input('Opção invalida. Vamos tentar de novo. Gostaria de jogar o jogo da adivinhação? [Y/N]')).upper().strip()[0]

if começar == 'Y':
    print('Então vamos começar!')
    sleep(1)
    print('Estou pensando em um número...')
    num = randint(1, 10)
    sleep(1)
    escolha = int(input('Pronto, pensei em um número! Qual número eu pensei? '))
    while escolha != num:
        sleep(1)
        tentativa += 1
        escolha = int(input('Não é esse o número que pensei! Tente de novo.\nQual número eu pensei: '))
        sleep(1)
    if escolha == num and tentativa <= 2:
        print(f'Parabéns! Você acertou bem rápido. O número que eu pensei é o {num}.')
        print(f'Você acertou em {tentativa} tentativas.')
    elif escolha == num and tentativa <= 5:
        print(f'Você acertou. Demorou um pouquinho para acertar. O número que eu tinha pensado era o {num}.')
        print(f'Você acertou em {tentativa} tentativas.')
    else:
        print(f'Zzzzz. Você demorou demais para acertar, pensei que nunca fosse descobrir que o número que eu tinha pensado era o {num}!')
        print(f'Você acertou em {tentativa} tentativas. Vamos ver se na próxima você acerta mais rápido!')
else:
    print('Que pena. Jogamos em uma próxima!')


