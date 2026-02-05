"""
Script para cargar datos de ejemplo en la biblioteca
"""
from src.repository.libro_repository import LibroRepository
from src.repository.usuario_repository import UsuarioRepository
from src.repository.prestamo_repository import PrestamoRepository
from src.service.libro_service import LibroService
from src.service.usuario_service import UsuarioService
from src.service.prestamo_service import PrestamoService


def cargar_datos_ejemplo():
    """Carga datos de ejemplo en el sistema"""
    
    # Inicializar repositorios
    libro_repo = LibroRepository("data/libros.json")
    usuario_repo = UsuarioRepository("data/usuarios.json")
    prestamo_repo = PrestamoRepository("data/prestamos.json")
    
    # Inicializar servicios
    libro_service = LibroService(libro_repo)
    usuario_service = UsuarioService(usuario_repo)
    prestamo_service = PrestamoService(prestamo_repo, libro_repo)
    
    print("📚 Cargando datos de ejemplo...\n")
    
    # Agregar libros
    libros_data = [
        ("Don Quijote", "Miguel de Cervantes", 1605),
        ("El Quijote Parte II", "Miguel de Cervantes", 1615),
        ("Orgullo y Prejuicio", "Jane Austen", 1813),
        ("Cien Años de Soledad", "Gabriel García Márquez", 1967),
        ("1984", "George Orwell", 1949),
        ("El Principito", "Antoine de Saint-Exupéry", 1943),
        ("Mujercitas", "Louisa May Alcott", 1868),
        ("El Conde de Montecristo", "Alexandre Dumas", 1844),
        ("Crimen y Castigo", "Fiódor Dostoyevski", 1866),
        ("La Iliada", "Homero", -750),
    ]
    
    print("Agregando libros...")
    libro_ids = []
    for titulo, autor, año in libros_data:
        exito, msg, libro = libro_service.agregar_libro(titulo, autor, str(año))
        if exito:
            libro_ids.append(libro.id)
            print(f"  ✅ {titulo}")
    
    # Agregar usuarios
    usuarios_data = [
        ("Juan Pérez", "juan@example.com"),
        ("María García", "maria@example.com"),
        ("Carlos López", "carlos@example.com"),
        ("Ana Martínez", "ana@example.com"),
        ("Pedro Rodríguez", "pedro@example.com"),
    ]
    
    print("\nAgregando usuarios...")
    usuario_ids = []
    for nombre, email in usuarios_data:
        exito, msg, usuario = usuario_service.registrar_usuario(nombre, email)
        if exito:
            usuario_ids.append(usuario.id)
            print(f"  ✅ {nombre}")
    
    # Crear algunos préstamos
    print("\nCreando préstamos de ejemplo...")
    if len(libro_ids) >= 3 and len(usuario_ids) >= 3:
        # Préstamo 1
        exito, msg, prestamo = prestamo_service.prestar_libro(libro_ids[0], usuario_ids[0])
        if exito:
            print(f"  ✅ {msg.split('(')[0].strip()}")
        
        # Préstamo 2
        exito, msg, prestamo = prestamo_service.prestar_libro(libro_ids[1], usuario_ids[1])
        if exito:
            print(f"  ✅ {msg.split('(')[0].strip()}")
        
        # Préstamo 3
        exito, msg, prestamo = prestamo_service.prestar_libro(libro_ids[2], usuario_ids[2])
        if exito:
            print(f"  ✅ {msg.split('(')[0].strip()}")
    
    print("\n✅ ¡Datos de ejemplo cargados correctamente!")
    print("\nPuede ejecutar 'python app.py' para usar el sistema.\n")


if __name__ == "__main__":
    cargar_datos_ejemplo()
