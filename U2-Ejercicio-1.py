
"""
Crea un programa que permita:
1. Agregar contactos (nombre, teléfono, email)
2. Buscar contactos por nombre
3. Mostrar todos los contactos
4. Eliminar contactos
Usa diccionarios y listas para almacenar los datos.
"""


class GestorContactos:
    def __init__(self):
        self.contactos = []
    
    def agregar_contacto(self):
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        
        contacto = {
            'nombre': nombre,
            'telefono': telefono,
            'email': email
        }
        
        self.contactos.append(contacto)
        print(f"✅ Contacto {nombre} agregado")
    
    def buscar_contacto(self):
        nombre_buscar = input("Nombre a buscar: ")
        encontrados = []
        
        for contacto in self.contactos:
            if nombre_buscar.lower() in contacto['nombre'].lower():
                encontrados.append(contacto)
        
        if encontrados:
            print("\n🔍 Contactos encontrados:")
            for contacto in encontrados:
                print(f"Nombre: {contacto['nombre']}")
                print(f"Teléfono: {contacto['telefono']}")
                print(f"Email: {contacto['email']}")
                print("---")
        else:
            print("❌ No se encontraron contactos")
    
    def mostrar_contactos(self):
        if not self.contactos:
            print("📞 No hay contactos guardados")
            return
        
        print("\n📋 Lista de contactos:")
        for i, contacto in enumerate(self.contactos, 1):
            print(f"{i}. {contacto['nombre']} - {contacto['telefono']}")
    
    def eliminar_contacto(self):
        self.mostrar_contactos()
        try:
            indice = int(input("Número del contacto a eliminar: ")) - 1
            if 0 <= indice < len(self.contactos):
                contacto_eliminado = self.contactos.pop(indice)
                print(f"🗑️ Contacto {contacto_eliminado['nombre']} eliminado")
            else:
                print("❌ Número inválido")
        except ValueError:
            print("❌ Ingresa un número válido")
    
    def menu(self):
        while True:
            print("\n" + "="*30)
            print("📒 GESTOR DE CONTACTOS")
            print("="*30)
            print("1. Agregar contacto")
            print("2. Buscar contacto")
            print("3. Mostrar contactos")
            print("4. Eliminar contacto")
            print("5. Salir")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == '1':
                self.agregar_contacto()
            elif opcion == '2':
                self.buscar_contacto()
            elif opcion == '3':
                self.mostrar_contactos()
            elif opcion == '4':
                self.eliminar_contacto()
            elif opcion == '5':
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción no válida")

# Ejecutar
gestor = GestorContactos()
gestor.menu()