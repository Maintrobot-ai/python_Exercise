edad = int(input('Ingrese su edad: '))

if (edad >= 18 ):
    tiene_documento = str(input('Tiene documento? (s/n): '.lower()))

    if(tiene_documento == 's'):
        print('Entrada concedida')
    elif (tiene_documento == 'n'):
        print('Debe presentar documento')
    else:
        print('Error, valor no valido')
elif (edad >= 0 and edad <= 17):
    print('Entrada denegada')
else:
    print('Error, no se permiten numeros negativos')