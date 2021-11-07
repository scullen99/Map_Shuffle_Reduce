# Python Map Shuffle Reduce
 
**Importante** tener los archivos .py en el mismo directorio que se hace la querie

### Ejecutar queries en terminal *windows*:

```
type compras.data | python mX.py | sort | python rX.py
Donde "x" será el número de la querie que queremos ejecutar
```

Ejemplo: 
```
type compras.data | python m1.py | sort | python r1.py
```


### Ejecutar queries en terminal *linux*:

```
cat compras.data | ./mX.py | sort | ./rX.py
Donde "x" será el número de la querie que queremos ejecutar
```

Ejemplo:
```
cat compras.data | ./m1.py | sort | ./r1.py
```

Para acceder a una querie con un directorio específico será de la manera:

Ejemplo:
```
Acceder a la querie 01:

type compras.data | python 0X/m1.py | sort | python 0X/r1.py
```
