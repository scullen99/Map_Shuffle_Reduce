#!/usr/bin/python3

# 1. Facturación total de un proveedor.
import sys

# dividir en tabuladores
for line in sys.stdin:
    filas = line.split("\t")

    # comprobar las columnas
    if len(filas) != 9 or filas[1] != "Infraestructuras Fracturas":
        continue

    # Casteo de strings a ints
    try:
        filas[8] = float(filas[8])
    except ValueError:
        continue

    print(filas[8])