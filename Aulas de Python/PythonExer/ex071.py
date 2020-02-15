 #* Crie um programa que simule o funcionamento de um caixa eletrônico.
 #* No início pergunte ao usuário qual será o valor sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
 #! OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('========== Banco do Toquinha ==========')
print('''
[1] Saque
[2] Depósito
[3] Sair''')


escolha = int(input('Escolha a sua opção: '))
if escolha == 1:
    print('O nosso caixa trabalha com notas de R$50, R$20, R$10 e R$1.')
    saque = float(input('Digite o valor a ser sacado: R$'))
    total = saque
    ced = 50
    totced = 0
    while True:
        if total >= ced:
            total = total - ced
            totced = totced + 1
        else:
            if totced > 0:
                print(f'Total de {totced} cédulas de R${ced}.')
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            totced = 0
            if total == 0:
                break
elif escolha == 2:
    totalcaixa = 0
    dep = float(input('Digite o valor do depósito: R$'))
    totalcaixa = dep
    print(f'O total na sua conta é de R${totalcaixa}.')
    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('Gostaria de adicionar mais algum valor na sua conta? [S/N]')).lower().strip()
    if resposta == 'n':
        print('Encerrando.')
elif escolha == 3:
    print('Encerrando.')
else:
    print('Escolha inválida, por favor escolha uma das três opções.')
print('Volte sempre.')