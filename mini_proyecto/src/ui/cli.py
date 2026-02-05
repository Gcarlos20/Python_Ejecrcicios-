"""
Interfaz CLI (Command Line Interface)
"""
from datetime import datetime
from src.service.libro_service import LibroService
from src.service.usuario_service import UsuarioService
from src.service.prestamo_service import PrestamoService


class BibliotecaCLI:
    """Interfaz de línea de comandos para la biblioteca"""
    
    def __init__(self, libro_service: LibroService, usuario_service: UsuarioService, 
                 prestamo_service: PrestamoService):
        self.libro_service = libro_service
        self.usuario_service = usuario_service
        self.prestamo_service = prestamo_service
    
    @staticmethod
    def limpiar_pantalla():
        """Limpia la pantalla"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def mostrar_titulo():
        """Muestra el título de la aplicación"""
        print("\n" + "="*60)
        print("📚 SISTEMA DE GESTIÓN DE BIBLIOTECA 📚".center(60))
        print("="*60 + "\n")
    
    @staticmethod
    def mostrar_menu_principal():
        """Muestra el menú principal"""
        print("\n┌─ MENÚ PRINCIPAL ─────────────────────────────────────┐")
        print("│                                                      │")
        print("│  1. 📖 Gestionar Libros                              │")
        print("│  2. 👤 Gestionar Usuarios                            │")
        print("│  3. 🔄 Gestionar Préstamos                           │")
        print("│  4. 📊 Ver Estadísticas                              │")
        print("│  5. 🚪 Salir                                         │")
        print("│                                                      │")
        print("└──────────────────────────────────────────────────────┘")
    
    @staticmethod
    def mostrar_menu_libros():
        """Muestra el menú de libros"""
        print("\n┌─ GESTIÓN DE LIBROS ──────────────────────────────────┐")
        print("│                                                      │")
        print("│  1. ➕ Agregar libro                                  │")
        print("│  2. 📋 Listar libros                                  │")
        print("│  3. 🔍 Buscar por título                             │")
        print("│  4. 🔍 Buscar por autor                              │")
        print("│  5. 🗑️  Eliminar libro                               │")
        print("│  6. ⬅️  Volver al menú principal                     │")
        print("│                                                      │")
        print("└──────────────────────────────────────────────────────┘")
    
    @staticmethod
    def mostrar_menu_usuarios():
        """Muestra el menú de usuarios"""
        print("\n┌─ GESTIÓN DE USUARIOS ────────────────────────────────┐")
        print("│                                                      │")
        print("│  1. ➕ Registrar usuario                              │")
        print("│  2. 📋 Listar usuarios                                │")
        print("│  3. ⬅️  Volver al menú principal                     │")
        print("│                                                      │")
        print("└──────────────────────────────────────────────────────┘")
    
    @staticmethod
    def mostrar_menu_prestamos():
        """Muestra el menú de préstamos"""
        print("\n┌─ GESTIÓN DE PRÉSTAMOS ───────────────────────────────┐")
        print("│                                                      │")
        print("│  1. 📤 Prestar libro                                  │")
        print("│  2. 📥 Devolver libro                                 │")
        print("│  3. 📋 Ver préstamos activos                          │")
        print("│  4. 📊 Historial de préstamos                         │")
        print("│  5. ⬅️  Volver al menú principal                     │")
        print("│                                                      │")
        print("└──────────────────────────────────────────────────────┘")
    
    def gestion_libros(self):
        """Submenú de gestión de libros"""
        while True:
            self.mostrar_menu_libros()
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == "1":
                self.agregar_libro()
            elif opcion == "2":
                self.listar_libros()
            elif opcion == "3":
                self.buscar_libro_titulo()
            elif opcion == "4":
                self.buscar_libro_autor()
            elif opcion == "5":
                self.eliminar_libro()
            elif opcion == "6":
                break
            else:
                print("❌ Opción inválida")
            
            input("\nPresione Enter para continuar...")
    
    def agregar_libro(self):
        """Agrega un nuevo libro"""
        print("\n➕ AGREGAR NUEVO LIBRO")
        print("-" * 50)
        
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        año = input("Año de publicación: ").strip()
        
        exito, mensaje, libro = self.libro_service.agregar_libro(titulo, autor, año)
        print(f"\n{mensaje}")
    
    def listar_libros(self):
        """Lista todos los libros"""
        libros = self.libro_service.listar_libros()
        
        if not libros:
            print("❌ No hay libros registrados")
            return
        
        print("\n📖 LISTA DE LIBROS")
        print("-" * 80)
        print(f"{'ID':<10} {'Título':<25} {'Autor':<20} {'Año':<6} {'Estado':<12}")
        print("-" * 80)
        
        for libro in libros:
            estado_icono = "✅ Disponible" if libro.estado == "disponible" else "🔴 Prestado"
            print(f"{libro.id:<10} {libro.titulo:<25} {libro.autor:<20} {libro.año:<6} {estado_icono:<12}")
        
        print(f"\nTotal: {len(libros)} libro(s)")
    
    def buscar_libro_titulo(self):
        """Busca libros por título"""
        titulo = input("\n🔍 Ingrese el título a buscar: ").strip()
        exito, mensaje, resultados = self.libro_service.buscar_por_titulo(titulo)
        
        print(f"\n{mensaje}")
        
        if exito and resultados:
            print("-" * 80)
            print(f"{'ID':<10} {'Título':<25} {'Autor':<20} {'Año':<6} {'Estado':<12}")
            print("-" * 80)
            
            for libro in resultados:
                estado_icono = "✅ Disponible" if libro.estado == "disponible" else "🔴 Prestado"
                print(f"{libro.id:<10} {libro.titulo:<25} {libro.autor:<20} {libro.año:<6} {estado_icono:<12}")
    
    def buscar_libro_autor(self):
        """Busca libros por autor"""
        autor = input("\n🔍 Ingrese el nombre del autor: ").strip()
        exito, mensaje, resultados = self.libro_service.buscar_por_autor(autor)
        
        print(f"\n{mensaje}")
        
        if exito and resultados:
            print("-" * 80)
            print(f"{'ID':<10} {'Título':<25} {'Autor':<20} {'Año':<6} {'Estado':<12}")
            print("-" * 80)
            
            for libro in resultados:
                estado_icono = "✅ Disponible" if libro.estado == "disponible" else "🔴 Prestado"
                print(f"{libro.id:<10} {libro.titulo:<25} {libro.autor:<20} {libro.año:<6} {estado_icono:<12}")
    
    def eliminar_libro(self):
        """Elimina un libro"""
        libro_id = input("\n🗑️  Ingrese el ID del libro a eliminar: ").strip()
        exito, mensaje = self.libro_service.eliminar_libro(libro_id)
        print(f"\n{mensaje}")
    
    def gestion_usuarios(self):
        """Submenú de gestión de usuarios"""
        while True:
            self.mostrar_menu_usuarios()
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.listar_usuarios()
            elif opcion == "3":
                break
            else:
                print("❌ Opción inválida")
            
            input("\nPresione Enter para continuar...")
    
    def registrar_usuario(self):
        """Registra un nuevo usuario"""
        print("\n➕ REGISTRAR NUEVO USUARIO")
        print("-" * 50)
        
        nombre = input("Nombre: ").strip()
        email = input("Email: ").strip()
        
        exito, mensaje, usuario = self.usuario_service.registrar_usuario(nombre, email)
        print(f"\n{mensaje}")
    
    def listar_usuarios(self):
        """Lista todos los usuarios"""
        usuarios = self.usuario_service.listar_usuarios()
        
        if not usuarios:
            print("\n❌ No hay usuarios registrados")
            return
        
        print("\n👤 LISTA DE USUARIOS")
        print("-" * 70)
        print(f"{'ID':<10} {'Nombre':<25} {'Email':<30}")
        print("-" * 70)
        
        for usuario in usuarios:
            print(f"{usuario.id:<10} {usuario.nombre:<25} {usuario.email:<30}")
        
        print(f"\nTotal: {len(usuarios)} usuario(s)")
    
    def gestion_prestamos(self):
        """Submenú de gestión de préstamos"""
        while True:
            self.mostrar_menu_prestamos()
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == "1":
                self.prestar_libro()
            elif opcion == "2":
                self.devolver_libro()
            elif opcion == "3":
                self.ver_prestamos_activos()
            elif opcion == "4":
                self.ver_historial_prestamos()
            elif opcion == "5":
                break
            else:
                print("❌ Opción inválida")
            
            input("\nPresione Enter para continuar...")
    
    def prestar_libro(self):
        """Presta un libro a un usuario"""
        print("\n📤 PRESTAR LIBRO")
        print("-" * 50)
        
        # Mostrar libros disponibles
        disponibles = self.libro_service.obtener_disponibles()
        if not disponibles:
            print("❌ No hay libros disponibles para prestar")
            return
        
        print("\n📚 Libros disponibles:")
        for libro in disponibles:
            print(f"  {libro.id}: {libro.titulo} - {libro.autor}")
        
        libro_id = input("\nIngrese ID del libro: ").strip()
        
        # Mostrar usuarios
        usuarios = self.usuario_service.listar_usuarios()
        if not usuarios:
            print("❌ No hay usuarios registrados")
            return
        
        print("\n👤 Usuarios registrados:")
        for usuario in usuarios:
            print(f"  {usuario.id}: {usuario.nombre}")
        
        usuario_id = input("\nIngrese ID del usuario: ").strip()
        
        exito, mensaje, prestamo = self.prestamo_service.prestar_libro(libro_id, usuario_id)
        print(f"\n{mensaje}")
    
    def devolver_libro(self):
        """Devuelve un libro"""
        print("\n📥 DEVOLVER LIBRO")
        print("-" * 50)
        
        prestamos_activos = self.prestamo_service.listar_prestamos_activos()
        
        if not prestamos_activos:
            print("❌ No hay préstamos activos")
            return
        
        print("\n📋 Préstamos activos:")
        for prestamo in prestamos_activos:
            libro = self.libro_service.obtener_libro(prestamo.libro_id)
            usuario = self.usuario_service.obtener_usuario(prestamo.usuario_id)
            print(f"  {prestamo.id}: {libro.titulo} → {usuario.nombre}")
        
        prestamo_id = input("\nIngrese ID del préstamo a devolver: ").strip()
        exito, mensaje = self.prestamo_service.devolver_libro(prestamo_id)
        print(f"\n{mensaje}")
    
    def ver_prestamos_activos(self):
        """Ver préstamos activos"""
        prestamos = self.prestamo_service.listar_prestamos_activos()
        
        if not prestamos:
            print("\n❌ No hay préstamos activos")
            return
        
        print("\n🔄 PRÉSTAMOS ACTIVOS")
        print("-" * 100)
        print(f"{'ID':<10} {'Libro':<30} {'Usuario':<20} {'Fecha Préstamo':<20} {'Días':<5}")
        print("-" * 100)
        
        for prestamo in prestamos:
            libro = self.libro_service.obtener_libro(prestamo.libro_id)
            usuario = self.usuario_service.obtener_usuario(prestamo.usuario_id)
            
            fecha_prestamo = datetime.fromisoformat(prestamo.fecha_prestamo)
            dias = (datetime.now() - fecha_prestamo).days
            
            print(f"{prestamo.id:<10} {libro.titulo:<30} {usuario.nombre:<20} {prestamo.fecha_prestamo:<20} {dias:<5}")
        
        print(f"\nTotal: {len(prestamos)} préstamo(s) activo(s)")
    
    def ver_historial_prestamos(self):
        """Ver historial de todos los préstamos"""
        prestamos = self.prestamo_service.listar_todos_prestamos()
        
        if not prestamos:
            print("\n❌ No hay registros de préstamos")
            return
        
        print("\n📊 HISTORIAL DE PRÉSTAMOS")
        print("-" * 110)
        print(f"{'ID':<10} {'Libro':<25} {'Usuario':<18} {'Estado':<12} {'Fecha Préstamo':<18} {'Devolución':<18}")
        print("-" * 110)
        
        for prestamo in prestamos:
            libro = self.libro_service.obtener_libro(prestamo.libro_id)
            usuario = self.usuario_service.obtener_usuario(prestamo.usuario_id)
            
            estado = "✅ Devuelto" if prestamo.estado == "devuelto" else "🔴 Activo"
            fecha_dev = prestamo.fecha_devolucion if prestamo.fecha_devolucion else "-"
            
            print(f"{prestamo.id:<10} {libro.titulo:<25} {usuario.nombre:<18} {estado:<12} {prestamo.fecha_prestamo:<18} {fecha_dev:<18}")
        
        print(f"\nTotal: {len(prestamos)} registro(s)")
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas del sistema"""
        libros = self.libro_service.listar_libros()
        usuarios = self.usuario_service.listar_usuarios()
        prestamos = self.prestamo_service.listar_todos_prestamos()
        prestamos_activos = self.prestamo_service.listar_prestamos_activos()
        
        libros_disponibles = len(self.libro_service.obtener_disponibles())
        libros_prestados = len(libros) - libros_disponibles
        prestamos_devueltos = len(prestamos) - len(prestamos_activos)
        
        print("\n📊 ESTADÍSTICAS DEL SISTEMA")
        print("=" * 60)
        print(f"📚 Total de libros: {len(libros)}")
        print(f"   ✅ Disponibles: {libros_disponibles}")
        print(f"   🔴 Prestados: {libros_prestados}")
        print(f"\n👤 Total de usuarios: {len(usuarios)}")
        print(f"\n🔄 Total de préstamos: {len(prestamos)}")
        print(f"   🔴 Préstamos activos: {len(prestamos_activos)}")
        print(f"   ✅ Préstamos devueltos: {prestamos_devueltos}")
        print("=" * 60)
    
    def ejecutar(self):
        """Ejecuta la interfaz CLI principal"""
        while True:
            self.limpiar_pantalla()
            self.mostrar_titulo()
            self.mostrar_menu_principal()
            
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == "1":
                self.gestion_libros()
            elif opcion == "2":
                self.gestion_usuarios()
            elif opcion == "3":
                self.gestion_prestamos()
            elif opcion == "4":
                self.mostrar_estadisticas()
                input("\nPresione Enter para continuar...")
            elif opcion == "5":
                print("\n👋 ¡Hasta luego! Gracias por usar nuestro sistema de biblioteca.")
                break
            else:
                print("❌ Opción inválida")
                input("\nPresione Enter para continuar...")
