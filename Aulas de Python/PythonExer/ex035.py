print('-=' * 20)
print('Analisador de Triângulos!')
print('-=' * 20)
m1 = float(input('Primeiro seguimento: '))
m2 = float(input('Segundo seguimento: '))
m3 = float(input('Terceiro seguimento: '))
# Esse código pode ser simplificado da seguinte forma:
# if(m1 + m2) > m3: Você pode formar um triângulo.
if m1 < m3 + m3 and m2 < m1 + m3 and m3 < m2 + m1:
    print('Os seus seguimentos \033[32mpodem\033[m um triângulo!')
else:
    print('Os seus seguimentos \033[31mnão\033[m podem formar um triângulo!')
