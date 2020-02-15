 #* Crie um programa que tenha uma tupla com várias palavras (Não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Cachorro', 'Cavalo', 'Aviao', 'Macaco', 'Teste', 'Pombo', 'Gato', 'Papagaio', 'Campones', 'Dinheiro', 'Nota',
'Warcraft', 'Pongo', 'Bobo')

for c in palavras:
    print(f'\n Na palavra {c.upper()} temos as vogais: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')