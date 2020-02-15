num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número: '))
    cont = cont + 1
    soma = soma + num
soma = soma - 999
print(f'A soma é: {soma}')