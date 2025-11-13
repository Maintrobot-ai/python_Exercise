valor_libro = 25000.0
es_estudiante = str(input('Eres estudiante?:  '.strip() .lower()))
cupon = str(input('Tienes cupon? (Enter en caso que no tengas): '.strip() .upper()))
total = valor_libro

if(es_estudiante == 's'):
    total *= 0.85

    if(cupon == 'LIBRO10'):
        total *= 0.90
    elif cupon != "":
        print('Cupon incorrecto, no se aplicara descuento')
else:
    if cupon != '':
        print('El cupon solo se aplica para estudiantes')

print(f'Total a pagar: ${total}')