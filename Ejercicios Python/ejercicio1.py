precio_pan = 300.0
valor_pan = int(input("Ingrese la cantidad de panes que desea comprar: "))

if (valor_pan >= 20):
    descuento = 0.10
    total = precio_pan * valor_pan * (1 - descuento)
    print(f"Se aplicó un descuento del 10%. El total a pagar es: ${total:.2f}")
elif (valor_pan >= 50):
    descuento = 0.20
    total = precio_pan * valor_pan * (1 - descuento)
    print(f"Se aplicó un descuento del 20%. El total a pagar es: ${total:.2f}")
elif (valor_pan >= 0):
    total = precio_pan * valor_pan
    print(f"No se aplicó ningún descuento. El total a pagar es: ${total:.2f}")
else:
    print("Cantidad inválida. Por favor ingrese un número positivo.")