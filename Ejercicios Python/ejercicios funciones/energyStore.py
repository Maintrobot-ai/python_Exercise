def calcular_puntos(compras):
    puntos = 0
    for compras in range(1, compras + 1):
        if (compras % 3 == 0):
            puntos += 10
        else:
            puntos += 5

    print(f'Puntos totales: {puntos}')

cantidad_compras = (int(input('Ingrese la cantidad de compras: ')))
calcular_puntos(cantidad_compras)
