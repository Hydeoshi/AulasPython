num = 0
while True:
    num = int(input('Gostaria de ver a tabuada de qual valor? '))
    if num < 0:
        break
    print(f'=====TABUADA DO {num}=====')
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
print('Programa Tabuada encerrado.')

