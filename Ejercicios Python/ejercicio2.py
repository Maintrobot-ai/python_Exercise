edad_cliente = int(input("Ingrese su edad: "))

if (edad_cliente < 5 and edad_cliente >= 0):
    print("La entrada es gratuita para niños menores de 5 años.")
elif(edad_cliente >= 5 and edad_cliente <= 11):
    precio_entrada = 5000.0
    print(f"El precio de la entrada para niños de 5 a 11 años es: ${precio_entrada:.2f}")
elif(edad_cliente >= 12 and edad_cliente <= 59):
    precio_entrada = 8000.0
    print(f"El precio de la entrada para adultos de 12 a 59 años es: ${precio_entrada:.2f}")
elif(edad_cliente >= 60):
    precio_entrada = 4000.0
    print(f"El precio de la entrada para adultos mayores de 60 años es: ${precio_entrada:.2f}")
else:
    print("Edad inválida. Por favor ingrese una edad correcta.")