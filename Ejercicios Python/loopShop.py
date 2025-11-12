def aplicar_descuento():
    total = 0

    while True:
        precio = float(input('Ingrese el precio del producto (0 para finalizar): '))
        
        if precio == 0:
            print('Finalizando...')
            break

        if precio > 50000:
            descuento = precio * 0.10
            precio -= descuento
            print(f'Descuento aplicado: ${descuento:.2f}')
        
        total += precio

    print(f'\nEl total de las compras con descuento es: ${total:.2f}')

aplicar_descuento()