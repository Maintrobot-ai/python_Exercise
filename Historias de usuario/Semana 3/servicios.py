"""
Módulo de servicios para la gestión del inventario.

Contiene funciones para agregar, mostrar, buscar, actualizar,
eliminar productos, calcular estadísticas y manejar persistencia en CSV.
"""

import csv
import time


def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un producto al inventario si no existe.

    Parámetros:
        inventario (list): Lista de productos (diccionarios).
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
        cantidad (int): Cantidad disponible.

    Retorno:
        bool: True si se agregó, False si ya existía.
    """
    # Verificar duplicados
    for producto in inventario:
        if producto['nombre'] == nombre:
            return False
        
    # Agregar nuevo producto al inventario
    inventario.append({
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    })

    return True


def mostrar_inventario(inventario):
    """
    Imprime en pantalla el inventario completo.

    Parámetros:
        inventario (list): Lista de productos.
    """
    if not inventario:
        print('[AVISO]: El inventario se encuentra vacio')
        for tiempo in range(3, 0, -1):
            time.sleep(1)
        return
    
    # Mostrar cada producto formateado
    for producto in inventario:
        print(f"""
|============================================|
| Producto: {producto['nombre']}
| Precio:   {producto['precio']}
| Cantidad: {producto['cantidad']}
|============================================|
""")


def buscar_producto(inventario, nombre):
    """
    Busca un producto en el inventario por nombre.

    Parámetros:
        inventario (list): Lista de productos.
        nombre (str): Nombre a buscar.

    Retorno:
        dict | None: Producto encontrado o None si no existe.
    """
    for producto in inventario:
        if producto['nombre'] == nombre:
            return producto
    
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o cantidad de un producto existente.

    Parámetros:
        inventario (list): Lista de productos.
        nombre (str): Nombre del producto a modificar.
        nuevo_precio (float | None): Nuevo precio, None si no cambia.
        nueva_cantidad (int | None): Nueva cantidad, None si no cambia.

    Retorno:
        bool: True si se actualizó, False si no existe.
    """
    for producto in inventario:
        if producto['nombre'] == nombre:
            if nuevo_precio is not None:
                producto['precio'] = nuevo_precio   
            if nueva_cantidad is not None:
                producto['cantidad'] = nueva_cantidad  
            return True
        
    return False


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.

    Parámetros:
        inventario (list): Lista de productos.
        nombre (str): Nombre del producto a eliminar.

    Retorno:
        bool: True si se eliminó, False si no existe.
    """
    for producto in inventario:
        if producto['nombre'] == nombre:
            inventario.remove(producto)
            return True
    
    return False


def calcular_estadisticas(inventario):
    """
    Calcula métricas generales del inventario.

    Parámetros:
        inventario (list): Lista de productos.

    Retorno:
        dict: Total de productos, valor total,
              producto más caro y con más unidades.
    """
    if not inventario:
        return {
            "total_productos": 0,
            "valor_total": 0,
            "producto_mas_caro": None,
            "producto_con_mas_stock": None
        }
    
    # Cálculos estadísticos
    total_productos = len(inventario)
    valor_total = sum(p['precio'] * p['cantidad'] for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p['precio'])
    producto_con_mas_stock = max(inventario, key=lambda p: p['cantidad'])

    return {
        "total_productos": total_productos,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro["nombre"],
        "producto_con_mas_stock": producto_con_mas_stock["nombre"]
    }


def guardar_csv(inventario, nombre_archivo="inventario.csv"):
    """
    Guarda el inventario en un archivo CSV.

    Parámetros:
        inventario (list): Lista de productos.
        nombre_archivo (str): Nombre del archivo destino.

    Retorno:
        bool: True si se guardó correctamente, False si falló.
    """
    if not inventario:
        print("[ERROR]: No hay productos para guardar.")
        for tiempo in range(3, 0, -1):
            time.sleep(1)
        return False

    # Asegurar extensión CSV
    if not nombre_archivo.lower().endswith(".csv"):
        nombre_archivo += ".csv"

    try:
        # Guardar datos tabulares
        with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio", "cantidad"])
            escritor.writeheader()
            escritor.writerows(inventario)

        print(f"[AVISO]: Inventario guardado exitosamente en '{nombre_archivo}'.")
        for tiempo in range(3, 0, -1):
            time.sleep(1)
        return True

    except Exception as e:
        print(f"[ERROR]: No se pudo guardar el archivo: {e}")

    for tiempo in range(3, 0, -1):
        time.sleep(1)
    return False


def cargar_csv(inventario, nombre_archivo="inventario.csv"):
    """
    Carga un inventario desde un archivo CSV existente.

    Parámetros:
        inventario (list): Lista de productos a sobrescribir.
        nombre_archivo (str): Nombre del archivo origen.

    Retorno:
        bool: True si se cargó correctamente, False si falló.
    """
    # Asegurar extensión CSV
    if not nombre_archivo.lower().endswith(".csv"):
        nombre_archivo += ".csv"

    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            # Validar estructura del CSV
            if lector.fieldnames != ["nombre", "precio", "cantidad"]:
                print("[ERROR]: El archivo CSV no tiene el formato correcto.")
                for tiempo in range(3, 0, -1):
                    time.sleep(1)
                return False

            # Borrar inventario previo y cargar nuevos datos
            inventario.clear()

            for fila in lector:
                inventario.append({
                    "nombre": fila["nombre"],
                    "precio": float(fila["precio"]),
                    "cantidad": int(fila["cantidad"])
                })

        print(f"[AVISO]: Inventario cargado correctamente desde '{nombre_archivo}'.")
        for tiempo in range(3, 0, -1):
            time.sleep(1)
        return True

    except Exception as e:
        print(f"[ERROR]: No se pudo cargar el archivo: {e}")

    for tiempo in range(3, 0, -1):
        time.sleep(1)
    return False
