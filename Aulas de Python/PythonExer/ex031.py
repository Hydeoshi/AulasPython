dis = int(input('Qual a distância da sua viagem? '))
if dis >= 200:
    soma = dis * 0.45
    print('A sua passagem para uma viagem de {}KM custará R${:.2f}.'.format(dis, soma))
else:
    soma2 = dis * 0.50
    print('A sua passagem para uma viagem de {}KM custará R${:.2f}.'.format(dis, soma2))
