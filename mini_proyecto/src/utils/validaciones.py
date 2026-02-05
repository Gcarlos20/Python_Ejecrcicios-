"""
Validaciones para el sistema
"""
import re
from typing import Tuple


class Validador:
    """Clase para validaciones del sistema"""
    
    @staticmethod
    def validar_email(email: str) -> Tuple[bool, str]:
        """Valida formato de email"""
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(patron, email):
            return True, ""
        return False, "Email inválido. Use formato: usuario@dominio.com"
    
    @staticmethod
    def validar_titulo(titulo: str) -> Tuple[bool, str]:
        """Valida título del libro"""
        if not titulo or len(titulo.strip()) < 3:
            return False, "El título debe tener al menos 3 caracteres"
        return True, ""
    
    @staticmethod
    def validar_autor(autor: str) -> Tuple[bool, str]:
        """Valida nombre del autor"""
        if not autor or len(autor.strip()) < 3:
            return False, "El autor debe tener al menos 3 caracteres"
        return True, ""
    
    @staticmethod
    def validar_año(año: str) -> Tuple[bool, str]:
        """Valida año de publicación"""
        try:
            año_int = int(año)
            if año_int < 1000 or año_int > 2100:
                return False, "El año debe estar entre 1000 y 2100"
            return True, ""
        except ValueError:
            return False, "El año debe ser un número válido"
    
    @staticmethod
    def validar_nombre(nombre: str) -> Tuple[bool, str]:
        """Valida nombre de usuario"""
        if not nombre or len(nombre.strip()) < 3:
            return False, "El nombre debe tener al menos 3 caracteres"
        return True, ""
