from math import pow
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / pow(altura, 2)
print('O seu IMC é de: {:.1f}.'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do seu peso ideal.')
elif imc >= 18.6 and imc <=25:
    print('Você está no seu peso ideal.')
elif imc > 25 and imc <=30:
    print('Você está com sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Você está obeso.')
else:
    print('Você está com obesidade morbida!')