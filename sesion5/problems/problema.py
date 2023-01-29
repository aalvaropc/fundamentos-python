# Crear un sistema de gestión de biblioteca que permita a los usuarios prestar y devolver libros.
class Libro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.disponible = True

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_num_paginas(self):
        return self.num_paginas

    def is_disponible(self):
        return self.disponible

    def set_disponible(self, disponible):
        self.disponible = disponible

class Usuario:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def get_nombre(self):
        return self.nombre

    def get_direccion(self):
        return self.direccion

    def get_telefono(self):
        return self.telefono

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def prestamo_libro(self, libro, usuario):
        if libro.is_disponible():
            libro.set_disponible(False)
            usuario.libro_prestado = libro
            print(f'El libro {libro.get_titulo()} ha sido prestado a {usuario.get_nombre()}')
        else:
            print(f'El libro {libro.get_titulo()} no está disponible')

    def devolver_libro(self, libro, usuario):
        if usuario.libro_prestado == libro:
            libro.set_disponible(True)
            usuario.libro_prestado = None
            print(f'El libro {libro.get_titulo()} ha sido devuelto por {usuario.get_nombre()}')
        else:
            print(f'{usuario.get_nombre()} no tiene prestado ese libro')

# Crea una instancia de Biblioteca
biblioteca = Biblioteca()

# Crea libros y usuarios
libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", 432)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 345)
usuario1 = Usuario("Juan Pérez", "Calle Falsa 123", "555-555-5555")
usuario2 = Usuario("Maria García", "Calle Real 456", "555-555-5556")

biblioteca.libros.append(libro1)
biblioteca.libros.append(libro2)
biblioteca.usuarios.append(usuario1)
biblioteca.usuarios.append(usuario2)

biblioteca.prestamo_libro(libro1, usuario1) # El libro El señor de los anillos ha sido prestado a Juan Pérez
biblioteca.prestamo_libro(libro1, usuario2) # El libro El señor de los anillos no está disponible
biblioteca.devolver_libro(libro1, usuario1) # El libro El señor de los anillos ha sido devuelto por Juan Pérez
biblioteca.prestamo_libro(libro1, usuario2) # El libro El señor de los anillos ha sido prestado a Maria García
biblioteca.devolver_libro(libro2, usuario2) # Maria Garcia no tiene prestado ese libro