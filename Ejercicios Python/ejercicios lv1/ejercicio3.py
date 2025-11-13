dias_entrenados = int(input('Ingrese la cantidad de dias entrenados: '))
puntos = 0

if (dias_entrenados >= 4):
    print('Excelente disciplina')
    puntos += 1
    print(f'Puntos de energia: {puntos}')
elif (dias_entrenados == 2 or dias_entrenados == 3):
    print('Bien, pero puedes dar mas')
    print(f'Puntos de energia: {puntos}')
elif (dias_entrenados == 1 or dias_entrenados == 0):
    print('No aflojes, tu puedes mejorar')
    print(f'Puntos de energia: {puntos}')
else:
    print('Error, no se permiten numeros negativos: ')