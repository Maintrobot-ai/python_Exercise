def calcular_propina(total_cuenta):

    if(total_cuenta > 100000.0):
        propina = 0.15
    else:
        propina = 0.10
    
    total_final = total_cuenta + propina

    print(f'Total de la cuenta: ${total_cuenta:,.0f}')
    print(f'Propina aplicada: ${propina:,.2f}')
    print(f'Total a pagar: ${total_final:,.2f}')

    return total_final

calcular_propina(int(input('Ingrese el valor de la cuenta: ')))