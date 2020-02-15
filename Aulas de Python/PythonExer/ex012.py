prc = float(input('Insira o preço do seu produto para checarmos o desconto de 5%: R$'))
pct = 5*prc/100
res = prc-pct
print('O produto no valor de {:.2f}R$ recebeu um desconto de 5% que equivale à {:.2f}R$. O valor atual do produto é de {:.2f}R$.'.format(prc,pct,res))
