#!/usr/bin/python3

# 2.Facturación media por mes de un proveedor.
import sys

facturacion_total = 0

months = [0]*12
times = [0]*12

for item in sys.stdin:
    col = item.split(",")
    col[0] = int(col[0])-1
    col[1] = float(col[1])

    months[col[0]] += col[1]
    times[col[0]] += 1


for i in range(12):
    if times[i] != 0:
        print(f"En el mes {i+1} se ha facturado de media {months[i]/times[i]:.2f}€")
    else:
        print(f"En el mes {i+1} no se ha facturado nada")