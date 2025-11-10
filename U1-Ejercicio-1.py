"""
Crea un programa que solicite dos números y una operación (+, -, *, /)
y muestre el resultado. Incluye manejo de división por cero.
"""



def calculadora_basica():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        operacion = input("Ingresa la operación (+, -, *, /): ")
        
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 == 0:
                print("Error: No se puede dividir por cero")
                return
            resultado = num1 / num2
        else:
            print("Operación no válida")
            return
            
        print(f"Resultado: {num1} {operacion} {num2} = {resultado}")
        
    except ValueError:
        print("Error: Ingresa números válidos")

# Ejecutar
calculadora_basica()
