
"""
Crea una clase base Figura con método area() y perimetro().
Luego crea clases hijas:
- Circulo
- Rectangulo  
- Triangulo
Cada una debe implementar los métodos de la clase base.
"""


import math

class Figura:
    def area(self):
        raise NotImplementedError("Método area() debe ser implementado")
    
    def perimetro(self):
        raise NotImplementedError("Método perimetro() debe ser implementado")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def __str__(self):
        return f"Círculo (radio: {self.radio})"

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def __str__(self):
        return f"Rectángulo ({self.base}x{self.altura})"

class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def __str__(self):
        return f"Triángulo (base: {self.base}, altura: {self.altura})"

# Demo del sistema
def demo_figuras():
    figuras = [
        Circulo(5),
        Rectangulo(4, 6),
        Triangulo(4, 3, 3, 4, 5)
    ]
    
    print("📐 CÁLCULO DE ÁREAS Y PERÍMETROS\n")
    
    for figura in figuras:
        print(f"{figura}")
        print(f"  Área: {figura.area():.2f}")
        print(f"  Perímetro: {figura.perimetro():.2f}")
        print()

# Ejecutar
demo_figuras()