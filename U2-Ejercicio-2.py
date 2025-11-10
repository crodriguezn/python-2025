"""
Crea una función que reciba un texto y devuelva:
- El número de cada vocal (a, e, i, o, u)
- Las 5 palabras más frecuentes
- El número de oraciones (separadas por . ! ?)
"""


import re
from collections import Counter

def analizador_texto_avanzado():
    texto = input("Ingresa un texto para analizar: ")
    
    # Contar vocales
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in texto.lower():
        if letra in vocales:
            vocales[letra] += 1
    
    # Palabras más frecuentes
    palabras = re.findall(r'\b\w+\b', texto.lower())
    contador_palabras = Counter(palabras)
    palabras_comunes = contador_palabras.most_common(5)
    
    # Número de oraciones
    oraciones = re.split(r'[.!?]+', texto)
    num_oraciones = len([o for o in oraciones if o.strip()])
    
    # Mostrar resultados
    print("\n📊 ANÁLISIS AVANZADO DEL TEXTO")
    print("\n🔤 Vocales encontradas:")
    for vocal, cantidad in vocales.items():
        print(f"  {vocal.upper()}: {cantidad}")
    
    print(f"\n📈 Total de vocales: {sum(vocales.values())}")
    
    print("\n🏆 5 palabras más frecuentes:")
    for palabra, frecuencia in palabras_comunes:
        print(f"  '{palabra}': {frecuencia} veces")
    
    print(f"\n📝 Número de oraciones: {num_oraciones}")

# Ejecutar
analizador_texto_avanzado()

