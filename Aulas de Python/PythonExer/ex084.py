 #* Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
 #* A: Quantas pessoas foram cadastradas.
 #* B: Uma listagem com as pessoas mais pesadas.
 #* C: Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
maior_peso = []
menor_peso = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Gostaria de adicionar mais pessoas? [S/N]')).lower().strip()[0]
    if continuar not in 'sn':
        continuar = str(input('Resposta inválida. Por favor responda SIM ou NÃO. Gostaria de adicionar mais pessoas? ')).lower().strip()[0]
    if continuar == 'n':
        break
print(f'Os dados registrados são: {pessoas}')
print(f'Foram cadastradas {len(pessoas)} pessoas.')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}]', end=' ')
print(f'tem o maior peso, pesando {maior_peso}kg.')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end=' ')
print(f'tem o menor peso, pesando {menor_peso}kg.')
