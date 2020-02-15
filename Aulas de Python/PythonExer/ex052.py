num = int(input('Digite um número inteiro: '))
tot = 0
for count in range(1, num + 1):
    if num % count == 0:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(count), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('O número {} \033[32mé\033[m um número primo.'.format(num))
else:
    print('O número {} \033[31mnão\033[m é um número primo.'.format(num))