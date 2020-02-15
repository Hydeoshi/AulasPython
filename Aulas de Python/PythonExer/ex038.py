num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('O número \033[32m{}\033[m é maior que o número \033[31m{}\033[m.'.format(num1, num2))
elif num2 > num1:
    print('O número \033[32m{}\033[m é maior que o número \033[31m{}\033[m.'.format(num2, num1))
else:
    print('O número \033[32m{}\033[m e o número \033[31m{}\033[m são iguais, não existe valor maior.'.format(num1, num2))