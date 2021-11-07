#!/usr/bin/python3

# 1. Facturación total de un proveedor.
import sys

facturacion_total = 0

for item in sys.stdin:
    facturacion_total += float(item)

print("Facturacion total: ", round(facturacion_total, 2))