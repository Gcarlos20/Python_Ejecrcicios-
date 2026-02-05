# Sistema de Gestión de Biblioteca

## 📋 Descripción

Sistema completo de gestión de biblioteca implementado en Python con arquitectura limpia, persistencia en JSON y CLI interactiva. Incluye validaciones robustas y manejo de errores.

## 🏗️ Arquitectura

```
src/
├── domain/           # Modelos de dominio (Libro, Usuario, Préstamo)
├── repository/       # Capa de persistencia (acceso a datos)
├── service/          # Lógica de negocio
├── ui/               # Interfaz CLI
├── utils/            # Utilidades (validaciones)
└── main.py          # Punto de entrada
```

### Patrones de Diseño Implementados

- **Repository Pattern**: Abstracción de la persistencia de datos
- **Service Layer**: Lógica de negocio separada
- **Clean Architecture**: Separación de responsabilidades
- **Dependency Injection**: Inyección de dependencias en servicios
- **Data Transfer Objects**: Modelos de datos como dataclasses

## 🎯 Funcionalidades

### 📚 Gestión de Libros
- ✅ Agregar libro (título, autor, año)
- ✅ Listar todos los libros
- ✅ Buscar por título
- ✅ Buscar por autor
- ✅ Eliminar libro (solo si no está prestado)
- ✅ Ver estado (disponible/prestado)

### 👤 Gestión de Usuarios
- ✅ Registrar usuario (nombre, email)
- ✅ Listar usuarios
- ✅ Validar email único
- ✅ Validar datos de entrada

### 🔄 Gestión de Préstamos
- ✅ Prestar libro a usuario
- ✅ Devolver libro
- ✅ Evitar prestar libros ya prestados
- ✅ Ver préstamos activos
- ✅ Historial de préstamos
- ✅ Rastrear fechas de préstamo y devolución

### 📊 Estadísticas
- ✅ Total de libros disponibles/prestados
- ✅ Total de usuarios
- ✅ Resumen de préstamos activos y devueltos

### 💾 Persistencia
- ✅ Guardar en archivos JSON
- ✅ Cargar datos al iniciar
- ✅ Persistencia automática en cada operación

### 🛡️ Robustez
- ✅ Validaciones de entrada (email, año, caracteres mínimos)
- ✅ Manejo de excepciones (try/except)
- ✅ Mensajes claros al usuario
- ✅ Iconos emoji para mejor UX

## 🚀 Instalación y Uso

### Requisitos
- Python 3.7+
- No hay dependencias externas

### Ejecución

```bash
cd mini_proyecto
python app.py
```

## 📁 Estructura de Archivos

```
mini_proyecto/
├── app.py                          # Punto de entrada principal
├── README.md                       # Este archivo
├── src/
│   ├── __init__.py
│   ├── main.py                     # Inicialización del sistema
│   ├── domain/
│   │   ├── __init__.py
│   │   └── models.py               # Modelos: Libro, Usuario, Préstamo
│   ├── repository/
│   │   ├── __init__.py
│   │   ├── base_repository.py      # Clase base abstracta
│   │   ├── libro_repository.py     # Operaciones CRUD de libros
│   │   ├── usuario_repository.py   # Operaciones CRUD de usuarios
│   │   └── prestamo_repository.py  # Operaciones CRUD de préstamos
│   ├── service/
│   │   ├── __init__.py
│   │   ├── libro_service.py        # Lógica de negocio de libros
│   │   ├── usuario_service.py      # Lógica de negocio de usuarios
│   │   └── prestamo_service.py     # Lógica de negocio de préstamos
│   ├── ui/
│   │   ├── __init__.py
│   │   └── cli.py                  # Interfaz de línea de comandos
│   └── utils/
│       ├── __init__.py
│       └── validaciones.py         # Validaciones de entrada
└── data/                           # Carpeta de datos (creada automáticamente)
    ├── libros.json                 # Base de datos de libros
    ├── usuarios.json               # Base de datos de usuarios
    └── prestamos.json              # Base de datos de préstamos
```

## 🔄 Flujo de Operaciones

### Prestar un Libro
1. Usuario selecciona "Prestar libro"
2. Sistema valida que el libro existe
3. Sistema valida que el libro está disponible
4. Sistema valida que no hay otro préstamo activo
5. Se crea el préstamo
6. Se actualiza el estado del libro a "prestado"
7. Se guarda en JSON

### Devolver un Libro
1. Usuario selecciona "Devolver libro"
2. Sistema obtiene el préstamo activo
3. Sistema valida que aún no fue devuelto
4. Se marca el préstamo como "devuelto"
5. Se establece la fecha de devolución
6. Se actualiza el estado del libro a "disponible"
7. Se guarda en JSON

## ✨ Validaciones Implementadas

- **Email**: Formato válido (usuario@dominio.com)
- **Título**: Mínimo 3 caracteres
- **Autor**: Mínimo 3 caracteres
- **Año**: Número entre 1000 y 2100
- **Nombre usuario**: Mínimo 3 caracteres
- **Email único**: Evita duplicados
- **Integridad referencial**: No permite operaciones inválidas

## 📝 Ejemplo de Uso

```
1. Registrar usuario:
   - Nombre: Juan Pérez
   - Email: juan@example.com

2. Agregar libro:
   - Título: Don Quijote
   - Autor: Cervantes
   - Año: 1605

3. Prestar libro:
   - Seleccionar libro: Don Quijote
   - Seleccionar usuario: Juan Pérez
   - Se crea préstamo automáticamente

4. Devolver libro:
   - Seleccionar préstamo activo
   - Se marca como devuelto
   - Se registra fecha de devolución
```

## 🎨 Interfaz de Usuario

La CLI utiliza:
- Menús claros con bordes ASCII
- Iconos emoji para mejor visualización
- Tablas formateadas para listar datos
- Mensajes de éxito/error diferenciados
- Navegación intuitiva con opciones numeradas

## 📊 Archivos JSON

### libros.json
```json
[
  {
    "id": "a1b2c3d4",
    "titulo": "Don Quijote",
    "autor": "Miguel de Cervantes",
    "año": 1605,
    "estado": "disponible",
    "fecha_creacion": "2026-02-04T..."
  }
]
```

### usuarios.json
```json
[
  {
    "id": "e5f6g7h8",
    "nombre": "Juan Pérez",
    "email": "juan@example.com",
    "fecha_registro": "2026-02-04T..."
  }
]
```

### prestamos.json
```json
[
  {
    "id": "i9j0k1l2",
    "libro_id": "a1b2c3d4",
    "usuario_id": "e5f6g7h8",
    "fecha_prestamo": "2026-02-04T...",
    "fecha_devolucion": null,
    "estado": "activo"
  }
]
```

## 🐛 Manejo de Errores

Todos los errores son capturados y manejados con mensajes claros:

- Entrada inválida → Validación en tiempo de entrada
- Archivo no encontrado → Creación automática
- Operación no permitida → Mensaje descriptivo
- Excepciones inesperadas → Captura con traceback

## 🔐 Seguridad y Validaciones

- Validaciones antes de guardar en BD
- Prevención de duplicados (emails)
- Integridad referencial en préstamos
- No permite eliminar libros prestados
- No permite prestar libros no disponibles

## 🚀 Mejoras Futuras Posibles

- Base de datos relacional (SQLite/PostgreSQL)
- Autenticación de usuarios
- Generación de reportes PDF
- Interfaz gráfica (Tkinter/PyQt)
- API REST (Flask/FastAPI)
- Sistema de multas por retrasos
- Notificaciones por email
- Tests unitarios y de integración

## 📄 Licencia

Proyecto educativo - Uso libre

## 👨‍💻 Autor
Gian Carlos Q
Sistema de Gestión de Biblioteca - Arquitectura Limpia en Python
