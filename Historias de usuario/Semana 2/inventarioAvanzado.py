import time  # Importación del módulo time para generar pausas y simular carga

# Diccionario donde se almacenan los valores del inventario
inventario = {
    'nombre': [],
    'precio': [],
    'cantidad': []
}

def cargar_animacion(mensaje="Subiendo datos", segundos=3, intervalo=1):
    """Animación simple de carga usando solo time."""
    print(mensaje, end="")
    for _ in range(segundos):  # Ciclo que imprime un punto cada segundo
        time.sleep(intervalo)
        print(".", end="")
    print()  # Salto de línea al terminar


# ---------------------------------------------------------
# FUNCIÓN PARA AGREGAR PRODUCTOS AL INVENTARIO
# ---------------------------------------------------------
def agregar_inventario(inventario):
    # Ciclo infinito que permite agregar varios productos seguidos
    while True:
        print('!--------------------- Agregar producto ---------------------!')

        # El usuario ingresa los datos del producto
        agregar_nombre = input('Ingrese el nombre del producto: ').strip()
        if not agregar_nombre:
            print("[ERROR] El nombre no puede estar vacío.\n")
            continue  # Reinicia el ciclo y vuelve a pedir los datos

        # Validación del precio ingresado
        try:
            precio_producto = float(input('Ingrese el precio del producto: ').strip())
            if precio_producto < 0:
                print("[ERROR] El precio no puede ser negativo.\n")
                continue
        except ValueError:
            print("[ERROR] Precio inválido. Debes ingresar un número.\n")
            continue

        # Validación de la cantidad ingresada
        try:
            cantidad_producto = int(input('Ingrese la cantidad del producto: ').strip())
            if cantidad_producto < 0:
                print("[ERROR] La cantidad no puede ser negativa.\n")
                continue
        except ValueError:
            print("[ERROR] Cantidad inválida. Debes ingresar un entero.\n")
            continue

        # Agregar los datos al inventario
        inventario['nombre'].append(agregar_nombre)
        inventario['precio'].append(precio_producto)
        inventario['cantidad'].append(cantidad_producto)

        # Simulación de carga usando un ciclo
        cargar_animacion("Subiendo datos", segundos=3, intervalo=1)
        print('Datos subidos correctamente!\n')

        # Pregunta si desea continuar agregando productos
        continuar = input("¿Desea agregar otro producto? (s/n): ").strip().lower()

        # Condicional: si NO escribe "s", sale y vuelve al menú
        if continuar != "s":
            print("Regresando al menú...\n")
            break  # Rompe el ciclo while True


# ---------------------------------------------------------
# FUNCIÓN PARA MOSTRAR EL INVENTARIO
# ---------------------------------------------------------
def mostrar_inventario(inventario):

    # Condicional que detecta si el inventario está vacío
    if not inventario['nombre']:
        print('[ADVERTENCIA]: El inventario está vacío, ingrese 1 para empezar a agregar valores.\n')
        return  # Sale de la función sin intentar imprimir nada

    print('!--------------------- Inventario ---------------------!')

    # Ciclo que recorre el inventario usando los índices de las listas
    for i in range(len(inventario['nombre'])):
        print(
            f'Producto {i+1}:\n'
            f'  Nombre: {inventario["nombre"][i]} | '
            f'Precio: {inventario["precio"][i]} | '
            f'Cantidad: {inventario["cantidad"][i]}'
        )

    print('!------------------------------------------------------!\n')


# ---------------------------------------------------------
# FUNCIÓN PARA CALCULAR ESTADÍSTICAS DEL INVENTARIO
# ---------------------------------------------------------
def calcular_estadisticas(inventario):

    # Condicional que evita cálculos cuando no hay datos
    if not inventario['nombre']:
        print("[ADVERTENCIA]: El inventario está vacío. ingrese 1 para empezar a agregar valores.\n")
        return

    print('!--------------------- Estadísticas ---------------------!')

    # Cuenta cuántos productos existen en el inventario
    total_productos = len(inventario['nombre'])

    # Variable acumuladora para el valor total del inventario
    valor_total = 0.0

    # Ciclo para recorrer cada producto y calcular (precio * cantidad)
    for i in range(total_productos):
        valor_total += inventario['precio'][i] * inventario['cantidad'][i]

    # Resultados finales
    print(f'Cantidad total de productos registrados: {total_productos}')
    print(f'Valor total del inventario: ${valor_total:,.2f}')
    print('!------------------------------------------------------!\n')


# ---------------------------------------------------------
# MENÚ PRINCIPAL DEL PROGRAMA
# ---------------------------------------------------------
def main():
    # Ciclo principal que mantiene funcionando el programa hasta que el usuario elija salir
    while True:
        try:
            # Se pide una opción al usuario
            opcion_usuario = int(input(
                '!--------------------- Menu Inventario ---------------------!\n'
                '1. Agregar productos\n'
                '2. Mostrar inventario\n'
                '3. Calcular estadísticas\n'
                '4. Salir\n'
                'Opcion: '
            ).strip())
            print()  # Salto de línea

            # Condicional para opciones fuera del menú
            if opcion_usuario < 1 or opcion_usuario > 4:
                print(f'[ERROR]: {opcion_usuario} no está entre las opciones, intente nuevamente.\n')

            # Opción 1: agregar inventario
            elif opcion_usuario == 1:
                agregar_inventario(inventario)

            # Opción 2: mostrar inventario
            elif opcion_usuario == 2:
                mostrar_inventario(inventario)

            # Opción 3: calcular estadísticas
            elif opcion_usuario == 3:
                calcular_estadisticas(inventario)

            # Opción 4: cerrar programa
            else:
                # Ciclo regresivo antes de cerrar
                for tiempo in range(3, 0, -1):
                    print(f'Cerrando programa en: {tiempo}...')
                    time.sleep(1)
                print('¡Programa cerrado exitosamente!')
                break  # Rompe el ciclo while True y finaliza el programa

        except ValueError:
            # Este except captura cuando el usuario ingresa letras o símbolos en vez de un número
            print('[ERROR]: Entrada inválida. Debes ingresar un número del 1 al 4.\n')

if __name__ == "__main__":
    main()