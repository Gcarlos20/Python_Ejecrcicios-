"""
Servicio de lógica de negocio para préstamos
"""
from typing import List, Tuple
from datetime import datetime
from src.domain.models import Prestamo, Libro
from src.repository.prestamo_repository import PrestamoRepository
from src.repository.libro_repository import LibroRepository


class PrestamoService:
    """Servicio para gestión de préstamos"""
    
    def __init__(self, prestamo_repo: PrestamoRepository, libro_repo: LibroRepository):
        self.prestamo_repo = prestamo_repo
        self.libro_repo = libro_repo
    
    def prestar_libro(self, libro_id: str, usuario_id: str) -> Tuple[bool, str, Prestamo]:
        """
        Presta un libro a un usuario
        
        Returns:
            (éxito, mensaje, prestamo)
        """
        # Validar que el libro existe
        libro = self.libro_repo.obtener_por_id(libro_id)
        if not libro:
            return False, f"❌ Libro no encontrado (ID: {libro_id})", None
        
        # Validar que el libro está disponible
        if libro.estado != "disponible":
            return False, f"❌ El libro '{libro.titulo}' no está disponible para prestar", None
        
        # Validar que no hay otro préstamo activo
        prestamo_activo = self.prestamo_repo.obtener_prestamo_libro_activo(libro_id)
        if prestamo_activo:
            return False, f"❌ El libro ya está prestado a otro usuario", None
        
        try:
            # Crear préstamo
            prestamo = self.prestamo_repo.crear(libro_id, usuario_id)
            
            # Actualizar estado del libro
            self.libro_repo.actualizar(libro_id, estado="prestado")
            
            msg = f"✅ Libro '{libro.titulo}' prestado exitosamente (Préstamo ID: {prestamo.id})"
            return True, msg, prestamo
        except Exception as e:
            return False, f"❌ Error al prestar libro: {str(e)}", None
    
    def devolver_libro(self, prestamo_id: str) -> Tuple[bool, str]:
        """
        Devuelve un libro
        
        Returns:
            (éxito, mensaje)
        """
        try:
            prestamo = self.prestamo_repo.obtener_por_id(prestamo_id)
            if not prestamo:
                return False, f"❌ Préstamo no encontrado (ID: {prestamo_id})"
            
            if prestamo.estado == "devuelto":
                return False, "❌ Este préstamo ya fue devuelto"
            
            # Actualizar estado del préstamo
            self.prestamo_repo.actualizar(
                prestamo_id,
                estado="devuelto",
                fecha_devolucion=datetime.now().isoformat()
            )
            
            # Actualizar estado del libro
            self.libro_repo.actualizar(prestamo.libro_id, estado="disponible")
            
            libro = self.libro_repo.obtener_por_id(prestamo.libro_id)
            msg = f"✅ Libro '{libro.titulo}' devuelto correctamente"
            return True, msg
        except Exception as e:
            return False, f"❌ Error al devolver libro: {str(e)}"
    
    def listar_prestamos_activos(self) -> List[Prestamo]:
        """Lista todos los préstamos activos"""
        try:
            return self.prestamo_repo.obtener_prestamos_activos()
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return []
    
    def listar_todos_prestamos(self) -> List[Prestamo]:
        """Lista todos los préstamos (activos y devueltos)"""
        try:
            return self.prestamo_repo.obtener_todos()
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return []
    
    def obtener_prestamos_usuario(self, usuario_id: str) -> List[Prestamo]:
        """Obtiene todos los préstamos de un usuario"""
        try:
            return self.prestamo_repo.obtener_prestamos_usuario(usuario_id)
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return []
    
    def obtener_prestamos_activos_usuario(self, usuario_id: str) -> List[Prestamo]:
        """Obtiene préstamos activos de un usuario"""
        try:
            return self.prestamo_repo.obtener_prestamos_activos_usuario(usuario_id)
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return []
