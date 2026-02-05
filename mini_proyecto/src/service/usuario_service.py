"""
Servicio de lógica de negocio para usuarios
"""
from typing import List, Tuple
from src.domain.models import Usuario
from src.repository.usuario_repository import UsuarioRepository
from src.utils.validaciones import Validador


class UsuarioService:
    """Servicio para gestión de usuarios"""
    
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository
        self.validador = Validador()
    
    def registrar_usuario(self, nombre: str, email: str) -> Tuple[bool, str, Usuario]:
        """
        Registra un nuevo usuario con validación
        
        Returns:
            (éxito, mensaje, usuario)
        """
        # Validaciones
        valido, msg = self.validador.validar_nombre(nombre)
        if not valido:
            return False, msg, None
        
        valido, msg = self.validador.validar_email(email)
        if not valido:
            return False, msg, None
        
        # Verificar email único
        if self.repository.obtener_por_email(email):
            return False, "❌ Este email ya está registrado", None
        
        try:
            usuario = self.repository.crear(nombre, email)
            return True, f"✅ Usuario '{nombre}' registrado exitosamente (ID: {usuario.id})", usuario
        except Exception as e:
            return False, f"❌ Error al registrar usuario: {str(e)}", None
    
    def listar_usuarios(self) -> List[Usuario]:
        """Lista todos los usuarios"""
        try:
            return self.repository.obtener_todos()
        except Exception as e:
            print(f"❌ Error al listar usuarios: {str(e)}")
            return []
    
    def obtener_usuario(self, usuario_id: str) -> Usuario:
        """Obtiene un usuario por ID"""
        try:
            return self.repository.obtener_por_id(usuario_id)
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None
    
    def obtener_por_email(self, email: str) -> Usuario:
        """Obtiene un usuario por email"""
        try:
            return self.repository.obtener_por_email(email)
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None
