num = int(input('Digite um número inteiro: '))
print('''Escolha uma opção para conversão:
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opc = int(input('Digite sua opção: '))
if opc == 1:
    print('O número \033[31m{}\033[m convertido em binário é igual a \033[32m{}\033[m.'.format(num, bin(num)[2:]))
elif opc == 2:
    print('O número \033[31m{}\033[m convertido em octal é igual a \033[32m{}\033[m.'.format(num, oct(num)[2:]))
elif opc == 3:
    print('O número \033[31m{}\033[m convertido em hexadecimal é igual a \033[32m{}\033[m.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')