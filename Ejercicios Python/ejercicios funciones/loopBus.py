def simular_viaje(pasajeros):
    for i in range(1, pasajeros + 1):
        print(f'Pasajero {i} a bordo')
        if (i == 10):
            print('Bus lleno!')
            break

simular_viaje(int(input('Ingrese la cantidad de pasajeros: ')))
