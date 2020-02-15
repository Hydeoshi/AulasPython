slr = float(input('Insira o seu salário:'))
pct = 15*slr/100
aum = slr+pct
print('O seu salário é de {:.2f}R$. Você irá receber um aumento de 15% equivalente à {:.2f}R$. Seu salário atual passará a ser de: {:.2f}R$.'.format(slr,pct,aum))
