"""
Usa la API de OpenWeatherMap (o similar) para:
- Obtener el clima actual de una ciudad
- Mostrar temperatura, humedad, descripción
- Guardar el historial en un archivo JSON
"""

import requests
import json
from datetime import datetime

class ClienteClima:
    def __init__(self, archivo_historial="historial_clima.json"):
        self.archivo_historial = archivo_historial
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        # NOTA: En producción, usar una API key real
        self.api_key = "tu_api_key_aqui"  # Necesitas registrarte en openweathermap.org
    
    def obtener_clima(self, ciudad):
        """Obtiene el clima actual de una ciudad"""
        try:
            # Para demo, usamos datos simulados
            if ciudad.lower() == "quito":
                datos_simulados = {
                    "name": "Quito",
                    "main": {"temp": 285.15, "humidity": 65},  # 12°C
                    "weather": [{"description": "cielo claro"}],
                    "cod": 200
                }
                return datos_simulados
            else:
                # Código real para usar la API (necesita API key)
                params = {
                    'q': ciudad,
                    'appid': self.api_key,
                    'units': 'metric',
                    'lang': 'es'
                }
                respuesta = requests.get(self.base_url, params=params)
                return respuesta.json()
                
        except Exception as e:
            print(f"Error al obtener datos: {e}")
            return None
    
    def mostrar_clima(self, ciudad):
        """Muestra la información del clima de forma legible"""
        datos = self.obtener_clima(ciudad)
        
        if datos and datos.get('cod') == 200:
            temperatura = datos['main']['temp']
            humedad = datos['main']['humidity']
            descripcion = datos['weather'][0]['description']
            nombre_ciudad = datos['name']
            
            print(f"\n🌤️ CLIMA EN {nombre_ciudad.upper()}")
            print(f"📍 Ciudad: {nombre_ciudad}")
            print(f"🌡️ Temperatura: {temperatura}°C")
            print(f"💧 Humedad: {humedad}%")
            print(f"☁️ Condición: {descripcion.title()}")
            
            # Guardar en historial
            self.guardar_historial(ciudad, datos)
            
        else:
            print(f"❌ No se pudo obtener el clima para {ciudad}")
            print("💡 Consejo: Verifica el nombre de la ciudad o tu conexión a internet")
    
    def guardar_historial(self, ciudad, datos):
        """Guarda la consulta en el archivo de historial"""
        registro = {
            'ciudad': ciudad,
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'temperatura': datos['main']['temp'],
            'humedad': datos['main']['humidity'],
            'descripcion': datos['weather'][0]['description']
        }
        
        try:
            # Cargar historial existente
            try:
                with open(self.archivo_historial, 'r') as f:
                    historial = json.load(f)
            except FileNotFoundError:
                historial = []
            
            # Agregar nuevo registro
            historial.append(registro)
            
            # Guardar
            with open(self.archivo_historial, 'w') as f:
                json.dump(historial, f, indent=2, ensure_ascii=False)
                
            print("📝 Registro guardado en historial")
            
        except Exception as e:
            print(f"Error guardando historial: {e}")
    
    def mostrar_historial(self):
        """Muestra el historial de consultas"""
        try:
            with open(self.archivo_historial, 'r') as f:
                historial = json.load(f)
            
            print("\n📊 HISTORIAL DE CONSULTAS")
            print("=" * 50)
            
            for registro in historial[-5:]:  # Últimas 5 consultas
                print(f"🏙️ Ciudad: {registro['ciudad']}")
                print(f"📅 Fecha: {registro['fecha']}")
                print(f"🌡️ Temp: {registro['temperatura']}°C")
                print(f"💧 Humedad: {registro['humedad']}%")
                print(f"☁️ Clima: {registro['descripcion']}")
                print("-" * 30)
                
        except FileNotFoundError:
            print("📂 No hay historial de consultas")
        except Exception as e:
            print(f"Error leyendo historial: {e}")
    
    def menu(self):
        """Menú interactivo del cliente de clima"""
        while True:
            print("\n" + "="*40)
            print("🌤️ CLIENTE DE API DEL CLIMA")
            print("="*40)
            print("1. Consultar clima de una ciudad")
            print("2. Ver historial")
            print("3. Salir")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == '1':
                ciudad = input("Ingresa el nombre de la ciudad: ")
                self.mostrar_clima(ciudad)
            elif opcion == '2':
                self.mostrar_historial()
            elif opcion == '3':
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción no válida")

# Ejecutar el cliente de clima
cliente = ClienteClima()

# Para probar sin menú:
print("🌤️ DEMO CLIENTE DE CLIMA")
cliente.mostrar_clima("quito")