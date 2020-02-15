seg1 = float(input('Insíra o valor do primeiro segmento: '))
seg2 = float(input('Insíra o valor do segundo segmento: '))
seg3 = float(input('Insíra o valor do terceiro segmento: '))
#Está parte abaixo pode ser feita de forma mais longa:
#if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
#Se a soma de dois lados for menor do que uma das retas:
if (seg1 + seg2) > seg3:
    print('Você pode formar um triângulo ', end='')
    #Isso também pode ser feito da seguinte forma: Já que se uma coisa A é igual uma coisa B e uma coisa B é igual uma coisa C, automáticamente A é igual a C.
    #if seg1 == seg2 and seg2 == seg3.
    #Mas no Python é possível simplificar como está abaixo.
    if seg1 == seg2 == seg3:
        print('\033[32mEQUILÁTERO\033[m com esses segmentos.')
    #É necessário checar a diferença entre seg1 com seg3, por isso no final dessa comparação abaixo é importante colocar o seg1.
    elif seg1 != seg2 != seg3 != seg1:
        print('\033[32mESCALENO\033[m com esses segmentos.')
    else:
        print('\033[32mISÓSCELES\033[m com esses segmentos.')
else:
    print('Você \033[31mNÃO\033[m pode formar um triângulo com esses segmentos.')