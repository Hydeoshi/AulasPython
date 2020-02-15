from datetime import date
ano = int(input('Qual o ano de nascimento do atleta? '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('O atleta tem {} anos e está na categoria \033[36MIRIM\033[m.'.format(idade))
elif idade >= 10 and idade <= 14:
    print('O atleta tem {} anos e está na categoria \033[33mINFANTIL\033[m.'.format(idade))
elif idade >= 15 and idade <=19:
    print('O atleta tem {} anos e está na categoria \033[32mJUNIOR\033[m.'.format(idade))
elif idade == 20:
    print('O atleta tem {} anos e está na categoria \033[35mSÊNIOR\033[m.'.format(idade))
else:
    print('O atleta tem {} anos e está na categoria \033[31mMASTER\033[m.'.format(idade))