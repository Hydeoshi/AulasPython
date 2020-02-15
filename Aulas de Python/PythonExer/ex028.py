import random
jogars = str(input('Vamos jogar um jogo? Diga sim para começar: ')).strip().upper()
if jogars == 'SIM':
    print('Então vamos começar!\nEu vou pensar em um número de 0 até 5 e você precisa adivinhar o número que eu pensei!')
    num = int(input('Escolha o seu número: '))
    ran = random.randint(0,5)
    if num == ran:
        print('Parabéns! Você ganhou! O número que eu pensei era: {}.'.format(ran))
    else:
        print('Que pena, você perdeu! O número que eu pensei era: {}.'.format(ran))  
else:
    print('Então até uma próxima!')
