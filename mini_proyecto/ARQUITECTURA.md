# 🏗️ Documentación Técnica - Sistema de Gestión de Biblioteca

## Índice
1. [Arquitectura](#arquitectura)
2. [Componentes](#componentes)
3. [Flujos de Datos](#flujos-de-datos)
4. [Patrones Implementados](#patrones-implementados)
5. [Detalles de Implementación](#detalles-de-implementación)

---

## 🏗️ Arquitectura

El sistema sigue el patrón de **Arquitectura Limpia (Clean Architecture)** con una estructura de capas:

```
┌─────────────────────────────────────────┐
│         INTERFAZ (UI)                   │
│    CLI - Interacción con Usuario        │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         SERVICIOS (Business Logic)      │
│   - Validaciones                        │
│   - Reglas de negocio                   │
│   - Orquestación                        │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│        REPOSITORIOS (Data Access)       │
│   - CRUD Operations                     │
│   - Persistencia en JSON                │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│        DOMINIO (Modelos)                │
│   - Entidades (Libro, Usuario, etc)     │
│   - Lógica de dominio pura              │
└─────────────────────────────────────────┘
```

---

## 📦 Componentes

### 1. **Domain Layer** (`src/domain/`)

#### `models.py`
Define las entidades del sistema usando dataclasses:

- **Libro**: id, titulo, autor, año, estado, fecha_creacion
- **Usuario**: id, nombre, email, fecha_registro
- **Prestamo**: id, libro_id, usuario_id, fecha_prestamo, fecha_devolucion, estado

**Responsabilidades**:
- Definir la estructura de datos
- Métodos de conversión (to_dict/from_dict)
- Valores por defecto

### 2. **Repository Layer** (`src/repository/`)

#### `base_repository.py` (Clase Abstracta)
```python
class BaseRepository(ABC):
    - _cargar()      # Lee JSON
    - _guardar()     # Escribe JSON
    - obtener_todos()
    - obtener_por_id()
    - crear()
    - actualizar()
    - eliminar()
```

**Patrones aplicados**:
- Template Method Pattern
- Abstract Base Class
- Single Responsibility

#### `libro_repository.py`
Métodos CRUD + búsquedas específicas:
- `buscar_por_titulo()`
- `buscar_por_autor()`
- `obtener_disponibles()`

#### `usuario_repository.py`
Métodos CRUD + búsqueda:
- `obtener_por_email()` - Validar unicidad

#### `prestamo_repository.py`
Métodos CRUD + búsquedas especializadas:
- `obtener_prestamos_activos()`
- `obtener_prestamo_libro_activo()`
- `obtener_prestamos_usuario()`

**Persistencia**:
- Archivos JSON en carpeta `/data`
- Encoding UTF-8
- Formato indentado (2 espacios)

### 3. **Service Layer** (`src/service/`)

Contiene la lógica de negocio y validaciones.

#### `libro_service.py`
```python
class LibroService:
    - agregar_libro()      # Validaciones + repositorio
    - listar_libros()
    - buscar_por_titulo()  # Con manejo de errores
    - buscar_por_autor()
    - eliminar_libro()     # Validar que no está prestado
    - obtener_disponibles()
```

**Validaciones implementadas**:
- Título: mínimo 3 caracteres
- Autor: mínimo 3 caracteres
- Año: entre 1000 y 2100

#### `usuario_service.py`
```python
class UsuarioService:
    - registrar_usuario()  # Email único + validaciones
    - listar_usuarios()
    - obtener_usuario()
    - obtener_por_email()
```

**Validaciones implementadas**:
- Email: formato válido (regex)
- Email: debe ser único
- Nombre: mínimo 3 caracteres

#### `prestamo_service.py`
```python
class PrestamoService:
    - prestar_libro()      # Validaciones complejas
    - devolver_libro()     # Actualizar estado
    - listar_prestamos_activos()
    - obtener_prestamos_usuario()
```

**Lógica de negocio compleja**:
```
prestar_libro():
├─ Validar libro existe
├─ Validar libro está disponible
├─ Validar no hay préstamo activo
├─ Crear préstamo
├─ Actualizar estado libro
└─ Guardar persistencia

devolver_libro():
├─ Validar préstamo existe
├─ Validar no fue devuelto ya
├─ Marcar como devuelto
├─ Registrar fecha
├─ Actualizar estado libro
└─ Guardar persistencia
```

### 4. **UI Layer** (`src/ui/`)

#### `cli.py` - Interfaz de Línea de Comandos
```python
class BibliotecaCLI:
    - ejecutar()                 # Loop principal
    - gestion_libros()           # Submenú
    - gestion_usuarios()
    - gestion_prestamos()
    - mostrar_estadisticas()
```

**Características UI**:
- Menús con bordes ASCII art
- Iconos emoji (📚, 👤, 🔄, etc)
- Tablas formateadas con columnas
- Navegación clara y intuitiva
- Mensajes de éxito/error diferenciados

### 5. **Utils** (`src/utils/`)

#### `validaciones.py`
Clase estática con métodos de validación reutilizables:
```python
class Validador:
    - validar_email()      # Regex pattern
    - validar_titulo()     # Longitud mínima
    - validar_autor()
    - validar_año()        # Rango numérico
    - validar_nombre()
```

**Retorna**: Tuple[bool, str] - (valido, mensaje_error)

---

## 🔄 Flujos de Datos

### Flujo: Agregar Libro

```
CLI (usuario input)
    │
    ├─→ BibliotecaCLI.agregar_libro()
    │       │
    │       └─→ LibroService.agregar_libro()
    │               │
    │               ├─→ Validador.validar_titulo()
    │               ├─→ Validador.validar_autor()
    │               ├─→ Validador.validar_año()
    │               │
    │               └─→ LibroRepository.crear()
    │                       │
    │                       ├─→ UUID generation
    │                       ├─→ Create Libro object
    │                       ├─→ _cargar() from JSON
    │                       ├─→ Append to list
    │                       └─→ _guardar() to JSON
    │
    └─→ Mostrar resultado (éxito/error)
```

### Flujo: Prestar Libro

```
CLI (usuario input)
    │
    ├─→ BibliotecaCLI.prestar_libro()
    │       │
    │       ├─→ Mostrar libros disponibles
    │       │   └─→ LibroService.obtener_disponibles()
    │       │       └─→ LibroRepository.obtener_disponibles()
    │       │
    │       ├─→ Mostrar usuarios
    │       │   └─→ UsuarioService.listar_usuarios()
    │       │
    │       └─→ PrestamoService.prestar_libro()
    │               │
    │               ├─→ Validar libro existe
    │               │   └─→ LibroRepository.obtener_por_id()
    │               │
    │               ├─→ Validar libro está disponible
    │               │
    │               ├─→ Validar no hay préstamo activo
    │               │   └─→ PrestamoRepository.obtener_prestamo_libro_activo()
    │               │
    │               ├─→ PrestamoRepository.crear()
    │               │
    │               └─→ LibroRepository.actualizar(estado='prestado')
    │
    └─→ Mostrar resultado
```

### Flujo: Devolver Libro

```
CLI (usuario input)
    │
    ├─→ BibliotecaCLI.devolver_libro()
    │       │
    │       ├─→ Mostrar préstamos activos
    │       │   └─→ PrestamoService.listar_prestamos_activos()
    │       │
    │       └─→ PrestamoService.devolver_libro()
    │               │
    │               ├─→ Validar préstamo existe
    │               ├─→ Validar no fue devuelto ya
    │               │
    │               ├─→ PrestamoRepository.actualizar()
    │               │   ├─→ estado = 'devuelto'
    │               │   └─→ fecha_devolucion = now()
    │               │
    │               └─→ LibroRepository.actualizar(estado='disponible')
    │
    └─→ Mostrar resultado
```

---

## 🎯 Patrones Implementados

### 1. **Repository Pattern**
- Abstracción de la persistencia
- CRUD operations en repositorios
- Fácil cambiar de JSON a BD

```python
# Implementación
class LibroRepository(BaseRepository):
    def crear(self, titulo, autor, año):
        libro = Libro(...)
        datos = self._cargar()
        datos.append(libro.to_dict())
        self._guardar(datos)
```

### 2. **Service Layer**
- Lógica de negocio separada
- Validaciones centralizadas
- Orquestación de repositorios

```python
class LibroService:
    def __init__(self, repository):
        self.repository = repository
    
    def agregar_libro(self, titulo, autor, año):
        # Validación
        valido, msg = self.validador.validar_titulo(titulo)
        # Operación
        libro = self.repository.crear(titulo, autor, año)
```

### 3. **Dependency Injection**
- Servicios reciben repositorios en constructor
- Bajo acoplamiento
- Fácil testing

```python
clase LibroService:
    def __init__(self, repository: LibroRepository):
        self.repository = repository  # Inyectado
```

### 4. **Abstract Base Class**
- Contrato de repositorios
- Métodos comunes (cargar/guardar)

```python
from abc import ABC, abstractmethod

class BaseRepository(ABC):
    def _cargar(self):  # Implementación común
        pass
    
    @abstractmethod
    def obtener_todos(self):  # Contrato
        pass
```

### 5. **Dataclasses**
- Modelos simples y claros
- Métodos automáticos (__init__, __repr__)
- Conversión fácil a/desde dict

```python
@dataclass
class Libro:
    id: str
    titulo: str
    estado: str = "disponible"
    
    def to_dict(self):
        return asdict(self)
```

### 6. **Tuple Unpacking para Retorno**
- Retornar múltiples valores
- Patrón clara de éxito/error

```python
exito, mensaje, libro = service.agregar_libro(...)
if exito:
    print(mensaje)
```

---

## 🔧 Detalles de Implementación

### Persistencia en JSON

**Estructura de directorios**:
```
data/
├── libros.json      # [{ id, titulo, autor, año, estado, fecha_creacion }, ...]
├── usuarios.json    # [{ id, nombre, email, fecha_registro }, ...]
└── prestamos.json   # [{ id, libro_id, usuario_id, fecha_prestamo, estado }, ...]
```

**Operaciones**:
```python
# Cargar
with open(archivo, 'r', encoding='utf-8') as f:
    datos = json.load(f)

# Guardar
with open(archivo, 'w', encoding='utf-8') as f:
    json.dump(datos, f, ensure_ascii=False, indent=2)
```

### Manejo de Errores

**Try-Except en múltiples niveles**:
```python
# Nivel 1: Validación en Service
def agregar_libro(self, ...):
    valido, msg = self.validador.validar_titulo(titulo)
    if not valido:
        return False, msg, None

# Nivel 2: Persistencia
try:
    libro = self.repository.crear(...)
    return True, f"✅ Éxito", libro
except Exception as e:
    return False, f"❌ Error: {str(e)}", None

# Nivel 3: UI captura errores
try:
    self.gestion_libros()
except Exception as e:
    print(f"❌ Error fatal: {e}")
```

### UUID para IDs

```python
import uuid

id = str(uuid.uuid4())[:8]  # "a1b2c3d4"
```

**Ventajas**:
- Único garantizado
- No requiere base de datos
- Independiente de inserciones

### Timestamps ISO 8601

```python
from datetime import datetime

timestamp = datetime.now().isoformat()
# Resultado: "2026-02-04T19:30:45.123456"
```

**Ventajas**:
- Formato estándar
- Sorteable como string
- Compatible con JSON

---

## 📊 Estadísticas y Reportes

El sistema proporciona:
- Total de libros (disponibles vs prestados)
- Total de usuarios
- Resumen de préstamos (activos vs devueltos)
- Historial completo de préstamos con fechas

---

## 🔒 Validaciones y Seguridad

### Validaciones de Entrada
- Email: formato regex
- Números: rango permitido
- Strings: longitud mínima
- Unicidad: emails duplicados

### Integridad de Datos
- No eliminar libros prestados
- No prestar libros no disponibles
- No devolver préstamos devueltos
- Refs. automáticas (libro↔prestamo↔usuario)

### Manejo de Excepciones
- Try-catch en capas críticas
- Mensajes descriptivos
- Logging de errores

---

## 🚀 Escalabilidad

### Cambios Mínimos para:

**Usar SQLite en lugar de JSON**:
```python
# Solo cambiar LibroRepository
class LibroRepository(BaseRepository):
    def __init__(self, db_path):
        self.db = sqlite3.connect(db_path)
    
    def crear(self, ...):
        self.db.execute("INSERT INTO libros ...")
        self.db.commit()
```

**Agregar roles de usuario**:
```python
@dataclass
class Usuario:
    id: str
    nombre: str
    email: str
    rol: str = "usuario"  # "admin", "usuario"
```

**Agregar multas por retrasos**:
```python
def calcular_multa(self, prestamo_id):
    prestamo = self.prestamo_repo.obtener_por_id(prestamo_id)
    dias_retraso = (datetime.now() - prestamo.fecha_prestamo).days - 14
    if dias_retraso > 0:
        multa = dias_retraso * 0.50  # $0.50 por día
        return multa
    return 0
```

---

## 📚 Referencias

- Clean Architecture: Robert C. Martin
- Design Patterns: Gang of Four
- Python Best Practices: PEP 8, PEP 20

---

**Versión**: 1.0  
**Fecha**: Febrero 2026  
**Estado**: Producción
