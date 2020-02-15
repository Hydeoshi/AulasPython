from random import randint
print('='*20, ' JOGO DO PAR OU ÍMPAR ', '='*20)
cont = 0
while True:
    escolha = str(input('Você quer escolher par ou ímpar? [P/I]')).lower().strip()
    if escolha not in 'PpIi':
        print('Escolha inválida. Por favor escolha par ou ímpar.')
    else:
        num = int(input('Escolha um valor de 1 até 10: '))
        if num > 10 or num < 0:
            print('Valor inválido, escolha outro número!')
        else:
            comp_e = randint(0, 10)
            soma = comp_e + num
            if soma % 2 == 0 and escolha == 'p':
                cont += 1
                print(f'Você escolheu {num} e o computador escolheu {comp_e}, a soma é de {soma}. O resultado é PAR.')
                print(f'Você ganhou!')
            elif soma % 2 == 1 and escolha == 'i':
                print(f'Você escolheu {num} e o computador escolheu {comp_e}, a soma é de {soma}. O resultado é ÍMPAR.')
                print('Você ganhou!')
            elif soma % 2 == 0 and escolha == 'i':
                print(f'Você escolheu {num} e o computador escolheu {comp_e}, a soma é de {soma}. O resultado é PAR.')
                print('Você perdeu!')
                break
            elif soma % 2 == 1 and escolha == 'p':
                print(f'Você escolheu {num} e o computador escolheu {comp_e}, a soma é de {soma}. O resultado é ÍMPAR.')
                print('Você perdeu!')
                break
print(f'Fim de jogo. Você ganhou {cont} vezes.')
    