from datetime import date
sexo = str(input('Qual o seu sexo? ')).upper()
nasc = int(input('Qual o seu ano de nascimento?' ))
atual = date.today().year
idade = atual - nasc
if sexo == 'MASCULINO':
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você precisa se alistar \033[32mimediatamente\033[m.')
    elif idade < 18:
        saldo = 18 - idade
        print('Você ainda não tem 18 anos, ainda faltam \033[31m{}\033[m anos para que você precise se alistar.'.format(saldo))
    elif idade > 18:
        saldo = idade - 18
        print('Tem \033[32m{}\033[m anos que você passou da idade para se alistar, se aliste imediatamente.'.format(saldo))
else:
    print('Você não precisa se alistar.')
    