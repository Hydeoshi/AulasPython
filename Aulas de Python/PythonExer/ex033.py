n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um último número: '))
#Esse código poderia ser feito de forma mais simplificada, especificando um dos números como menor logo de cara e fazendo comparativos com ele:
#menor = n1
#if n2 < n1 and n2 < n3:
#   menor = n2
#if n3 < n1 and n3 < n2:
#   menor = n3
#O maior pode ser feito da mesma forma, assim ocupando menos espaço na linha de código.
#maior = n1
#if n2 > n1 and n2 > n3:
#   maior = n2
#if n3 > n1 and n3 > n2:
#   maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n1:
    maior = n3
print('O \033[31mmaior\033[m número é o \033[31m{}\033[m e o \033[33mmenor\033[m é o \033[33m{}\033[m.'.format(maior, menor))