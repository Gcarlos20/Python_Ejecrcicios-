# 🚀 Guía Rápida de Inicio

## Instalación y Primera Ejecución

### Paso 1: Navegar al Proyecto
```bash
cd d:\Escritorio\mini_proyecto
```

### Paso 2: Verificar Python
```bash
python --version
```
Requiere Python 3.7 o superior.

### Paso 3: Opción A - Ejecutar Vacío
```bash
python app.py
```
El sistema creará automáticamente las carpetas y archivos JSON necesarios.

### Paso 3: Opción B - Ejecutar con Datos de Ejemplo
```bash
python cargar_ejemplo.py
python app.py
```

---

## 📖 Primer Uso

### Menú Principal

```
60 ============================================================
  📚 SISTEMA DE GESTIÓN DE BIBLIOTECA 📚
  ============================================================

┌─ MENÚ PRINCIPAL ─────────────────────────────────────┐
│                                                      │
│  1. 📖 Gestionar Libros                              │
│  2. 👤 Gestionar Usuarios                            │
│  3. 🔄 Gestionar Préstamos                           │
│  4. 📊 Ver Estadísticas                              │
│  5. 🚪 Salir                                         │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### Operaciones Básicas

#### 1️⃣ Agregar un Libro
```
Seleccione una opción: 1
Seleccione una opción: 1

➕ AGREGAR NUEVO LIBRO
--------------------------------------------------
Título: Don Quijote
Autor: Miguel de Cervantes
Año de publicación: 1605

✅ Libro 'Don Quijote' agregado exitosamente (ID: a1b2c3d4)
```

#### 2️⃣ Registrar un Usuario
```
Seleccione una opción: 2
Seleccione una opción: 1

➕ REGISTRAR NUEVO USUARIO
--------------------------------------------------
Nombre: Juan Pérez
Email: juan@example.com

✅ Usuario 'Juan Pérez' registrado exitosamente (ID: e5f6g7h8)
```

#### 3️⃣ Prestar un Libro
```
Seleccione una opción: 3
Seleccione una opción: 1

📤 PRESTAR LIBRO
--------------------------------------------------

📚 Libros disponibles:
  a1b2c3d4: Don Quijote - Miguel de Cervantes

Ingrese ID del libro: a1b2c3d4

👤 Usuarios registrados:
  e5f6g7h8: Juan Pérez

Ingrese ID del usuario: e5f6g7h8

✅ Libro 'Don Quijote' prestado exitosamente (Préstamo ID: p1q2r3s4)
```

#### 4️⃣ Devolver un Libro
```
Seleccione una opción: 3
Seleccione una opción: 2

📥 DEVOLVER LIBRO
--------------------------------------------------

📋 Préstamos activos:
  p1q2r3s4: Don Quijote → Juan Pérez

Ingrese ID del préstamo a devolver: p1q2r3s4

✅ Libro 'Don Quijote' devuelto correctamente
```

#### 5️⃣ Ver Estadísticas
```
Seleccione una opción: 4

📊 ESTADÍSTICAS DEL SISTEMA
============================================================
📚 Total de libros: 10
   ✅ Disponibles: 8
   🔴 Prestados: 2

👤 Total de usuarios: 5

🔄 Total de préstamos: 5
   🔴 Préstamos activos: 2
   ✅ Préstamos devueltos: 3
============================================================
```

---

## 🗂️ Estructura de Archivos Generada

Después de ejecutar:

```
mini_proyecto/
├── app.py                          # Ejecutable
├── cargar_ejemplo.py               # Script de ejemplo
├── README.md                       # Documentación general
├── ARQUITECTURA.md                 # Documentación técnica
├── INICIO_RAPIDO.md                # Este archivo
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── domain/
│   │   ├── __init__.py
│   │   └── models.py               # Modelos
│   ├── repository/
│   │   ├── __init__.py
│   │   ├── base_repository.py
│   │   ├── libro_repository.py
│   │   ├── usuario_repository.py
│   │   └── prestamo_repository.py
│   ├── service/
│   │   ├── __init__.py
│   │   ├── libro_service.py
│   │   ├── usuario_service.py
│   │   └── prestamo_service.py
│   ├── ui/
│   │   ├── __init__.py
│   │   └── cli.py                  # Interfaz
│   └── utils/
│       ├── __init__.py
│       └── validaciones.py
└── data/                           # CREADO AUTOMÁTICAMENTE
    ├── libros.json                 # Base de datos
    ├── usuarios.json
    └── prestamos.json
```

---

## ⚠️ Errores Comunes y Soluciones

### Error: "ModuleNotFoundError"
```
Solución:
- Asegúrate de estar en el directorio: d:\Escritorio\mini_proyecto
- Verifica que existe la carpeta 'src'
- Intenta: python -c "import sys; sys.path.insert(0, '.'); from src.main import main"
```

### Error: "No hay libros registrados"
```
Solución:
- Ejecuta: python cargar_ejemplo.py
- Luego: python app.py
```

### Error de permisos al crear archivos
```
Solución:
- Verifica que tienes permisos de escritura en D:\Escritorio\mini_proyecto
- Intenta ejecutar PowerShell como Administrador
```

### Los datos no se guardan
```
Posibles causas:
- Revisa que la carpeta 'data' fue creada
- Verifica permisos de escritura
- Comprueba el espacio en disco
```

---

## 🎮 Casos de Uso Completos

### Caso 1: Ciclo Completo de Préstamo

**Paso 1**: Agregar libro
- Menú → 1 (Libros) → 1 (Agregar)
- Ingresa: "Python 3.9", "Guido van Rossum", "2020"

**Paso 2**: Registrar usuario
- Menú → 2 (Usuarios) → 1 (Registrar)
- Ingresa: "María López", "maria@email.com"

**Paso 3**: Prestar libro
- Menú → 3 (Préstamos) → 1 (Prestar)
- Selecciona el libro y usuario

**Paso 4**: Verificar en estadísticas
- Menú → 4 (Estadísticas)
- Verás 1 libro prestado, 1 préstamo activo

**Paso 5**: Devolver libro
- Menú → 3 (Préstamos) → 2 (Devolver)
- Confirma el préstamo

**Resultado**: Libro vuelve a estar disponible

### Caso 2: Búsqueda de Libros

**Opción A - Por Título**:
- Menú → 1 (Libros) → 3 (Buscar por título)
- Ingresa: "Python" (búsqueda parcial funciona)

**Opción B - Por Autor**:
- Menú → 1 (Libros) → 4 (Buscar por autor)
- Ingresa: "Guido" (búsqueda parcial funciona)

### Caso 3: Ver Historial Completo

- Menú → 3 (Préstamos) → 4 (Historial)
- Muestra todos los préstamos (activos y devueltos)
- Incluye fechas de préstamo y devolución

---

## 📊 Datos Persistidos

### libros.json
```json
[
  {
    "id": "a1b2c3d4",
    "titulo": "Don Quijote",
    "autor": "Miguel de Cervantes",
    "año": 1605,
    "estado": "disponible",
    "fecha_creacion": "2026-02-04T19:30:45.123456"
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
    "fecha_registro": "2026-02-04T19:30:46.234567"
  }
]
```

### prestamos.json
```json
[
  {
    "id": "p1q2r3s4",
    "libro_id": "a1b2c3d4",
    "usuario_id": "e5f6g7h8",
    "fecha_prestamo": "2026-02-04T19:30:47.345678",
    "fecha_devolucion": "2026-02-05T10:15:00.456789",
    "estado": "devuelto"
  }
]
```

---

## 🔍 Validaciones en Acción

### ✅ Email Válido
```
Email: usuario@dominio.com
✅ Aceptado
```

### ❌ Email Inválido
```
Email: usuario@invalido
❌ Email inválido. Use formato: usuario@dominio.com
```

### ✅ Título Válido
```
Título: Python Programming
✅ Aceptado
```

### ❌ Título Muy Corto
```
Título: Py
❌ El título debe tener al menos 3 caracteres
```

### ✅ Año Válido
```
Año: 2020
✅ Aceptado
```

### ❌ Año Inválido
```
Año: 3000
❌ El año debe estar entre 1000 y 2100
```

---

## 💡 Tips y Trucos

1. **Busca parcial**: En búsquedas de título/autor, solo escribe una parte
   - "Quijo" encontrará "Don Quijote"
   - "Cerv" encontrará "Miguel de Cervantes"

2. **Vuelve al menú anterior**: Selecciona la opción más alta + 1
   - Generalmente es la opción "6" o "3"

3. **Ver IDs rápido**: Usa las operaciones "Listar"
   - Los IDs necesarios están en la primera columna

4. **Datos persistentes**: Cierra y abre el programa
   - Todos los datos se mantienen
   - Están en archivos JSON en la carpeta `data/`

---

## 🆘 Necesitas Ayuda?

1. **Revisa** [README.md](README.md) - Documentación general
2. **Consulta** [ARQUITECTURA.md](ARQUITECTURA.md) - Detalles técnicos
3. **Verifica** los mensajes de error del sistema
4. **Revisa** el código en `src/service/` para entender validaciones

---

**¡Que disfrutes usando el Sistema de Gestión de Biblioteca! 📚**
