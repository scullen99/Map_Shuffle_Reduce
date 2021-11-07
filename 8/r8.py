#!/usr/bin/python3

# 8. Envíos (origen – destino) con más tráfico en un año determinado.
import sys

viaje_max = ""
cantidad_max = 0

viaje = ""
cantidad = 0

for item in sys.stdin:
    item = item.strip()
    if item != viaje:
        if cantidad > cantidad_max:
            cantidad_max = cantidad
            viaje_max = viaje

        viaje = item
        cantidad = 0

    cantidad += 1

print(f"El envio con mas trafico seria: {viaje_max}")