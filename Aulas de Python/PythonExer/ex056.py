somaidade = 0
maioridadehomem = 0
médiaidade = 0
nomevelho = ''
contmulher = 0
for p in range(1, 5):
    print(f'======== {p}ª Pessoa ========')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade #ou então somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        contmulher = contmulher + 1 #Pode ser simplificado com += 1.
médiaidade = somaidade / 4
print(f'A média de idade do grupo de pessoas é {médiaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'{contmulher} mulheres tem a idade menor do que 20 anos.')