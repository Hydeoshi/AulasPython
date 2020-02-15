dias = int(input('Por quantos dias você ficou com o carro?'))
km = float(input('Quantos quilómetros você rodou com o carro?'))
aluguel = (dias * 60) + (0.15 * km)
print('O valor a ser pago é de: R${:.2f}.'.format(aluguel))