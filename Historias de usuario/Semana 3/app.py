"""
Aplicación principal del sistema de inventario.

Maneja la interacción con el usuario mediante menú,
recibe entradas de consola y llama funciones del módulo servicios.
"""

import time

from servicios import (
    agregar_producto,
    mostrar_inventario,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas,
    guardar_csv,
    cargar_csv
)


def menuPrincipal():
    """
    Función principal del programa.

    Crea y mantiene el inventario en memoria,
    muestra el menú de opciones y ejecuta operaciones
    dependiendo de la selección del usuario.
    """
    inventario = []

    while True:
        try:
            opcion = int(input(f'|============================================|\n'
                               f'|1. Agregar producto.                        |\n'
                               f'|2. Mostrar inventario.                      |\n'
                               f'|3. Buscar producto.                         |\n'
                               f'|4. Actualizar producto.                     |\n'
                               f'|5. Eliminar producto.                       |\n'
                               f'|6. Calcular estadisticas.                   |\n'
                               f'|7. Guardar CSV.                             |\n'
                               f'|8. Cargar CSV.                              |\n'
                               f'|9. Salir del programa.                      |\n'
                               f'|============================================|\n'
                               f'|[OPCION]: '))
            # Validar rango de opción
            if(opcion < 1 or opcion > 9):
                print('[ERROR]: Su valor no se encuentra en las opciones. Por favor escoga un digito del 1 al 9')
                for tiempo in range(3,0,-1):
                    time.sleep(1)
            # Agregar producto nuevo
            elif (opcion == 1):
                while True:
                    nombre = str(input('Nombre del producto: '))

                    if nombre.replace(" ", "").isalpha():
                        break
                    print("[ERROR] El nombre solo puede contener letras. Inténtelo de nuevo.")
                    for tiempo in range(2,0,-1):
                        time.sleep(1)
                while True:
                    try:
                        precio = float(input('Valor del producto: '))

                        if precio > 0:
                            break
                        else:
                            print("[ERROR] El precio debe ser un número mayor a 0.")
                    
                    except ValueError:
                            print("[ERROR] Debe ingresar un número válido.")

                while True:
                    try:
                        cantidad = int(input('Cantidad del producto: '))

                        if cantidad > 0:
                            break;
                        else:
                            print("[ERROR] La cantidad debe ser un número mayor a 0.")
                    except ValueError:
                        print("[ERROR] Debe ingresar un número válido.")

                if agregar_producto(inventario, nombre, precio, cantidad):
                    print('[AVISO]: El producto se a agregado exitosamente.')
                    for tiempo in range(2,0,-1):
                        time.sleep(1)
                else:
                    print('[AVISO]: El producto ya existe en el inventario')
                    for tiempo in range(2,0,-1):
                        time.sleep(1)
            # Mostrar inventario
            elif (opcion == 2):
                mostrar_inventario(inventario)
                for tiempo in range(3,0,-1):
                    time.sleep(1) 
            # Buscar producto
            elif (opcion == 3):
                while True:
                    nombre = str(input('Nombre del producto: '))

                    if nombre.replace(" ", "").isalpha():
                        break
                    print("[ERROR] El nombre solo puede contener letras. Inténtelo de nuevo.")
                    for tiempo in range(2,0,-1):
                        time.sleep(1)

                producto = buscar_producto(inventario, nombre)
                print(producto if producto else "[ERROR]: Producto no encontrado")
                for tiempo in range(3,0,-1):
                    time.sleep(1)
            # Actualizar producto
            elif (opcion == 4):
                while True:
                    nombre = input('Ingrese el nombre del producto a actualizar: ').strip()

                    if not nombre.replace(" ", "").isalpha():
                        print("[ERROR] El nombre solo puede contener letras. Inténtelo de nuevo.")
                        continue

                    producto = buscar_producto(inventario, nombre)
                    if not producto:
                        print('[ERROR]: Producto no encontrado en el inventario. Inténtelo de nuevo.')
                        continue 

                    # Mostrar información actual
                    print(f"Producto actual: {producto}")

                    while True:
                        nuevo_precio = input('Ingrese el nuevo precio (Presione ENTER para no cambiar): ').strip()
                        if nuevo_precio == "":
                            nuevo_precio = None
                            break
                        try:
                            nuevo_precio = float(nuevo_precio)
                            if nuevo_precio <= 0:
                                print("[ERROR] El precio debe ser mayor que 0.")
                                continue
                            break
                        except ValueError:
                            print("[ERROR] Debe ingresar un número válido.")

                    while True:
                        nueva_cantidad = input('Ingrese la nueva cantidad (Presione ENTER para no cambiar): ').strip()
                        if nueva_cantidad == "":
                            nueva_cantidad = None
                            break
                        try:
                            nueva_cantidad = int(nueva_cantidad)
                            if nueva_cantidad < 0:
                                print("[ERROR] La cantidad no puede ser negativa.")
                                continue
                            break
                        except ValueError:
                            print("[ERROR] Debe ingresar un número entero válido.")

                    actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
                    print('[AVISO]: Producto actualizado con éxito.')
                    for tiempo in range(3,0,-1):
                        time.sleep(1)
                    break
            # Eliminar producto
            elif (opcion == 5):
                while True:
                    nombre = str(input('Nombre del producto: '))

                    if nombre.replace(" ", "").isalpha():
                        break
                    print("[ERROR] El nombre solo puede contener letras. Inténtelo de nuevo.")
                    for tiempo in range(2,0,-1):
                        time.sleep(1)
                    
                if eliminar_producto(inventario, nombre):
                    print("[AVISO]: Producto eliminado.")
                    for tiempo in range(3,0,-1):
                        time.sleep(1)
                else:
                    print("[AVISO]: No existe este producto.")
                    for tiempo in range(3,0,-1):
                        time.sleep(1)
            # Calcular estadísticas
            elif (opcion == 6):
                stats = calcular_estadisticas(inventario)
                print("Estadísticas:", stats)
                for tiempo in range(3,0,-1):
                    time.sleep(1)
            # Guardar inventario en CSV
            elif (opcion == 7):
                guardar_csv(inventario)
                print('[AVISO]: Inventario guardado en inventario.csv')
                for tiempo in range(3,0,-1):
                    time.sleep(1)
            # Cargar inventario desde CSV
            elif (opcion == 8):
                cargar_csv(inventario)
                print('[AVISO]: Inventario cargado desde inventario.csv')
                for tiempo in range(3,0,-1):
                    time.sleep(1)
            # Salir del programa
            else:
                print('[AVISO]: Saliendo del programa...')
                for tiempo in range(3,0,-1):
                    print(tiempo, '...')
                    time.sleep(1)
                print('[AVISO]: Programa finalizado.')
                break
        
        except ValueError:
            print('[ERROR]: Su opcion no es valida, vuelva a intentarlo.')
            for tiempo in range(3,0,-1):
                time.sleep(1)

# Iniciar la aplicación
menuPrincipal()