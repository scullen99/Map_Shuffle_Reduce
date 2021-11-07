#!/usr/bin/python3

# 4. Top tres proveedores que más gastan en envíos en un año determinado y coste total de los
# envíos para cada proveedor (Coste de envíos: Tipo 1: 10€, Tipo 2: 5€, Tipo 3: 3€.)
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
        filas[2] = int(filas[2])
    except:
        continue

    print(f"{filas[1]},{filas[2]}")