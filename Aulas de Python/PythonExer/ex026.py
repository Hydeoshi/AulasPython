#Sempre lembrar de adicionar strip() quando se trata de um input, assim evitando erros por conta do usuário.
frase = str(input('Digite uma frase: ')).strip().upper()
#O .upper() foi usado para evitar problemas com a frase ser digitada em minúsculo. Ao invés do upper poderia ter sido usado um .lower(), seguindo o mesmo princípio.
#Nesse caso o count() seria com um 'a', ao invés de um 'A'.
print(' Na sua frase a letra A aparece {} vezes!'.format(frase.count('A')))
print(' Na sua frase a letra A aparece pela primeira vez na posição {}.'.format(frase.find('A')+1))
#rfind é usado para encontrar coisas começando pela direita. "Rightfind". O +1 ao lado dos finds é para adicionar mais uma posição na contagem, assim tornando mais fácil
#de entender, já que o Python começa a contar a partir de 0.
print(' Na sua frase a letra A aparece pela última vez na posição {}.'.format(frase.rfind('A')+1 ))
