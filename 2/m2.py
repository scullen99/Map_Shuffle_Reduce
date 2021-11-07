#!/usr/bin/python3

# 2.Facturación media por mes de un proveedor.
import sys

# dividir en tabuladores
for line in sys.stdin:
    filas = line.split("\t")

    # comprobar las columnas
    if len(filas) != 9 or filas[1] != "Infraestructuras Fracturas":
        continue

    # Casteo de strings a ints
    try:
        filas[5] = filas[5].split("/")[1]
        filas[8] = float(filas[8])
    except ValueError:
        continue

    print(f"{filas[5]},{filas[8]}")