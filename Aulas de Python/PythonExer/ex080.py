 #* Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já 
 #* na posição correta de inserção. (Sem usar o sort())
 #* No final, mostre a lista ordenada na tela.

numeros = list()
for count in range(0, 5):
    num_add = int(input('Digite um número: '))
    if count == 0 or num_add > numeros[len(numeros)-1]:      #* Também é possível colocar numeros[-1]. Dessa forma ele vai checar se
        numeros.append(num_add)                              #* O número é maior que o último valor adicionado na lista.
        print(f'Adicionado ao final da lista.')
    else:
        pos = 0                                              #* Aqui é para checar as posições do vetor. Começando em 0.
        while pos < len(numeros):                            #* Então será checado em cada posição se o valor a ser inserido é menor do que o valor naquela posição.
            if num_add <= numeros[pos]:
                numeros.insert(pos, num_add)                 #* Se for menor, o número vai ser adicionado naquela posição.
                print(f'Adicionando na {pos}ª posição da lista.')
                break
            pos = pos + 1
print(f'Os valores digitados são: {numeros}')
    