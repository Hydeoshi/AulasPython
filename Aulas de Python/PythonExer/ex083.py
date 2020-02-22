 #* Crie um programa onde o usuário digite uma expressão matemática qualquer que use parênteses.
 #* Seu aplicativo deverá analisar se a expressão passada está com parênteses abertos e fechados na ordem correta.

exp = list()
parenteses = list()
exp_matematica = str(input('Digite uma expressão matemática: '))
for mat in exp_matematica:
    if mat == '(':
        parenteses.append('(')
    elif mat == ')':
        parenteses.append(')'),
if len(parenteses) % 2 == 0:
    print(f'Operação Válida. Sua expressão matemática é: {exp_matematica}')
else:
    print(f'Operação Inválida. Por favor cheque se sua expressão matemática está correta: {exp_matematica}')
