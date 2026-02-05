"""
Repositorio base para la persistencia
"""
import json
import os
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from datetime import datetime


class BaseRepository(ABC):
    """Clase base para repositorios"""
    
    def __init__(self, archivo_datos: str):
        """
        Inicializa el repositorio
        
        Args:
            archivo_datos: Ruta del archivo JSON para persistencia
        """
        self.archivo_datos = archivo_datos
        self._crear_directorio()
        self._asegurar_archivo()
    
    def _crear_directorio(self):
        """Crea el directorio si no existe"""
        directorio = os.path.dirname(self.archivo_datos)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio, exist_ok=True)
    
    def _asegurar_archivo(self):
        """Asegura que el archivo JSON existe"""
        if not os.path.exists(self.archivo_datos):
            self._guardar([])
    
    def _cargar(self) -> List[Dict[str, Any]]:
        """Carga datos del archivo JSON"""
        try:
            with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                return datos if isinstance(datos, list) else []
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def _guardar(self, datos: List[Dict[str, Any]]):
        """Guarda datos en el archivo JSON"""
        try:
            with open(self.archivo_datos, 'w', encoding='utf-8') as f:
                json.dump(datos, f, ensure_ascii=False, indent=2)
        except IOError as e:
            print(f"⚠️ Error al guardar datos: {str(e)}")
    
    @abstractmethod
    def obtener_todos(self):
        """Obtiene todos los elementos"""
        pass
    
    @abstractmethod
    def obtener_por_id(self, id: str):
        """Obtiene un elemento por ID"""
        pass
    
    @abstractmethod
    def crear(self, **kwargs):
        """Crea un nuevo elemento"""
        pass
    
    @abstractmethod
    def eliminar(self, id: str) -> bool:
        """Elimina un elemento"""
        pass
    
    @abstractmethod
    def actualizar(self, id: str, **kwargs) -> bool:
        """Actualiza un elemento"""
        pass
