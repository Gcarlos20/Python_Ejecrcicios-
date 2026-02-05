"""
Repositorio para gestión de usuarios
"""
import uuid
from typing import List, Optional
from src.domain.models import Usuario
from src.repository.base_repository import BaseRepository


class UsuarioRepository(BaseRepository):
    """Repositorio para usuarios"""
    
    def obtener_todos(self) -> List[Usuario]:
        """Obtiene todos los usuarios"""
        datos = self._cargar()
        return [Usuario.from_dict(item) for item in datos]
    
    def obtener_por_id(self, id: str) -> Optional[Usuario]:
        """Obtiene un usuario por ID"""
        datos = self._cargar()
        for item in datos:
            if item['id'] == id:
                return Usuario.from_dict(item)
        return None
    
    def obtener_por_email(self, email: str) -> Optional[Usuario]:
        """Obtiene un usuario por email"""
        datos = self._cargar()
        for item in datos:
            if item['email'].lower() == email.lower():
                return Usuario.from_dict(item)
        return None
    
    def crear(self, nombre: str, email: str) -> Usuario:
        """Crea un nuevo usuario"""
        usuario = Usuario(
            id=str(uuid.uuid4())[:8],
            nombre=nombre,
            email=email
        )
        datos = self._cargar()
        datos.append(usuario.to_dict())
        self._guardar(datos)
        return usuario
    
    def eliminar(self, id: str) -> bool:
        """Elimina un usuario"""
        datos = self._cargar()
        datos_filtrados = [item for item in datos if item['id'] != id]
        
        if len(datos_filtrados) == len(datos):
            return False
        
        self._guardar(datos_filtrados)
        return True
    
    def actualizar(self, id: str, **kwargs) -> bool:
        """Actualiza un usuario"""
        datos = self._cargar()
        
        for item in datos:
            if item['id'] == id:
                item.update(kwargs)
                self._guardar(datos)
                return True
        
        return False
