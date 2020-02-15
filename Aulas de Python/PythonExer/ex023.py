num = int(input('Digite um número de até quatro digitos:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A únidade do seu número é {}, sua dezena é {}, sua centena é {} e seu milhar é {}.'.format(u, d, c, m))
#Essa forma não funciona com menos do que quatro digitos.
#n = str(num)
#print('A únidade do seu número é {}, sua dezena é {}, sua centena é {} e seu milhar é {}.'.format(n[3], n[2], n[1], n[0]))
