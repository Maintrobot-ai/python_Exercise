horas = int(input('Ingrese la cantidad de horas: '))

if (horas >= 0):
    total = 2000 * horas
    if (horas == 0):
        print('Usted no a usado el parqueadero')
    print(f'Total a pagar: {total}')
else:
    print('Error, no se permite numeros negativos')