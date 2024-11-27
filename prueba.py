import mysql.connector
from mysql.connector import Error

class Menu:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.conectar_db()

    def conectar_db(self):
        """Método para conectar a la base de datos MySQL"""
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root', # Cambia esto por tu contraseña
                database='netflix1'  # Nombre de tu base de datos
            )
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def mostrar_menu(self):
        """Método para mostrar el menú de opciones"""
        while True:
            print("\n------- NETFLIX -------")
            print("1. Crear plan")
            print("2. Leer plan")
            print("3. Crear Usuario")
            print("4. Leer Usuario")
            print("5. Crear Perfil")
            print("6. Leer Perfil")
            print("7. Crear Categoria")
            print("8. Leer Categoria")
            print("9. Crear Contenido")
            print("10. Leer Contenido")
            print("11. Actualizar Contenido")
            print("12. Actualizar UsuarioPerfil")
            print("13. Eliminar Contenido")
            print("14. Eliminar Usuario")
            print("15. Salir")
            opcion = input("Elige una opción: ")
            self.ejecutar_opcion(opcion)

    def ejecutar_opcion(self, opcion):
        """Método que ejecuta la opción seleccionada"""
        if opcion == "1":
            self.crear_plan()
        elif opcion == "2":
            self.leer_plan()
        elif opcion == "3":
            self.crear_usuario()
        elif opcion == "4":
            self.leer_usuario()
        elif opcion == "5":
            self.crear_perfil()
        elif opcion == "6":
            self.leer_perfil()
        elif opcion == "7":
            self.crear_categoria()
        elif opcion == "8":
            self.leer_categoria()
        elif opcion == "9":
            self.crear_contenido()
        elif opcion == "10":
            self.leer_contenido()
        elif opcion == "11":
            self.actualizar_contenido()
        elif opcion == "12":
            self.actualizar_usuario_perfil()
        elif opcion == "13":
            self.eliminar_contenido()
        elif opcion == "14":
            self.eliminar_usuario()
        elif opcion == "15":
            self.salir()
        else:
            print("Opción no válida. Intenta nuevamente.")

    # Métodos para las opciones del menú:

    def crear_plan(self):
        nombre_plan = input("Ingrese el nombre del plan: ")
        descripcion = input("Ingrese la descripción del plan: ")
        precio = input("Ingrese el precio del plan: ")
        try:
            self.cursor.execute(
                "INSERT INTO Plan (TipoPlan, Caracteristicas, Precio) VALUES (%s, %s, %s)",
                (nombre_plan, descripcion, precio)
            )
            self.conn.commit()
            print("Plan creado exitosamente.")
        except Error as e:
            print(f"Error al crear plan: {e}")

    def leer_plan(self):
        self.cursor.execute("SELECT * FROM Plan")
        planes = self.cursor.fetchall()
        for plan in planes:
            print(plan)

    def crear_usuario(self):
        idPlan = input ("Ingrese el plan:")
        nombre_usuario = input("Ingrese el correo del usuario: ")
        email = input("Ingrese su contrasena: ")
        try:
            self.cursor.execute(
                "INSERT INTO Usuario (IdPlan, Correo, Contrasena) VALUES (%s, %s, %s)",
                (idPlan, nombre_usuario, email)
            )
            self.conn.commit()
            print("Usuario creado exitosamente.")
        except Error as e:
            print(f"Error al crear usuario: {e}")

    def leer_usuario(self):
        self.cursor.execute("SELECT * FROM Usuario")
        usuarios = self.cursor.fetchall()
        for usuario in usuarios:
            print(usuario)

    def crear_perfil(self):
        id_usuario = input("Ingrese el ID del usuario: ")
        nombre_perfil = input("Ingrese el nombre del perfil: ")
        apellidoP_perfil = input("Ingrese el apellido Paterno: ")
        apellidoM_perfil = input("Ingrese el apellido Materno: ")
        fecha_nacimiento = input("fecha de nacimiento (aaaa/mm/dd)")
        telefono = input("Telefono:")
        try:
            self.cursor.execute(
                "INSERT INTO Perfil (IdUsuario,Nombre,ApellidoPaterno,ApellidoMaterno,FechaNacimiento,Telefono) VALUES (%s, %s, %s, %s, %s, %s)",
                (id_usuario, nombre_perfil, apellidoP_perfil, apellidoM_perfil, fecha_nacimiento, telefono)
            )
            self.conn.commit()
            print("Perfil creado exitosamente.")
        except Error as e:
            print(f"Error al crear perfil: {e}")

    def leer_perfil(self):
        self.cursor.execute("SELECT * FROM Perfil")
        perfiles = self.cursor.fetchall()
        for perfil in perfiles:
            print(perfil)

    def crear_categoria(self):
        nombre_categoria = input("Ingrese el nombre de la categoría: ")
        try:
            self.cursor.execute(
                "INSERT INTO Categoria (Nombre) VALUES (%s)",
                (nombre_categoria)
            )
            self.conn.commit()
            print("Categoría creada exitosamente.")
        except Error as e:
            print(f"Error al crear categoría: {e}")

    def leer_categoria(self):
        self.cursor.execute("SELECT * FROM Categoria")
        categorias = self.cursor.fetchall()
        for categoria in categorias:
            print(categoria)

    def crear_contenido(self):
        id_categoria = input("Ingrese el ID de la categoría: ")
        nombre_titulo = input("Ingrese el Titulo: ")
        descripcion = input("Ingrese la Descripcion: ")
        nombre_categoria = input("Ingrese ek nombre de la categoria: ")
        anio = input("Anio de publicacion: ")
        try:
            self.cursor.execute(
                "INSERT INTO Contenido (IdCategoria,Titulo,Descripcion,NombreCategoria,Anio) VALUES (%s, %s, %s, %s, %s)",
                (id_categoria, nombre_titulo, descripcion, nombre_categoria, anio)
            )
            self.conn.commit()
            print("Contenido creado exitosamente.")
        except Error as e:
            print(f"Error al crear contenido: {e}")

    def leer_contenido(self):
        self.cursor.execute("SELECT * FROM Contenido")
        contenidos = self.cursor.fetchall()
        for contenido in contenidos:
            print(contenido)

    def actualizar_contenido(self):
        id_contenido = input("Ingrese el ID del contenido a actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo Titulo del contenido: ")
        nueva_descripcion = input("Ingrese la nueva descripción del contenido: ")
        nueva_categoria = input("Ingrese la nueva categoría del contenido: ")
        try:
            self.cursor.execute(
                "UPDATE Contenido SET Titulo = %s, Descripcion = %s, NombreCategoria = %s WHERE IdContenido = %s",
                (nuevo_nombre, nueva_descripcion, nueva_categoria, id_contenido)
            )
            self.conn.commit()
            print("Contenido actualizado exitosamente.")
        except Error as e:
            print(f"Error al actualizar contenido: {e}")

    def actualizar_usuario_perfil(self):
        id_usuario = input("Ingrese el ID del usuario a actualizar: ")
        nuevo_correo = input("Ingrese el nuevo Correo del usuario: ")
        nuevo_nombre = input("Ingrese el nuevo Nombre del usuario: ")
        nuevo_telefono = input("Ingrese el nuevo Teléfono del usuario: ")
        try:
            self.cursor.execute(
                "UPDATE Usuario SET Correo = %s, Nombre = %s, Telefono = %s WHERE IdUsuario = %s",
                (nuevo_correo, nuevo_nombre, nuevo_telefono, id_usuario)
            )
            self.conn.commit()
            print("Usuario actualizado exitosamente.")
        except Error as e:
            print(f"Error al actualizar usuario: {e}")

    def eliminar_contenido(self):
        id_contenido = input("Ingrese el ID del contenido a eliminar: ")
        try:
            # Verificar si el contenido existe
            self.cursor.execute("SELECT IdContenido FROM Contenido WHERE IdContenido = %s", (id_contenido,))
            resultado = self.cursor.fetchone()
            if not resultado:
                print(f"El contenido con ID {id_contenido} no existe.")
                return

            # Eliminar las calificaciones asociadas con el contenido
            self.cursor.execute("DELETE FROM Calificacion WHERE IdContenido = %s", (id_contenido,))
            self.conn.commit()

            # Ahora eliminar el contenido
            self.cursor.execute("DELETE FROM Contenido WHERE IdContenido = %s", (id_contenido,))
            self.conn.commit()

            print("Contenido y sus calificaciones eliminados exitosamente.")
        except Error as e:
            print(f"Error al eliminar contenido: {e}")

    def eliminar_usuario(self):
        id_usuario = input("Ingrese el ID del perfil de usuario a eliminar: ")
        try:
            self.cursor.execute("DELETE FROM Perfil WHERE IdPerfil = %s", (id_usuario,))
            self.conn.commit()
            print("Usuario eliminado exitosamente.")
        except Error as e:
            print(f"Error al eliminar usuario: {e}")

    def salir(self):
        """Cierra la conexión con la base de datos y termina el programa"""
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexión cerrada")
        print("Saliendo...")
        exit()


# Crear una instancia del menú y mostrarlo
if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()
