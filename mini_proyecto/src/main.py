"""
Punto de entrada principal de la aplicación
"""
import os
from src.repository.libro_repository import LibroRepository
from src.repository.usuario_repository import UsuarioRepository
from src.repository.prestamo_repository import PrestamoRepository
from src.service.libro_service import LibroService
from src.service.usuario_service import UsuarioService
from src.service.prestamo_service import PrestamoService
from src.ui.cli import BibliotecaCLI


def crear_estructura_datos():
    """Crea la estructura de directorios para los datos"""
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)


def main():
    """Función principal"""
    try:
        # Crear estructura
        crear_estructura_datos()
        
        # Inicializar repositorios
        libro_repo = LibroRepository("data/libros.json")
        usuario_repo = UsuarioRepository("data/usuarios.json")
        prestamo_repo = PrestamoRepository("data/prestamos.json")
        
        # Inicializar servicios
        libro_service = LibroService(libro_repo)
        usuario_service = UsuarioService(usuario_repo)
        prestamo_service = PrestamoService(prestamo_repo, libro_repo)
        
        # Inicializar CLI
        cli = BibliotecaCLI(libro_service, usuario_service, prestamo_service)
        
        # Ejecutar
        cli.ejecutar()
        
    except Exception as e:
        print(f"❌ Error fatal: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
