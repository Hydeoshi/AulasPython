from datetime import date
count1 = 0
count2 = 0
hoje = date.today().year
for ano in range(1, 8):
    data = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(ano)))
    atual = hoje - data
    if atual <= 21:
        count1 = count1 + 1
    else:
        count2 = count2 + 1
print('Ao todo foram \033[31m{}\033[m pessoas \033[31mmaiores\033[m de idade.\nAo todo foram \033[32m{}\033[m pessoas \033[32mmenores\033[m de idade.'.format(count2, count1))