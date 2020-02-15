from math import acos, atan, asin, radians
ângulo = int(input('Insira o ângulo:'))
radiante = radians(ângulo)
cosseno = acos(radiante)
seno = asin(radiante)  
tangente = atan(radiante)
print('O resultado para o ângulo de {:.1f}° é:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(ângulo, seno, cosseno, tangente))
