 #* Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
 #* No final, mostre uma listagem dos preços, organizando os dados em forma tabular.

produtos = ('Café Melitta', 8.99, 'Sabão em Pó - OMO', 14.99, 'Requeijão', 4.87, 'Pão', 5, 
'Suco de Laranja', 11.80, 'Pizza Congelada', 10.90, 'Ração para Gatos', 27.87, 'Ração para Cachorros', 31, 
'Limões', 5.42)

print('-' * 42)
print(f'{"Lista de Compras":^42}')
print('-' * 42)
for pos in range(len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>10.2f}')