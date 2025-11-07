#Validacion de la variable nombre_producto 
while True: 
    nombre_producto = str(input('Ingrese el nombre del producto: ')) #Solicitar nombre del producto
    
    if not nombre_producto: #Verifica que el nombre no puede quedar vacio
        print('El nombre no puede quedar vacio. Ingrese el nombre del producto') 
    elif not all(c.isalpha() or c.isspace() for c in nombre_producto): #Verifica que el nombre si sea un string y no otro caracter
        print(f'Error, el {nombre_producto} no es un producto. Ingrese nuevamente el nombre del producto: ') 
    else:
        break; #Valida el nombre ingresado

#Validacion de la variable precio_producto s
while True:
    try:
        precio_producto = float(input('Ingrese el precio del producto: ')) #Solicitar el precio del producto
        if precio_producto >= 0: 
            break; #Valida que el dato si sea un numero
        else: 
            print('El precio no puede ser un numero negativo') # Mensaje de error si el precio es un numero negativo
    except ValueError:
        print('El dato ingresado es erroneo. Ingrese nuevamente el precio del producto: ') # Mensaje de erro si el precio no es un numero 

#Validacion de la variable cantidad_producto
while True:
    try:
        cantidad_producto = int(input('Ingrese la cantidad del producto: ')) #Solicita la cantidades del producto
        if cantidad_producto >= 0:
            break; #Valida que el dato si sea un numero
        else:
            print('La cantidad no puede ser un numero negativo') #Mensaje de error si la cantidad es un numero negativo
    except ValueError:
        print('El dato ingresado es erroneo. Ingrese nuevamente la cantidad del producto: ') #Mensaje de error si la cantidad no es un numero

# Operacion al costo total
costo_total = precio_producto * cantidad_producto

# Mostrar en terminal nombre, precio, cantidad y el costo total
print(f'Nombre: {nombre_producto}')
print(f'Precio unitario: {precio_producto}')
print(f'Cantidad: {cantidad_producto}')
print(f'Costo total: {costo_total}')