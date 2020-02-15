#from math import factorial
num = int(input('Digite um número para calcular o fatorial: '))
#fac = factorial(num)
#print(f'O fatorial de {num} é {fac}.')
c = num
f = 1
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print(f'{f}')