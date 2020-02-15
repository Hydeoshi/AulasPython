vel = int(input('Qual a velocidade do carro? '))
if vel >= 80:
    print('O carro está rápido demais e foi multado.')
    multa = vel * 7.0
    print('O valor da multa é de R${:.2f}.'.format(multa))
else:
    print('O carro não está rápido demais.')
