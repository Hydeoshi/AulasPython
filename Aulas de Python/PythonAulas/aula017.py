 #! Listas: []
 #? As listas podem ser modificadas, seja no fim, no meio, no começo, ou ter valores deletados e substituídos.

###### Teoria ######

lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Picolé']
print(lanche)
lanche.append('Cookie') #* O método append te deixa adicionar algo ao final de uma lista, no caso aqui estamos adicionando um cookie ao final de lanches.
print(lanche)
lanche.insert(0, 'Cachorro-Quente') #* O método insert te deixa adicionar algo em uma determinada posição da lista, no caso aqui estamos adicionando
print(lanche)                       #* um cachorro-quente ao começo da lista, o que faz com que os outros dados avancem uma posição.

#! Formas de deletar algo de uma lista:

del lanche[3] #* Com o comando del é possível deletar um valor de dentro de uma lista.
print(lanche)
lanche.insert(3, 'Pizza')
print(lanche)

lanche.pop(3) #* O método pop também te deixa deletar algo dentro de uma lista.
print(lanche) #* Normalmente o método pop é utilizado para eliminar o último elemento dentro de uma lista, mas é possível colocar o parâmetro que você deseja eliminar.
lanche.insert(3, 'Pizza') #* Por exemplo, lanche.pop() removeria o índice "Cookie" ao final da lista.

lanche.remove('Pizza') #* Essa é uma forma de remover um item de uma lista pelo conteúdo.
print(lanche)
lanche.insert(3, 'Pizza')


#? Caso tente remover um item que não está em uma lista voc~e vai receber um erro. Nesse caso é possível criar um if in para remover um item de 
#? uma lista apenas se esse item estiver na lista.
print(lanche)
if 'Pizza' in lanche:
    lanche.remove('Pizza')
    print(lanche)

#! Também é possível criar lista através de ranges:
valores = list(range(4,11)) #* list é uma função. Nesse caso será feita uma contagem de 4 até 10 dentro de uma lista chamada valores. 
print(valores)              #* Lembrando que o último número (11) é sempre desconsiderado.

valores2 = [8, 2, 5, 4, 9, 3, 0] #* Essa é uma lista com valores fora de ordem.
print(valores2)
valores2.sort()                   #* Com o método sort é possível ordenar esses valores.
print(valores2)
valores2.sort(reverse=True)       #* E essa é uma forma de ordenar ao contrário. Lembrando sempre que True é sempre com T maiúsculo.
print(valores2)
print(len(valores2))              #* 0, 1, 2, 3, 4, 5, 6, 7. Lembrar que sempre começa em 0.


###### Prática ######

num = [2, 5, 9, 1]
print(num)
num[2] = 3    #* Essa é uma outra forma de substituir um valor dentro de uma lista.
print(num)    #* Porém, não é possível adicionar um novo valor dentro de uma lista dessa forma. Por exemplo: num[4] = 7, isso não funcionaria.
num.append(7) #* Dessa forma é possível adicionar o valor 7 ao final da lista num.
print(num)
num.insert(2, 0)  #* Adicionando o valor 0 na segunda posição, no caso no lugar de 2.
num.sort      #* Ordenar os valores. (reverse=True) ao contrário.
print(f'Essa lista tem {len(num)} elementos.')     #* Mostrar quantos valores tem dentro da lista.
num.pop()     #* Dessa forma o último valor dentro da lista será removido. Se adicionar algo dentro de () removerá a posição indicada. Ex: num.pop(2)
print(num)    #* Nesse caso o segundo item dentro da lista, não o número 2. Para remover o valor 2 seria necessário usar remove.
num.insert(2, 2)
print(num)
num.remove(2) #* O remove irá remover apenas a primeira ocorrência do 2 dentro da lista.
print(num)

#! É possível criar uma lista vazia de duas formas.
#* valores = []
#* valores = list()

valores3 = []
valores3.append(5)
valores3.append(9)
valores3.append(4)
print(valores3)

#! Também é possível adicionar valores dentro de uma lista usando for e input. Ex:
#* for count in range(0, 5):
    #* valores.append(int(input('Digite um valor: ')))

for v in valores3:
    print(f'{v}...', end='') #* Uma forma de mostrar os valores usando for, com o end= para colocá-los na mesma linha.

for c, v, in enumerate(valores3):                     #? O enumerate é usado para mostrar a chave do índice. 
    print(f'\nNa posição {c} encontrei o valor {v}!') #? Nesse caso está sendo mostrado a posição e o valor nessa posição.

a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')        #! A partir do momento que uma lista é igualada com outra o Python cria uma ligação entre ambas.
                              #! Então nesse caso qualquer coisa modificada em uma lista será modificada na outra.

#? Para fazer uma cópia de uma lista é só seguir esse exemplo:
d = [2, 3, 4, 7]
e = d[:]
print(f'Lista D: {d}')
print(f'Lista E: {e}')
e[2] = 8
print(f'Lista D: {d}')
print(f'Lista E: {e}')    #! Dessa forma é feita uma cópia da lista e os valores na lista D não são modificados, mas na lista E eles são.
                          #! Diferente da forma anterior onde é criada uma ligação entre ambas.


######### Parte 2 ########
######### Teoria  ########

dados = list()
dados.append('Pedro') #* Posição 0.
dados.append(25)      #* Posição 1.
print(dados[0])
print(dados[1])

pessoas = list()
#*pessoas.append(dados[:])   * [:] Gera uma cópia de dados, um fatiamento. Agora dentro da lista pessoas a posição 0 é foramada por Pedro, 25.

#? Outra forma de se fazer uma lista dentro de outra lista é a seguinte:
pessoas = [['Pedro', 25],['Maria', 19], ['João', 32]]       #! Assim você tem três listas dentro de uma mesma lista chamada pessoas. 0, 1 e 2.

#? Formas de puxar os valores dentro das listas.
print(pessoas[0][0])     #* Dessa forma será puxado o valor 0 dentro da lista pessoas, puxando o 0 dentro da lista dados. No caso Pedro.
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])

#? Outra forma de buscar e mostrar valores em uma lista, utilizando for:
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')   #! Dessa forma eu vou estar mostrando o nome e a idade das pessoas na lista.

####### Prática #######

teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()          #* Outra forma de criar essa lista:
galera.append(teste[:])  #* galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galerinha = list()
dado = list()
total_maior = 0
total_menor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galerinha.append(dado[:])
    dado.clear()
for p in galerinha:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        total_maior = total_maior + 1
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor = total_menor + 1
print(f'Temos {total_maior} maiores de idade e {total_menor} menores de idade.')
