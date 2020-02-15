dp = float(input('Quanto dinheiro você tem em conta?: R$'))
cv = dp/3.27
print('Você tem {:.2f}R$ na sua conta. O valor atual do dólar está em US$3.27 para cada R$1. Com o dinheiro atual na sua conta você pode comprar US${:.2f}.'.format(dp,cv))
