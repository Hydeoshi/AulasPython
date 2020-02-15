#from colorama import Fore, Back, Style
nome = str(input('Qual é o seu nome? '))
#Os códigos de cores podem ser usados tanto no format quanto fora dele.
print('\033[4;30;45mOlá, mundo!\033[m')
print('É um prazer te conhecer {}{}{}.'.format('\033[4;31m', nome, '\033[m'))
#print('É um prazer conhecer você {}{}{}.'.format(Fore.RED, nome, Style.RESET_ALL ))


