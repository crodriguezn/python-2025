"""
Crea un decorador que mida el tiempo de ejecución de una función.
Debe mostrar cuántos segundos tardó en ejecutarse.
"""



import time
from functools import wraps

def medir_tiempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print(f"⏱️ La función '{func.__name__}' tardó {tiempo_ejecucion:.4f} segundos")
        return resultado
    return wrapper

# Ejemplos de uso
@medir_tiempo
def funcion_rapida():
    return sum(range(1000000))

@medir_tiempo
def funcion_lenta():
    time.sleep(2)
    return "Listo!"

@medir_tiempo
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Probar los decoradores
print("🔧 PROBANDO DECORADOR DE TIEMPO\n")
funcion_rapida()
funcion_lenta()
print(f"Factorial de 10: {factorial(10)}")