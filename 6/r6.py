#!/usr/bin/python3

# 6. Densidad media de las ventas con envío de tipo 1.
import sys

densidad = 0
count = 0

for item in sys.stdin:
    col = item.split(",")
    peso = int(col[0])
    volumen = int(col[1])

    densidad += peso/volumen
    count += 1

print(f"Densidad media: {densidad/count:.2f}Kg/m3")