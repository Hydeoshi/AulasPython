print('{:=^40}'.format(' LOJAS DOTTA '))
produto = float(input('Digite o preço do produto: R$'))
print('''Como você deseja pagar o produto no valor de R${:.2f}
[ 1 ] Dinheiro ou cheque com 10% de desconto
[ 2 ] À vista no cartão com 5% de desconto
[ 3 ] Em até 2 vezes no cartão sem juros
[ 4 ] Em 3 ou mais vezes com juros'''.format(produto))
opc = int(input('Escolha uma opção: '))
if opc == 1:
    pct = produto * 10 / 100
    des = produto - pct
    print('O seu produto no valor de R${:.2f} saíra por R${:.2f} com um desconto de 10% no pagamento em cheque ou dinheiro.'.format(produto, des))
elif opc == 2:
    pct = produto * 5 / 100
    des = produto - pct
    print('Pagando à vista no cartão o seu produto terá um desconto de 5%, passando de R${:.2f} para R${:.2f}.'.format(produto, des))
elif opc == 3:
    parcela = produto / 2
    print('O seu produto no valor de R${:.2f} terá duas parcelas de R${:.2f}.'.format(produto, parcela))
elif opc == 4:
    meses = int(input('Em quantas vezes você gostaria de parcelar o produto? '))
    pct = produto * 20 / 100
    parcela = (pct + produto) / meses
    print('O produto no valor de R${:.2f} será parcelado em {}x, com parcelas no valor de R${:.2f}.'.format(produto, meses, parcela))
else:
    print('Opção Inválida, escolha de novo.')
    