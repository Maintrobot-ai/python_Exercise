def hornear_pan(lotes):
    for lote in range(1, lotes + 1):
        print(f"Horneando lote {lote}...")
        if lote % 3 == 0:
            print("Verificación de calidad ")
    print("Producción terminada.")

hornear_pan(14) 