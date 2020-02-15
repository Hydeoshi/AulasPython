from datetime import date
ano = int(input('Que ano gostaria de analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year #Essa library vai puxar o ano atual.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #Anos bissextos normalmente são de quatro em quatro anos, menos anos multiplos de 100 que não são multiplos de 400.
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO.'.format(ano))
