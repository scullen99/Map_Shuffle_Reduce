#!/usr/bin/python3

# 7. Tipos de envíos realizados por un proveedor en un mes determinado de un año
# determinado.
import sys

# dividir en tabuladores
for line in sys.stdin:
    filas = line.split("\t")

    # comprobar las columnas
    if len(filas) != 9 or filas[1] != "Electronica Chispas":
        continue

    try:
        """"
        if filas[5].split('/')[1:] != ['11', '2003']:
            continue
        """
        f = filas[5].split('/')
        if f[1] != '11' or f[2] != '2003':
            continue
        filas[2] = int(filas[2])
    except:
        continue

    print(f"{filas[2]}")