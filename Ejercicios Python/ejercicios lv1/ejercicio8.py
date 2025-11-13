nota_tecnica = float(input('Ingrese la primera nota (0.0 al 5.0): '))
nota_logica = float(input('Ingrese la segunda nota (0.0 al 5.0): '))

if (0 <= nota_tecnica <= 5) and (0 <= nota_logica <= 5):
    nota_final = (nota_tecnica * 0.7) + (nota_logica * 0.3)
    print(f'Nota final: {nota_final:.2f}')
    
    if 3 <= nota_final <= 5:
        print('Aprobado')
    elif 2 <= nota_final < 3:
        print('Revisión')
    elif nota_final < 2:
        print('Reprobado')
else:
    print('Error: las notas deben estar entre 0.0 y 5.0')