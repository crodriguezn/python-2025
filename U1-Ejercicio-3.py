"""
Solicita una frase al usuario y muestra:
- Número total de caracteres
- Número de palabras
- Frase en mayúsculas
- Frase en minúsculas
"""


def analizar_texto():
    texto = input("Ingresa una frase: ")
    
    # Número de caracteres
    num_caracteres = len(texto)
    
    # Número de palabras
    palabras = texto.split()
    num_palabras = len(palabras)
    
    # Texto en mayúsculas y minúsculas
    mayusculas = texto.upper()
    minusculas = texto.lower()
    
    print(f"\n📊 Análisis del texto:")
    print(f"Caracteres totales: {num_caracteres}")
    print(f"Número de palabras: {num_palabras}")
    print(f"En mayúsculas: {mayusculas}")
    print(f"En minúsculas: {minusculas}")

# Ejecutar
analizar_texto()