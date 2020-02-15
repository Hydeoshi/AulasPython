sexo = str(input('Digite o seu sexo: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Informe o seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado.')

