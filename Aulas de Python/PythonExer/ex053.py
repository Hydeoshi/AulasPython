frase = str(input('Digite uma palavra: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
#É possível fazer essa parte abaixo e forma diferente, sem esse inverso de baixo. É com uma técnica de fatiamento, onde inverso = junto[::-1], isso tornaria o código menor.
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('Você digitou a frase {} que ao contrário fica {}.'.format(junto, inverso))
if inverso == junto:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo.')