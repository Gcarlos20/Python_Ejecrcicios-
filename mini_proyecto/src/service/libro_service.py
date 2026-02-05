"""
Servicio de lógica de negocio para libros
"""
from typing import List, Tuple
from src.domain.models import Libro
from src.repository.libro_repository import LibroRepository
from src.utils.validaciones import Validador


class LibroService:
    """Servicio para gestión de libros"""
    
    def __init__(self, repository: LibroRepository):
        self.repository = repository
        self.validador = Validador()
    
    def agregar_libro(self, titulo: str, autor: str, año: str) -> Tuple[bool, str, Libro]:
        """
        Agrega un nuevo libro con validación
        
        Returns:
            (éxito, mensaje, libro)
        """
        # Validaciones
        valido, msg = self.validador.validar_titulo(titulo)
        if not valido:
            return False, msg, None
        
        valido, msg = self.validador.validar_autor(autor)
        if not valido:
            return False, msg, None
        
        valido, msg = self.validador.validar_año(año)
        if not valido:
            return False, msg, None
        
        try:
            libro = self.repository.crear(titulo, autor, int(año))
            return True, f"✅ Libro '{titulo}' agregado exitosamente (ID: {libro.id})", libro
        except Exception as e:
            return False, f"❌ Error al agregar libro: {str(e)}", None
    
    def listar_libros(self) -> List[Libro]:
        """Lista todos los libros"""
        try:
            return self.repository.obtener_todos()
        except Exception as e:
            print(f"❌ Error al listar libros: {str(e)}")
            return []
    
    def buscar_por_titulo(self, titulo: str) -> Tuple[bool, str, List[Libro]]:
        """Busca libros por título"""
        if not titulo or len(titulo.strip()) < 1:
            return False, "❌ El término de búsqueda no puede estar vacío", []
        
        try:
            resultados = self.repository.buscar_por_titulo(titulo)
            if resultados:
                msg = f"✅ Se encontraron {len(resultados)} libro(s)"
                return True, msg, resultados
            else:
                return False, "❌ No se encontraron libros con ese título", []
        except Exception as e:
            return False, f"❌ Error en búsqueda: {str(e)}", []
    
    def buscar_por_autor(self, autor: str) -> Tuple[bool, str, List[Libro]]:
        """Busca libros por autor"""
        if not autor or len(autor.strip()) < 1:
            return False, "❌ El nombre del autor no puede estar vacío", []
        
        try:
            resultados = self.repository.buscar_por_autor(autor)
            if resultados:
                msg = f"✅ Se encontraron {len(resultados)} libro(s)"
                return True, msg, resultados
            else:
                return False, "❌ No se encontraron libros de ese autor", []
        except Exception as e:
            return False, f"❌ Error en búsqueda: {str(e)}", []
    
    def eliminar_libro(self, libro_id: str) -> Tuple[bool, str]:
        """Elimina un libro"""
        try:
            libro = self.repository.obtener_por_id(libro_id)
            if not libro:
                return False, f"❌ Libro no encontrado (ID: {libro_id})"
            
            if libro.estado == "prestado":
                return False, "❌ No se puede eliminar un libro que está prestado"
            
            if self.repository.eliminar(libro_id):
                return True, f"✅ Libro '{libro.titulo}' eliminado correctamente"
            else:
                return False, "❌ Error al eliminar el libro"
        except Exception as e:
            return False, f"❌ Error: {str(e)}"
    
    def obtener_libro(self, libro_id: str) -> Libro:
        """Obtiene un libro por ID"""
        try:
            return self.repository.obtener_por_id(libro_id)
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None
    
    def obtener_disponibles(self) -> List[Libro]:
        """Obtiene libros disponibles para prestar"""
        try:
            return self.repository.obtener_disponibles()
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return []
