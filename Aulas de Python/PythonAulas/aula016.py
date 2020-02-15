lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

#! Essa é a forma simples de usar o for com uma tubpla, caso não precise de posição:
for comida in lanche:
    if comida == 'Suco':
        print(f'Eu vou beber muito {comida}')
    else:
        print(f'Eu vou comer muito {comida}')

#! Essa é a forma de se usar for com range em uma tupla.
for count in range(0, len(lanche)):  
    if lanche[count] == 'Suco':
        print(f'Eu vou beber muito {lanche[count]}') #* Caso precise da posição do item na tupla junto com o item, adicionar {cont} no print. Ex: "Eu vou beber muito {lanche[count]} na posição {count}."
    else:
        print(f'Eu vou comer muito {lanche[count]}') #* Caso precise da posição do item na tupla junto com o item, adicionar {cont} no print. Ex: "Eu vou beber muito {lanche[count]} na posição {count}."


#! Essa é uma outra forma de se usar tuplas junto com for.
for comida in lanche: #* Aqui também é posível adicionar a posição do item. for pos, comida in enumerate(lanche):
    if comida == 'Suco': #* print(f'Eu vou beber {comida} na posição {pos}.)
        print(f'Eu vou beber {comida}!') 
    else:
        print(f'Eu vou comer {comida}!')
print('Comi para caramba!')

#! Aqui embaixo uma forma de ordenar uma tupla:
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #! a + b não é a mesma coisa que b + a. A ordem influência a nova tupla!
d = b + a
print(c) #! Exemplo de a + b
print(d) #! Exemplo de b + a

print(c.count(5)) #* Uma forma de contar quantas vezes aparece um determinado item dentro de uma tupla.
print(c.index(8)) #* Uma forma de mostrar onde aparece determinado item dentro da tupla.
print(c.index(5, 2)) #* Essa é uma forma de mostrar onde aparece determinado item dentro da tupla mudando a posição inicial da busca, nesse caso começando do segundo número.

pessoa = ('Klauss', 29, 'M', 130.00) #* Vários dados diferentes dentro de uma tupla.
#del(pessoa) É uma forma de deletar uma variável ou tupla.
print(pessoa)