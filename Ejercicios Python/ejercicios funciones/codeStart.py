def tablaMultiplicar(numero):
    for i in range(1,11):
        resultado = numero * i
        if resultado > 50:
            print(f'{numero} x {i} = {resultado} -> Resultado alto')
        else:
            print(f'{numero} x {i} = {resultado}')

tablaMultiplicar(int(input('Ingrese un numero: ')))