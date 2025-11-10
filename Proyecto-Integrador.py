"""
PROYECTO FINAL: SISTEMA DE GESTIÓN DE TIENDA ONLINE

Requisitos:
1. UNIDAD 1: Variables, estructuras de control, funciones básicas
2. UNIDAD 2: Estructuras de datos, manejo de archivos, excepciones
3. UNIDAD 3: Programación Orientada a Objetos, herencia, polimorfismo
4. UNIDAD 4: Decoradores, generadores, consumo de APIs

Descripción del proyecto:
Implementa un sistema completo de tienda online con las siguientes funcionalidades:
"""

# ===== ESTRUCTURA DEL PROYECTO =====

"""
PROYECTO FINAL: SISTEMA DE GESTIÓN DE TIENDA ONLINE
Integrando todas las unidades del curso
"""

import json
import requests
from datetime import datetime

# ===== UNIDAD 3: PROGRAMACIÓN ORIENTADA A OBJETOS =====

class Producto:
    def __init__(self, id, nombre, precio, categoria, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
    
    def aplicar_descuento(self, porcentaje):
        self.precio = self.precio * (1 - porcentaje/100)
        return self.precio
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} - Stock: {self.stock}"

class CarritoCompra:
    def __init__(self):
        self.items = []
    
    def agregar_producto(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.items.append((producto, cantidad))
            producto.stock -= cantidad
            return True
        return False
    
    def calcular_total(self):
        total = 0
        for producto, cantidad in self.items:
            total += producto.precio * cantidad
        return total
    
    def mostrar_carrito(self):
        if not self.items:
            print("🛒 El carrito está vacío")
            return
        
        print("\n=== TU CARRITO ===")
        for i, (producto, cantidad) in enumerate(self.items, 1):
            subtotal = producto.precio * cantidad
            print(f"{i}. {producto.nombre} x{cantidad} - ${subtotal:.2f}")
        print(f"TOTAL: ${self.calcular_total():.2f}")

class Cliente:
    def __init__(self, nombre, email, tipo="regular"):
        self.nombre = nombre
        self.email = email
        self.tipo = tipo
    
    def calcular_descuento(self, total):
        if self.tipo == "premium":
            return total * 0.10
        elif self.tipo == "vip":
            return total * 0.20
        return 0

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = self.cargar_productos()
        self.clientes = []
    
    def cargar_productos(self):
        return [
            Producto(1, "Laptop Gaming", 1200, "Tecnología", 10),
            Producto(2, "Smartphone", 800, "Tecnología", 15),
            Producto(3, "Auriculares Bluetooth", 150, "Audio", 20),
            Producto(4, "Tablet", 400, "Tecnología", 8),
            Producto(5, "Smart Watch", 300, "Wearables", 12)
        ]
    
    # UNIDAD 4: GENERADORES
    def buscar_producto(self, criterio, valor):
        for producto in self.productos:
            if criterio == "nombre" and valor.lower() in producto.nombre.lower():
                yield producto
            elif criterio == "categoria" and valor.lower() in producto.categoria.lower():
                yield producto
            elif criterio == "id" and str(producto.id) == str(valor):
                yield producto
    
    # UNIDAD 2: MANEJO DE ARCHIVOS
    def guardar_venta(self, cliente, carrito, total_final):
        venta = {
            "cliente": cliente.nombre,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "productos": [(p.nombre, cant) for p, cant in carrito.items],
            "total_final": total_final
        }
        
        try:
            with open("ventas.json", "a") as archivo:
                archivo.write(json.dumps(venta) + "\n")
        except Exception as e:
            print(f"Error guardando venta: {e}")
    
    # UNIDAD 4: DECORADORES
    def log_transaccion(func):
        def wrapper(self, *args, **kwargs):
            print(f"🔔 Ejecutando: {func.__name__}")
            resultado = func(self, *args, **kwargs)
            print(f"✅ Completado: {func.__name__}")
            return resultado
        return wrapper
    
    @log_transaccion
    def procesar_compra(self, cliente, carrito):
        total = carrito.calcular_total()
        descuento = cliente.calcular_descuento(total)
        total_final = total - descuento
        
        print(f"\n=== RESUMEN DE COMPRA ===")
        print(f"Cliente: {cliente.nombre}")
        print(f"Subtotal: ${total:.2f}")
        print(f"Descuento ({cliente.tipo}): ${descuento:.2f}")
        print(f"TOTAL FINAL: ${total_final:.2f}")
        
        self.guardar_venta(cliente, carrito, total_final)
        carrito.items = []
        
        return total_final

# UNIDAD 4: CONSUMO DE API
def obtener_tipo_cambio():
    try:
        # API pública para tipo de cambio
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD", timeout=5)
        if response.status_code == 200:
            datos = response.json()
            return datos['rates'].get('EUR', None)
    except:
        return None

# UNIDAD 1: PROGRAMA PRINCIPAL
def main():
    mi_tienda = Tienda("TecnoShop")
    cliente1 = Cliente("Ana García", "ana@email.com", "premium")
    carrito = CarritoCompra()
    
    # UNIDAD 4: API
    tipo_cambio = obtener_tipo_cambio()
    if tipo_cambio:
        print(f"💱 Tipo de cambio USD/EUR: {tipo_cambio}")
    
    while True:
        print("\n" + "="*50)
        print("🏪 BIENVENIDO A TECNOSHOP")
        print("="*50)
        print("1. Ver productos")
        print("2. Buscar producto")
        print("3. Agregar al carrito")
        print("4. Ver carrito")
        print("5. Finalizar compra")
        print("6. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            print("\n=== PRODUCTOS DISPONIBLES ===")
            for producto in mi_tienda.productos:
                print(producto)
                
        elif opcion == "2":
            criterio = input("Buscar por (nombre/categoria/id): ")
            valor = input("Valor a buscar: ")
            print("\n=== RESULTADOS ===")
            resultados = list(mi_tienda.buscar_producto(criterio, valor))
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("❌ No se encontraron productos")
                
        elif opcion == "3":
            try:
                id_producto = int(input("ID del producto: "))
                cantidad = int(input("Cantidad: "))
                
                producto_encontrado = None
                for producto in mi_tienda.buscar_producto("id", id_producto):
                    producto_encontrado = producto
                    break
                
                if producto_encontrado:
                    if carrito.agregar_producto(producto_encontrado, cantidad):
                        print(f"✅ {cantidad} {producto_encontrado.nombre} agregado(s)")
                    else:
                        print("❌ Stock insuficiente")
                else:
                    print("❌ Producto no encontrado")
                    
            except ValueError:
                print("❌ Error: Ingresa valores numéricos")
                
        elif opcion == "4":
            carrito.mostrar_carrito()
            
        elif opcion == "5":
            if carrito.items:
                mi_tienda.procesar_compra(cliente1, carrito)
            else:
                print("❌ El carrito está vacío")
                
        elif opcion == "6":
            print("¡Gracias por visitar TecnoShop! 👋")
            break
            
        else:
            print("❌ Opción no válida")

if __name__ == "__main__":
    main()