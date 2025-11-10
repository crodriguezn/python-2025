"""
Genera un número aleatorio entre 1 y 100. El usuario debe adivinarlo.
El programa debe dar pistas "mayor" o "menor" hasta que acierte.
Muestra cuántos intentos necesitó.
"""


import random

def adivina_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    
    print("🎯 Adivina el número entre 1 y 100")
    
    while True:
        try:
            intento = int(input("Tu intento: "))
            intentos += 1
            
            if intento < numero_secreto:
                print("⬆️ Mayor...")
            elif intento > numero_secreto:
                print("⬇️ Menor...")
            else:
                print(f"🎉 ¡Correcto! Adivinaste en {intentos} intentos")
                break
                
        except ValueError:
            print("Por favor ingresa un número válido")

# Ejecutar
adivina_numero()