#!/usr/bin/python3

# 5. Ventas de mayor y menor valor realizado en un año determinado y proveedores que la han realizado.
import sys

# dividir en tabuladores
for line in sys.stdin:
    filas = line.split("\t")

    # comprobar las columnas
    if len(filas) != 9:
        continue

    try:
        if filas[5].split('/')[2] != '2001':
            continue
        filas[8] = float(filas[8])
    except:
        continue

    print(f"{filas[1]},{filas[8]}")