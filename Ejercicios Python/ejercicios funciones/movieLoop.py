def calcular_entradas():
    while True:
        try: 
            opcion = int(input('1. Ingresar edad\n0. Salir del programa\nSu opcion: '))
        except:
            print('ERROR! Solo se acepta una opcion de 0 o 1')
            continue

        if opcion == 1:
            edad = int(input('Ingrese su edad: '))

            if(edad < 12 and edad > 0):
                precio = 5000.0
                print(f'Precio aplicado: {precio}')
            elif (edad >= 12 and edad <= 59): 
                precio = 8000.0
                print(f'Precio aplicado: {precio}')
            else:
                precio = 4000.0
                print(f'Precio aplicado: {precio}')
        
        else:
            print('Usted a salido del programa')
            break

calcular_entradas()