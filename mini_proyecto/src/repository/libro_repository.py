"""
Repositorio para gestión de libros
"""
import uuid
from typing import List, Optional
from src.domain.models import Libro
from src.repository.base_repository import BaseRepository


class LibroRepository(BaseRepository):
    """Repositorio para libros"""
    
    def obtener_todos(self) -> List[Libro]:
        """Obtiene todos los libros"""
        datos = self._cargar()
        return [Libro.from_dict(item) for item in datos]
    
    def obtener_por_id(self, id: str) -> Optional[Libro]:
        """Obtiene un libro por ID"""
        datos = self._cargar()
        for item in datos:
            if item['id'] == id:
                return Libro.from_dict(item)
        return None
    
    def buscar_por_titulo(self, titulo: str) -> List[Libro]:
        """Busca libros por título (búsqueda parcial)"""
        datos = self._cargar()
        titulo_lower = titulo.lower()
        resultados = [
            Libro.from_dict(item) for item in datos
            if titulo_lower in item['titulo'].lower()
        ]
        return resultados
    
    def buscar_por_autor(self, autor: str) -> List[Libro]:
        """Busca libros por autor (búsqueda parcial)"""
        datos = self._cargar()
        autor_lower = autor.lower()
        resultados = [
            Libro.from_dict(item) for item in datos
            if autor_lower in item['autor'].lower()
        ]
        return resultados
    
    def crear(self, titulo: str, autor: str, año: int, estado: str = "disponible") -> Libro:
        """Crea un nuevo libro"""
        libro = Libro(
            id=str(uuid.uuid4())[:8],
            titulo=titulo,
            autor=autor,
            año=año,
            estado=estado
        )
        datos = self._cargar()
        datos.append(libro.to_dict())
        self._guardar(datos)
        return libro
    
    def eliminar(self, id: str) -> bool:
        """Elimina un libro"""
        datos = self._cargar()
        datos_filtrados = [item for item in datos if item['id'] != id]
        
        if len(datos_filtrados) == len(datos):
            return False
        
        self._guardar(datos_filtrados)
        return True
    
    def actualizar(self, id: str, **kwargs) -> bool:
        """Actualiza un libro"""
        datos = self._cargar()
        
        for item in datos:
            if item['id'] == id:
                item.update(kwargs)
                self._guardar(datos)
                return True
        
        return False
    
    def obtener_disponibles(self) -> List[Libro]:
        """Obtiene todos los libros disponibles"""
        datos = self._cargar()
        return [
            Libro.from_dict(item) for item in datos
            if item['estado'] == 'disponible'
        ]
