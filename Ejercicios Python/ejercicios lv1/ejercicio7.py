menu = 12000
bebida = 3000
iva = 0.08
opcion_bebida = str(input('Desea agregar bebida? (s/n): '.lower()))

if(opcion_bebida == 's'):
    subtotal = menu + bebida
    total_iva = subtotal * iva
    total = subtotal + total_iva
    print(f'Total a pagar: {total}')
elif (opcion_bebida == 'n'):
    subtotal = menu
    total_iva = subtotal * iva
    total = subtotal + total_iva
    print(f'Total a pagar: {total}')
else:
    print('Error, ese dijito no es valido')
