 #* Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
 #! Qual o é o total gasto na compra.
 #! Quantos produtos custam mais de R$ 1000.
 #! Qual é o nome do produto mais barato.

total_produtos = 0
quantos_produtos_acima_1000 = 0
produto_mais_barato = 0
nome_produto_barato = ' '
contador = 0
print(f'='*20, 'Mercado Teste', f'='*20 )
while True:
    nome = str(input('Produto: ')).strip()
    price = float(input('Valor do produto: R$'))
    total_produtos += price
    contador = contador + 1
    if price >= 1000:
        quantos_produtos_acima_1000 += 1
    if contador == 1 or price < produto_mais_barato:
        produto_mais_barato = price
        nome_produto_barato = nome
    continuar = str(input('Adicionar novo produto [S/N]: ')).lower().strip()[0]
    if continuar not in 'sn':
        continuar = str(input('Adicionar novo produto [S/N]: ')).lower().strip()[0]
    if continuar == 'n':
        break
print(f'O total gasto na compra é de R${total_produtos:.2f}.\n{quantos_produtos_acima_1000} produtos custam mais de mil reais.\nO produto mais barato é {nome_produto_barato} no valor de R${produto_mais_barato:.2f}.')