"""
Repositorio para gestión de préstamos
"""
import uuid
from typing import List, Optional
from datetime import datetime
from src.domain.models import Prestamo
from src.repository.base_repository import BaseRepository


class PrestamoRepository(BaseRepository):
    """Repositorio para préstamos"""
    
    def obtener_todos(self) -> List[Prestamo]:
        """Obtiene todos los préstamos"""
        datos = self._cargar()
        return [Prestamo.from_dict(item) for item in datos]
    
    def obtener_por_id(self, id: str) -> Optional[Prestamo]:
        """Obtiene un préstamo por ID"""
        datos = self._cargar()
        for item in datos:
            if item['id'] == id:
                return Prestamo.from_dict(item)
        return None
    
    def obtener_prestamos_activos(self) -> List[Prestamo]:
        """Obtiene todos los préstamos activos"""
        datos = self._cargar()
        return [
            Prestamo.from_dict(item) for item in datos
            if item['estado'] == 'activo'
        ]
    
    def obtener_prestamos_usuario(self, usuario_id: str) -> List[Prestamo]:
        """Obtiene préstamos de un usuario específico"""
        datos = self._cargar()
        return [
            Prestamo.from_dict(item) for item in datos
            if item['usuario_id'] == usuario_id
        ]
    
    def obtener_prestamos_activos_usuario(self, usuario_id: str) -> List[Prestamo]:
        """Obtiene préstamos activos de un usuario"""
        datos = self._cargar()
        return [
            Prestamo.from_dict(item) for item in datos
            if item['usuario_id'] == usuario_id and item['estado'] == 'activo'
        ]
    
    def obtener_prestamo_libro_activo(self, libro_id: str) -> Optional[Prestamo]:
        """Obtiene el préstamo activo de un libro (si existe)"""
        datos = self._cargar()
        for item in datos:
            if item['libro_id'] == libro_id and item['estado'] == 'activo':
                return Prestamo.from_dict(item)
        return None
    
    def crear(self, libro_id: str, usuario_id: str) -> Prestamo:
        """Crea un nuevo préstamo"""
        prestamo = Prestamo(
            id=str(uuid.uuid4())[:8],
            libro_id=libro_id,
            usuario_id=usuario_id,
            fecha_prestamo=datetime.now().isoformat(),
            estado='activo'
        )
        datos = self._cargar()
        datos.append(prestamo.to_dict())
        self._guardar(datos)
        return prestamo
    
    def eliminar(self, id: str) -> bool:
        """Elimina un préstamo"""
        datos = self._cargar()
        datos_filtrados = [item for item in datos if item['id'] != id]
        
        if len(datos_filtrados) == len(datos):
            return False
        
        self._guardar(datos_filtrados)
        return True
    
    def actualizar(self, id: str, **kwargs) -> bool:
        """Actualiza un préstamo"""
        datos = self._cargar()
        
        for item in datos:
            if item['id'] == id:
                item.update(kwargs)
                self._guardar(datos)
                return True
        
        return False
