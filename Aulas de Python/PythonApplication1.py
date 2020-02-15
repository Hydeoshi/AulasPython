p1 = int(input('Insira um número:'))
p2 = int(input('Insira outro número:'))
rs = p1+p2
rm = p1*p2
rd = p1/p2
rdi = p1//p2
re = p1**p2
print(' O resultado da soma entre {} e {} é: {}.\n O produto é: {}.\n A divisão é: {:.3f}.\n A divisão inteira é: {}.\n A potência é: {}.'.format(p1,p2,rs,rm,rd,rdi,re))
