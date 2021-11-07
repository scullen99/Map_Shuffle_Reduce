#!/usr/bin/python3

# 3.Incremento por año (en porcentaje) de la facturación de un proveedor.
import sys

years = []
values = []

for item in sys.stdin:
    col = item.split(",")
    year = int(col[0])
    value = float(col[1])

    if year in years:
        i = years.index(year)
        values[i] += value
    else:
        years.append(year)
        values.append(value)

year_value = zip(years, values)
year_value = sorted(year_value, key=lambda x: x[0])

for i in range(1, len(year_value)):
    print(f"Del año {year_value[i-1][0]} al año {year_value[i][0]}, la facturacion ha aumentado un {year_value[i][1]/year_value[i-1][1]*100-100:.2f}%")