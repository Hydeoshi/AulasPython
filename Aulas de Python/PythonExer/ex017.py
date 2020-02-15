from math import hypot
co = float(input('Insira o comprimento do cateto oposto:'))
ca = float(input('Insira o comprimento do cateto adjacente:'))
hi = hypot(co, ca)
print('O comprimento da hipotenusa é de: {:.2f}'.format(hi))
