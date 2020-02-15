contmaior = conthomem = contmulher20 = 0
while True:
    print('-'*39)
    print('--------- Cadastre uma Pessoa ---------')
    print('-'*39)
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo [M/F]: ')).strip().lower() [0]
    if idade >= 18:
        contmaior += 1
    if sexo == 'm':
        conthomem += 1
    if sexo == 'f' and idade <= 20:
        contmulher20 += 1
    cont = ' '
    while cont not in 'yn':
        cont = str(input('Gostaria de adicionar outra pessoa? [Y/N]')).lower().strip() [0]
    if cont == 'n':
        break
print(f'Ao todo temos {contmaior} pessoas maiores de idade.')
print(f'Ao todo {conthomem} homens foram cadastrados.')
print(f'{contmulher20} mulheres menores de 20 anos.')