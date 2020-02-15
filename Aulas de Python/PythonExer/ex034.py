sal = float(input('Qual é o salário do funcionário? R$'))
if sal > 1250.00:
    aum = sal + (sal * 10 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} com o aumento de 10%.'.format(sal, aum))
else:
    aum = sal + (sal * 15 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} com o aumento de 15%.'.format(sal, aum))