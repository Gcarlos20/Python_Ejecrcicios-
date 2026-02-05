"""
Modelos de dominio para la biblioteca
"""
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Literal


@dataclass
class Libro:
    """Representa un libro en la biblioteca"""
    id: str
    titulo: str
    autor: str
    año: int
    estado: Literal["disponible", "prestado"]
    fecha_creacion: str = None
    
    def __post_init__(self):
        if self.fecha_creacion is None:
            self.fecha_creacion = datetime.now().isoformat()
    
    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)


@dataclass
class Usuario:
    """Representa un usuario registrado"""
    id: str
    nombre: str
    email: str
    fecha_registro: str = None
    
    def __post_init__(self):
        if self.fecha_registro is None:
            self.fecha_registro = datetime.now().isoformat()
    
    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)


@dataclass
class Prestamo:
    """Representa un préstamo de libro"""
    id: str
    libro_id: str
    usuario_id: str
    fecha_prestamo: str
    fecha_devolucion: str = None
    estado: Literal["activo", "devuelto"] = "activo"
    
    def __post_init__(self):
        if not self.fecha_prestamo:
            self.fecha_prestamo = datetime.now().isoformat()
    
    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
