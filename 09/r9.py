#!/usr/bin/python3

# 9. Ciudad con más envíos. Entrada de envíos más salida de envíos.
import sys

ciudad_max = ""
cantidad_max = 0

ciudad = ""
cantidad = 0

for item in sys.stdin:
    item = item.strip()
    if item != ciudad:
        if cantidad > cantidad_max:
            cantidad_max = cantidad
            ciudad_max = ciudad

        ciudad = item
        cantidad = 0

    cantidad += 1

print(f"La ciudad con mas trafico seria: {ciudad_max}")