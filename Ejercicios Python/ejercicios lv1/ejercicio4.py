helado_chocolate = 4000.0
helado_vainilla = 3500.0
topings = 1000.0

opcion = int(input('Sabores:\n1. Chocolate\n2. Vainilla\nSu opcion: '))

if(opcion == 1):
    print(f'Ustede escogio el sabor chocolate\nValor: {helado_chocolate}\nDesea agregra topings?: ')
    opcion_topings = str(input('Su opcion: '))

    if(opcion_topings == 's'):
        valor_total = helado_chocolate + topings
        print(f'Total a pagar: {valor_total}')
    elif (opcion_topings == 'n'):
        valor_total = helado_chocolate
        print(f'Total a pagar: {valor_total}')
    else:
        print(f'Error, este valor no es valido')
elif(opcion == 2):
    print(f'Ustede escogio el sabor vainilla\nValor: {helado_vainilla}\nDesea agregra topings?: ')
    opcion_topings = str(input('Su opcion: '))

    if(opcion_topings == 's'):
        valor_total = helado_vainilla + topings
        print(f'Total a pagar: {valor_total}')
    elif (opcion_topings == 'n'):
        valor_total = helado_vainilla
        print(f'Total a pagar: {valor_total}')
    else:
        print(f'Error, este valor no es valido')
else:
    print('Error, este sabor no esta disponible, por favor escoga entre 1 o 2')