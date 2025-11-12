import time

def promedio_notas():
    while True:
        print('!------------------- Registro Estudiantil ------------------------!')

        n1 = float(input('Ingrese la primera nota del estudiante: '))
        n2 = float(input('Ingrese la segunda nota del estudiante: '))
        n3 = float(input('Ingrese la tercera nota del estudiante: '))

        if (n1 > 5 or n2 > 5 or n3 > 5 or n1 < 0 or n2 < 0 or n3 < 0):
            print('La nota no puede ser mayor o menor que 0 o 5')
            continue

        promedio = (n1 + n2 + n3) / 3

        if (promedio >= 3.0):
            print(f'Promedio: {promedio:.2f} -> Aprobado')
        else:
            print(f'Promedio: {promedio:.2f} -> Reprobado')

        continuar = str(input('Desea continuar con otro estudiante? (s/n): ')).lower()

        if continuar != 's':
            for tiempo in range(3,0,-1):
                print(f'Saliendo en: {tiempo}')
                time.sleep(1)

            print('Programa cerrado exitosamente')
            break

promedio_notas()