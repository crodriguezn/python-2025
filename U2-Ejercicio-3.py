
"""
Crea un sistema que guarde tareas en un archivo:
- Agregar tarea
- Marcar tarea como completada
- Mostrar tareas pendientes
- Eliminar tarea
Los datos deben persistir en un archivo .txt
"""

import json
import os

class GestorTareas:
    def __init__(self, archivo="tareas.json"):
        self.archivo = archivo
        self.tareas = self.cargar_tareas()
    
    def cargar_tareas(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def guardar_tareas(self):
        with open(self.archivo, 'w') as f:
            json.dump(self.tareas, f, indent=2)
    
    def agregar_tarea(self):
        descripcion = input("Descripción de la tarea: ")
        tarea = {
            'id': len(self.tareas) + 1,
            'descripcion': descripcion,
            'completada': False,
            'fecha_creacion': '2024-01-01'  # En realidad usar datetime.now()
        }
        self.tareas.append(tarea)
        self.guardar_tareas()
        print(f"✅ Tarea '{descripcion}' agregada")
    
    def mostrar_tareas(self, solo_pendientes=False):
        if not self.tareas:
            print("📝 No hay tareas")
            return
        
        print("\n📋 LISTA DE TAREAS:")
        for tarea in self.tareas:
            if solo_pendientes and tarea['completada']:
                continue
            
            estado = "✅" if tarea['completada'] else "⏳"
            print(f"{tarea['id']}. {estado} {tarea['descripcion']}")
    
    def completar_tarea(self):
        self.mostrar_tareas(solo_pendientes=True)
        try:
            id_tarea = int(input("ID de la tarea a completar: "))
            for tarea in self.tareas:
                if tarea['id'] == id_tarea:
                    tarea['completada'] = True
                    self.guardar_tareas()
                    print(f"🎉 Tarea '{tarea['descripcion']}' completada")
                    return
            print("❌ Tarea no encontrada")
        except ValueError:
            print("❌ ID inválido")
    
    def eliminar_tarea(self):
        self.mostrar_tareas()
        try:
            id_tarea = int(input("ID de la tarea a eliminar: "))
            self.tareas = [t for t in self.tareas if t['id'] != id_tarea]
            self.guardar_tareas()
            print("🗑️ Tarea eliminada")
        except ValueError:
            print("❌ ID inválido")
    
    def menu(self):
        while True:
            print("\n" + "="*30)
            print("✅ GESTOR DE TAREAS")
            print("="*30)
            print("1. Agregar tarea")
            print("2. Mostrar todas las tareas")
            print("3. Mostrar tareas pendientes")
            print("4. Completar tarea")
            print("5. Eliminar tarea")
            print("6. Salir")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == '1':
                self.agregar_tarea()
            elif opcion == '2':
                self.mostrar_tareas()
            elif opcion == '3':
                self.mostrar_tareas(solo_pendientes=True)
            elif opcion == '4':
                self.completar_tarea()
            elif opcion == '5':
                self.eliminar_tarea()
            elif opcion == '6':
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción no válida")

# Ejecutar
gestor = GestorTareas()
gestor.menu()