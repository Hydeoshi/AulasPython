valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo número: '))

selec = 0
while selec != 5:
    print('''Escolha uma das opções a seguir: 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair''')
    selec = int(input('Por favor, digite o número da opção escolhida: '))

    if selec == 1:
        soma = valor1 + valor2
        print(f'O número {valor1} somado ao número {valor2} é igual à: {soma}.')
    elif selec == 2:
        multi = valor1 * valor2
        print(f'O número {valor1} multiplicado pelo número {valor2} é igual à: {multi}.')
    elif selec == 3:
        if valor1 > valor2:
            print(f'O número {valor1} é maior que o número {valor2}.')
        else:
            print(f'O número {valor2} é maior que o número {valor1}.')
    elif selec == 4:
        print('Então por favor, escolha novos números.')
        valor1 = int(input('Digite o primeiro número: '))
        valor2 = int(input('Digite o segundo número: '))
    elif selec == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, por favor escolha uma opção.')
print('Até uma próxima!')
