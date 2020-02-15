#cont = 1
#while cont <= 10:
    #print(cont, ' ', end='')
    #cont += 1
#print('Fim.')

num = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break                 #* Comando usado para quebrar um while infinito.
    soma += num
print(f'A soma dos valores é {soma}.')


nome = 'José'
idade = 33
sal = 985.3

print(f'O {nome} tem {idade} anos e recebe R${sal:.2f}.')
print(f'O {nome:20} tem {idade} anos e recebe R${sal:.2f}.')  #* Formatação: Nesse caso o nome irá aparecer com vinte espaços.
print(f'O {nome:^20} tem {idade} anos e recebe R${sal:.2f}.') #* O nome irá aparecer centralizado.
print(f'O {nome:-^20} tem {idade} anos e recebe R${sal:.2f}.') #* O nome irá aparecer centralizado e complementado com traços.
print(f'O {nome:->20} tem {idade} anos e recebe R${sal:.2f}.') #* O nome irá aparecer alinhado para a direita e complementado com traços.
print(f'O {nome:-<20} tem {idade} anos e recebe R${sal:.2f}.') #* Alinhado esquerda e complementado com traços.
