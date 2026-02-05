"""
TESTS UNITARIOS - Sistema de Gestión de Biblioteca

Este archivo contiene ejemplos de cómo testear el sistema.
Para ejecutar: python -m pytest tests/ -v
"""

def test_modelo_libro():
    """Test: Crear modelo de libro"""
    from src.domain.models import Libro
    
    libro = Libro(
        id="test123",
        titulo="Test",
        autor="Autor",
        año=2020,
        estado="disponible"
    )
    
    assert libro.id == "test123"
    assert libro.titulo == "Test"
    assert libro.estado == "disponible"
    print("✅ test_modelo_libro PASÓ")


def test_modelo_usuario():
    """Test: Crear modelo de usuario"""
    from src.domain.models import Usuario
    
    usuario = Usuario(
        id="user123",
        nombre="Juan",
        email="juan@test.com"
    )
    
    assert usuario.nombre == "Juan"
    assert usuario.email == "juan@test.com"
    print("✅ test_modelo_usuario PASÓ")


def test_validador_email():
    """Test: Validación de email"""
    from src.utils.validaciones import Validador
    
    valido, msg = Validador.validar_email("valido@test.com")
    assert valido == True
    
    valido, msg = Validador.validar_email("invalido@")
    assert valido == False
    print("✅ test_validador_email PASÓ")


def test_validador_año():
    """Test: Validación de año"""
    from src.utils.validaciones import Validador
    
    valido, msg = Validador.validar_año("2020")
    assert valido == True
    
    valido, msg = Validador.validar_año("3000")
    assert valido == False
    
    valido, msg = Validador.validar_año("abc")
    assert valido == False
    print("✅ test_validador_año PASÓ")


def test_validador_titulo():
    """Test: Validación de título"""
    from src.utils.validaciones import Validador
    
    valido, msg = Validador.validar_titulo("Don Quijote")
    assert valido == True
    
    valido, msg = Validador.validar_titulo("ab")
    assert valido == False
    print("✅ test_validador_titulo PASÓ")


def test_repository_crear_y_obtener():
    """Test: Repository - Crear y obtener libro"""
    import os
    import json
    from src.repository.libro_repository import LibroRepository
    
    # Usar archivo temporal
    archivo_test = "test_libros_temp.json"
    repo = LibroRepository(archivo_test)
    
    try:
        # Crear
        libro = repo.crear("Test Book", "Test Author", 2020)
        assert libro.titulo == "Test Book"
        
        # Obtener
        libro_obtenido = repo.obtener_por_id(libro.id)
        assert libro_obtenido is not None
        assert libro_obtenido.titulo == "Test Book"
        print("✅ test_repository_crear_y_obtener PASÓ")
    
    finally:
        # Limpiar
        if os.path.exists(archivo_test):
            os.remove(archivo_test)


def test_service_agregar_libro_valido():
    """Test: Service - Agregar libro válido"""
    import os
    from src.repository.libro_repository import LibroRepository
    from src.service.libro_service import LibroService
    
    archivo_test = "test_servicio_temp.json"
    repo = LibroRepository(archivo_test)
    service = LibroService(repo)
    
    try:
        exito, msg, libro = service.agregar_libro("Test", "Author", "2020")
        assert exito == True
        assert libro is not None
        print("✅ test_service_agregar_libro_valido PASÓ")
    
    finally:
        if os.path.exists(archivo_test):
            os.remove(archivo_test)


def test_service_agregar_libro_invalido():
    """Test: Service - Agregar libro con datos inválidos"""
    import os
    from src.repository.libro_repository import LibroRepository
    from src.service.libro_service import LibroService
    
    archivo_test = "test_servicio_temp2.json"
    repo = LibroRepository(archivo_test)
    service = LibroService(repo)
    
    try:
        # Título muy corto
        exito, msg, libro = service.agregar_libro("ab", "Author", "2020")
        assert exito == False
        
        # Año inválido
        exito, msg, libro = service.agregar_libro("Test", "Author", "3000")
        assert exito == False
        print("✅ test_service_agregar_libro_invalido PASÓ")
    
    finally:
        if os.path.exists(archivo_test):
            os.remove(archivo_test)


def test_usuario_email_unico():
    """Test: Usuario - Email debe ser único"""
    import os
    from src.repository.usuario_repository import UsuarioRepository
    from src.service.usuario_service import UsuarioService
    
    archivo_test = "test_usuario_temp.json"
    repo = UsuarioRepository(archivo_test)
    service = UsuarioService(repo)
    
    try:
        # Primer usuario
        exito1, msg1, usuario1 = service.registrar_usuario("Juan", "juan@test.com")
        assert exito1 == True
        
        # Segundo usuario con email duplicado
        exito2, msg2, usuario2 = service.registrar_usuario("Maria", "juan@test.com")
        assert exito2 == False
        assert "email ya está registrado" in msg2
        print("✅ test_usuario_email_unico PASÓ")
    
    finally:
        if os.path.exists(archivo_test):
            os.remove(archivo_test)


def test_prestamo_flujo_completo():
    """Test: Préstamo - Flujo completo (prestar y devolver)"""
    import os
    from src.repository.libro_repository import LibroRepository
    from src.repository.usuario_repository import UsuarioRepository
    from src.repository.prestamo_repository import PrestamoRepository
    from src.service.libro_service import LibroService
    from src.service.usuario_service import UsuarioService
    from src.service.prestamo_service import PrestamoService
    
    archivo_libros = "test_libros_flow.json"
    archivo_usuarios = "test_usuarios_flow.json"
    archivo_prestamos = "test_prestamos_flow.json"
    
    try:
        # Crear entidades
        libro_repo = LibroRepository(archivo_libros)
        usuario_repo = UsuarioRepository(archivo_usuarios)
        prestamo_repo = PrestamoRepository(archivo_prestamos)
        
        libro_service = LibroService(libro_repo)
        usuario_service = UsuarioService(usuario_repo)
        prestamo_service = PrestamoService(prestamo_repo, libro_repo)
        
        # Crear libro
        _, _, libro = libro_service.agregar_libro("Python", "Guido", "2020")
        
        # Crear usuario
        _, _, usuario = usuario_service.registrar_usuario("Juan", "juan@test.com")
        
        # Prestar
        exito_p, msg_p, prestamo = prestamo_service.prestar_libro(libro.id, usuario.id)
        assert exito_p == True
        
        # Verificar libro está prestado
        libro_check = libro_service.obtener_libro(libro.id)
        assert libro_check.estado == "prestado"
        
        # Devolver
        exito_d, msg_d = prestamo_service.devolver_libro(prestamo.id)
        assert exito_d == True
        
        # Verificar libro está disponible
        libro_check = libro_service.obtener_libro(libro.id)
        assert libro_check.estado == "disponible"
        
        print("✅ test_prestamo_flujo_completo PASÓ")
    
    finally:
        for f in [archivo_libros, archivo_usuarios, archivo_prestamos]:
            if os.path.exists(f):
                os.remove(f)


def test_no_prestar_libro_prestado():
    """Test: No permitir prestar libro que ya está prestado"""
    import os
    from src.repository.libro_repository import LibroRepository
    from src.repository.usuario_repository import UsuarioRepository
    from src.repository.prestamo_repository import PrestamoRepository
    from src.service.libro_service import LibroService
    from src.service.usuario_service import UsuarioService
    from src.service.prestamo_service import PrestamoService
    
    archivo_libros = "test_libros_doble.json"
    archivo_usuarios = "test_usuarios_doble.json"
    archivo_prestamos = "test_prestamos_doble.json"
    
    try:
        # Setup
        libro_repo = LibroRepository(archivo_libros)
        usuario_repo = UsuarioRepository(archivo_usuarios)
        prestamo_repo = PrestamoRepository(archivo_prestamos)
        
        libro_service = LibroService(libro_repo)
        usuario_service = UsuarioService(usuario_repo)
        prestamo_service = PrestamoService(prestamo_repo, libro_repo)
        
        # Crear libro y 2 usuarios
        _, _, libro = libro_service.agregar_libro("Test", "Author", "2020")
        _, _, usuario1 = usuario_service.registrar_usuario("Juan", "juan@test.com")
        _, _, usuario2 = usuario_service.registrar_usuario("Maria", "maria@test.com")
        
        # Primer préstamo (éxito)
        exito1, msg1, p1 = prestamo_service.prestar_libro(libro.id, usuario1.id)
        assert exito1 == True
        
        # Segundo préstamo (debe fallar)
        exito2, msg2, p2 = prestamo_service.prestar_libro(libro.id, usuario2.id)
        assert exito2 == False
        assert "no está disponible" in msg2
        
        print("✅ test_no_prestar_libro_prestado PASÓ")
    
    finally:
        for f in [archivo_libros, archivo_usuarios, archivo_prestamos]:
            if os.path.exists(f):
                os.remove(f)


def ejecutar_todos_tests():
    """Ejecuta todos los tests"""
    print("\n" + "="*60)
    print("🧪 EJECUTANDO TESTS UNITARIOS".center(60))
    print("="*60 + "\n")
    
    tests = [
        test_modelo_libro,
        test_modelo_usuario,
        test_validador_email,
        test_validador_año,
        test_validador_titulo,
        test_repository_crear_y_obtener,
        test_service_agregar_libro_valido,
        test_service_agregar_libro_invalido,
        test_usuario_email_unico,
        test_prestamo_flujo_completo,
        test_no_prestar_libro_prestado,
    ]
    
    pasados = 0
    fallidos = 0
    
    for test in tests:
        try:
            test()
            pasados += 1
        except AssertionError as e:
            print(f"❌ {test.__name__} FALLÓ: {str(e)}")
            fallidos += 1
        except Exception as e:
            print(f"❌ {test.__name__} ERROR: {str(e)}")
            fallidos += 1
    
    print("\n" + "="*60)
    print(f"✅ Pasados: {pasados} | ❌ Fallidos: {fallidos}")
    print("="*60 + "\n")
    
    return fallidos == 0


if __name__ == "__main__":
    import sys
    exito = ejecutar_todos_tests()
    sys.exit(0 if exito else 1)
