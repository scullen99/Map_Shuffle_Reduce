#!/usr/bin/python3

# 4. Top tres proveedores que más gastan en envíos en un año determinado y coste total de los
# envíos para cada proveedor (Coste de envíos: Tipo 1: 10€, Tipo 2: 5€, Tipo 3: 3€.)

import sys

costes = {'1': 10, '2': 5, '3': 3}
proveedor = ""
coste = 0
top3_proveedores = [0] * 3
top3_costes = [0] * 3

for item in sys.stdin:
    data = item.strip().split(',')

    if data[0] != proveedor:
        m = min(top3_costes)
        if m < coste:
            i = top3_costes.index(m)
            top3_proveedores[i] = data[0]
            top3_costes[i] = coste
        proveedor = data[0]
        coste = 0

    coste += costes[data[1]]

top3 = sorted(zip(top3_proveedores, top3_costes), key=lambda x: x[1], reverse=True)[:3]

for p,c in top3:
    print(f"La empresa '{p}' ha gastado {c}€ en gastos de envio")