#!/usr/bin/python3

# 10. Balance de facturación para una ciudad determinada. Ventas cuyo envío se realiza desde una
# ciudad menos las ventas enviadas a dicha ciudad.
import sys

balance = 0

for item in sys.stdin:
    item = float(item.strip())

    balance += item

print(f"El balance total de Ceuta es: {balance:.2f}€")