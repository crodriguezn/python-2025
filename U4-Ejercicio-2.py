"""
Crea generadores para:
- Secuencia Fibonacci
- Números primos
- Patrón personalizado (ej: n, n*2, n*3, ...)
"""


def generador_fibonacci(limite):
    """Generador de la secuencia Fibonacci hasta el límite"""
    a, b = 0, 1
    while a <= limite:
        yield a
        a, b = b, a + b

def generador_primos(limite):
    """Generador de números primos hasta el límite"""
    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for num in range(2, limite + 1):
        if es_primo(num):
            yield num

def generador_patron(n, multiplicador=2):
    """Generador de patrón personalizado: n, n*multiplicador, n*multiplicador^2, ..."""
    valor = n
    while True:
        yield valor
        valor *= multiplicador

# Probar los generadores
print("🔢 PROBANDO GENERADORES DE SECUENCIAS\n")

print("1. Secuencia Fibonacci (hasta 100):")
for num in generador_fibonacci(100):
    print(num, end=" ")
print("\n")

print("2. Números primos (hasta 50):")
primos = list(generador_primos(50))
print(primos)
print()

print("3. Patrón personalizado (5, 10, 20, 40, ...):")
patron = generador_patron(5)
for _ in range(6):
    print(next(patron), end=" ")
print("\n")

print("4. Usando generador en comprensión de lista:")
fib_hasta_50 = list(generador_fibonacci(50))
print(f"Fibonacci hasta 50: {fib_hasta_50}")