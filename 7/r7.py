#!/usr/bin/python3

# 7. Tipos de envíos realizados por un proveedor en un mes determinado de un año
# determinado.
import sys

t = set()

for item in sys.stdin:
    item = item.strip()
    t.add(item)

print(f"El proveedor 'Electronica Chispas' ha utilizado los metodos de envio {t} en el 11/2003")