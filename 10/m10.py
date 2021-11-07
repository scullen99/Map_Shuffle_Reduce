#!/usr/bin/python3

# 10. Balance de facturación para una ciudad determinada. Ventas cuyo envío se realiza desde una
# ciudad menos las ventas enviadas a dicha ciudad.
import sys

# dividir en tabuladores
for line in sys.stdin:
    filas = line.strip().split("\t")

    # comprobar las columnas
    if len(filas) != 9:
        continue

    try:
        filas[8] = float(filas[8])
    except ValueError:
        continue

    if filas[6] == "Bilbao":
        print(f"{filas[8]}")
    elif filas[7] == "Bilbao":
        print(f"{-filas[8]}")
    else:
        continue