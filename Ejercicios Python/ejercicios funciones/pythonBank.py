def evaluar_credito(ingresos,edad):
    if (ingresos > 2000000.0 and edad >= 25 and edad <= 60):
        print('Creditos aprobados')
    else:
        print('Creditos rechazados')

evaluar_credito(int(input('Ingrese la cantida de creditos: ')),(int(input('Ingrese su edad: '))))