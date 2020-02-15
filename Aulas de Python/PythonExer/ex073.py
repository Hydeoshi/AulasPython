 #* Crie uma tupla com os vinte primeiros colocados do campeonato brasileiro de futebol na ordem de colocação. Depois mostre:
 #! A: Apenas os cinco primeiros.
 #! B: Os últimos quatro colocados da tabela.
 #! C: Uma lista com os times em ordem alfabética. 
 #! D: Em que posição da tabela está o time da Chapecoense.

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 
'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('='*65)
print(f'='*20, ' Tabela do Brasileirão ', '='*20)
print('='*65, '\n')

print(f'\033[33mOs times do Campeonato Brasileiro são:\033[m {times}\n')
print('='*65, '\n')
print(f'\033[32mOs cinco primeiros colocados são:\033[m {times[:5]}\n')
print('='*65, '\n')
print(f'\033[31mOs últimos quatro colocados da tabela são:\033[m {times[16:]}\n')
print('='*65, '\n')
print(f'\033[33mOs times em ordem alfabética são:\033[m {sorted(times)}\n')
print('='*65, '\n')
print(f'\033[33mO time da Chapecoense está em {times.index("Chapecoense")+1}º lugar.\033[m')
