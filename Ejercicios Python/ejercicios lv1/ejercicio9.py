valor_producto = 2000
unidades = int(input('Ingrese la cantidad de productos comprados: '))

total = valor_producto * unidades


if unidades >= 30:
    total_con_descuento = total * 0.85   # 15% de descuento
elif unidades >= 10:
    total_con_descuento = total * 0.95   # 5% de descuento
else:
    total_con_descuento = total          # sin descuento

if total_con_descuento < 50000:
    total_final = total_con_descuento + 5000
else:
    total_final = total_con_descuento

print(f"Total final a pagar: ${total_final}")
