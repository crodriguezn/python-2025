
"""
Crea las clases:
- Libro (atributos: título, autor, ISBN, disponible)
- Usuario (atributos: nombre, ID, libros_prestados)
- Biblioteca (atributos: lista_libros, lista_usuarios)

Implementa métodos para:
- Prestar libro
- Devolver libro
- Buscar libro por título
- Mostrar libros disponibles
"""


class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
    
    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' por {self.autor} - {estado}"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id = id_usuario
        self.libros_prestados = []
    
    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id})"

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"📚 Libro '{libro.titulo}' agregado a la biblioteca")
    
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"👤 Usuario {usuario.nombre} registrado")
    
    def buscar_libro(self, titulo):
        encontrados = []
        for libro in self.libros:
            if titulo.lower() in libro.titulo.lower():
                encontrados.append(libro)
        return encontrados
    
    def prestar_libro(self, isbn, id_usuario):
        # Buscar libro
        libro = None
        for l in self.libros:
            if l.isbn == isbn and l.disponible:
                libro = l
                break
        
        # Buscar usuario
        usuario = None
        for u in self.usuarios:
            if u.id == id_usuario:
                usuario = u
                break
        
        if libro and usuario:
            libro.disponible = False
            usuario.libros_prestados.append(libro)
            print(f"📖 Libro '{libro.titulo}' prestado a {usuario.nombre}")
        else:
            print("❌ No se pudo realizar el préstamo")
    
    def devolver_libro(self, isbn, id_usuario):
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                for libro in usuario.libros_prestados[:]:
                    if libro.isbn == isbn:
                        libro.disponible = True
                        usuario.libros_prestados.remove(libro)
                        print(f"📗 Libro '{libro.titulo}' devuelto")
                        return
        print("❌ No se encontró el préstamo")
    
    def mostrar_libros_disponibles(self):
        disponibles = [libro for libro in self.libros if libro.disponible]
        if disponibles:
            print("\n📚 LIBROS DISPONIBLES:")
            for libro in disponibles:
                print(f"  - {libro}")
        else:
            print("📚 No hay libros disponibles")

# Ejemplo de uso
def demo_biblioteca():
    # Crear biblioteca
    biblio = Biblioteca()
    
    # Agregar libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "001")
    libro2 = Libro("1984", "George Orwell", "002")
    libro3 = Libro("El Quijote", "Miguel de Cervantes", "003")
    
    biblio.agregar_libro(libro1)
    biblio.agregar_libro(libro2)
    biblio.agregar_libro(libro3)
    
    # Registrar usuarios
    usuario1 = Usuario("Ana García", "U001")
    usuario2 = Usuario("Carlos López", "U002")
    
    biblio.registrar_usuario(usuario1)
    biblio.registrar_usuario(usuario2)
    
    # Operaciones
    biblio.mostrar_libros_disponibles()
    biblio.prestar_libro("001", "U001")
    biblio.mostrar_libros_disponibles()
    biblio.devolver_libro("001", "U001")
    biblio.mostrar_libros_disponibles()

# Ejecutar
demo_biblioteca()