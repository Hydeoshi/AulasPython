alt = float(input('Quanto de altura tem a parede a ser pintada?'))
lar = float(input('Quanto de largura tem a parede a ser pintada?'))
ar = alt*lar
tin = ar/2
print('A área da sua parede a ser pintada é de {}m². O nosso galão de tinta pinta uma área de 2m², então você vai precisar de {}l de tinta para completar o serviço.'.format(ar,tin))