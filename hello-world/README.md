# Hello World

Ejemplo basico de Hello World en Express JS.

## Paso a paso

Empezamos por nuestra biblioteca de Flask.
```python
from flask import Flask
```
Creamos una variable donde inicializaremos nuestra biblioteca en una variable que llamaremos app.
```python
app = Flask(__name__)
```
Pasemos a crear una ruta inicial en nuestro servidor que responda al verbo GET y nos responda con `Hello World`.
```python
@app.route('/')
def index():
    return 'Hello World'
```
Hagamos que nuestra aplicacion ahora escuche en el puerto `3000` de nuestro computador.
```python
app.run(port=3000)
```
Y listo, terminaste tu primer API REST en Flask.