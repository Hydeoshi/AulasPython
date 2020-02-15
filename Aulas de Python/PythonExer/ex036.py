casa = float(input('Qual o valor do imóvel? R$'))
sal = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você planeja pagar o imóvel? '))
prest = casa / (anos * 12)
print('Para pagar uma casa no valor de R${:.2f} em {} anos a prestação mensal será de R${:.2f}.'.format(casa, anos, prest))
if prest >= 30 * sal / 100:
    print('O seu pedido de empréstimo foi \033[1;31mnegado\033[m.')
else:
    print('O seu emprestimo foi \033[1;32maprovado\033[m.')