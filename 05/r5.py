#!/usr/bin/python3

# 5. Ventas de mayor y menor valor realizado en un año determinado y proveedores que la han realizado.
import sys

proveedor_max = ""
coste_max = 0
proveedor_min = ""
coste_min = float('inf')

proveedor = ""
coste = 0

for item in sys.stdin:
    data = item.strip().split(',')

    if data[0] != proveedor:
        if proveedor != "":
            if coste > coste_max:
                coste_max = coste
                proveedor_max = proveedor
            if coste < coste_min:
                coste_min = coste
                proveedor_min = proveedor

        proveedor = data[0]
        coste = 0

    coste += float(data[1])

print(f"El proveedor con menor facturacion ha sido '{proveedor_min}': {coste_min:.2f}€")
print(f"El proveedor con mayor facturacion ha sido '{proveedor_max}': {coste_max:.2f}€")