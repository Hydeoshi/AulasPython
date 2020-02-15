escolha = 'y'
soma = media = quant = maior = menor = 0
while escolha in 'Yy':
    num = int(input('Digite um número: '))
    escolha = str(input('Gostaria de continuar? [Y/N]')).lower().strip()
    quant = quant + 1
    soma = soma + num
    if quant == 1:
         maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quant
print(f'Você digitou {quant} números.\nA soma de todos os valores é {soma} e a média é de {media:.2f}!\nO maior valor é {maior} e o menor é {menor}.')
print('Encerrando.')