
"""
Crea un sistema de vehículos con herencia:
- Vehiculo (marca, modelo, año)
- Coche (numero_puertas)
- Motocicleta (cilindrada)
- Camion (capacidad_carga)

Implementa métodos específicos para cada tipo.
"""


class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad = 0
    
    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"🚗 {self.marca} {self.modelo} acelerando... Velocidad: {self.velocidad} km/h")
    
    def frenar(self, decremento):
        self.velocidad = max(0, self.velocidad - decremento)
        print(f"🛑 {self.marca} {self.modelo} frenando... Velocidad: {self.velocidad} km/h")
    
    def info(self):
        return f"{self.marca} {self.modelo} ({self.año})"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
    
    def abrir_maletero(self):
        print(f"📦 Maletero del {self.marca} {self.modelo} abierto")
    
    def info(self):
        return f"{super().info()} - {self.numero_puertas} puertas"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada
    
    def hacer_caballito(self):
        print(f"🏍️ {self.marca} {self.modelo} haciendo caballito! 🎯")
    
    def info(self):
        return f"{super().info()} - {self.cilindrada}cc"

class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.capacidad_carga = capacidad_carga
        self.carga_actual = 0
    
    def cargar(self, peso):
        if self.carga_actual + peso <= self.capacidad_carga:
            self.carga_actual += peso
            print(f"📦 Cargando {peso}kg. Carga actual: {self.carga_actual}kg")
        else:
            print("❌ Excede la capacidad máxima")
    
    def descargar(self, peso):
        self.carga_actual = max(0, self.carga_actual - peso)
        print(f"📤 Descargando {peso}kg. Carga actual: {self.carga_actual}kg")
    
    def info(self):
        return f"{super().info()} - Capacidad: {self.capacidad_carga}kg"

# Demo del sistema
def demo_vehiculos():
    vehiculos = [
        Coche("Toyota", "Corolla", 2022, 4),
        Motocicleta("Yamaha", "MT-07", 2023, 689),
        Camion("Volvo", "FH16", 2020, 25000)
    ]
    
    print("🚗 SIMULADOR DE VEHÍCULOS\n")
    
    for vehiculo in vehiculos:
        print(f"=== {vehiculo.info()} ===")
        vehiculo.acelerar(30)
        
        # Acciones específicas
        if isinstance(vehiculo, Coche):
            vehiculo.abrir_maletero()
        elif isinstance(vehiculo, Motocicleta):
            vehiculo.hacer_caballito()
        elif isinstance(vehiculo, Camion):
            vehiculo.cargar(5000)
        
        vehiculo.frenar(15)
        print()

# Ejecutar
demo_vehiculos()