#!/usr/bin/python3

# 6. Densidad media de las ventas con envío de tipo 1.
import sys

# dividir en tabuladores
for line in sys.stdin:
    filas = line.split("\t")

    # comprobar las columnas
    if len(filas) != 9 or filas[2] != "1" or filas[4] == "0":
        continue

    # Casteo de strings a ints
    try:
        filas[3] = int(filas[3])
        filas[4] = int(filas[4])
    except ValueError:
        continue

    print(f"{filas[3]},{filas[4]}")