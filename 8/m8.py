#!/usr/bin/python3

# 8. Envíos (origen – destino) con más tráfico en un año determinado.
import sys

# dividir en tabuladores
for line in sys.stdin:
    filas = line.split("\t")

    # comprobar las columnas
    if len(filas) != 9:
        continue

    try:
        if filas[5].split("/")[2] != "2001":
            continue
    except IndexError:
        continue

    try:
        filas[0] = int(filas[0])
        filas[2] = int(filas[2])
        filas[3] = int(filas[3])
        filas[4] = int(filas[4])
        filas[8] = float(filas[8])
    except ValueError:
        continue

    print(f"{filas[6]}-{filas[7]}")