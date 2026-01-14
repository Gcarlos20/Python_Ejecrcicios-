# Gestor de Estudiantes

## Descripción
Aplicación de consola para gestionar información de estudiantes. Permite agregar, eliminar, mostrar estudiantes y calcular promedios de calificaciones.

## Funcionalidades

### 1. Agregar Estudiante
Permite registrar un nuevo estudiante con sus datos básicos:
- Nombre
- Apellido
- Edad
- Promedio

### 2. Eliminar Estudiante
Permite eliminar un estudiante existente de la base de datos proporcionando sus datos.

### 3. Mostrar Estudiantes
Muestra el listado completo de todos los estudiantes registrados en el sistema.

### 4. Mostrar Promedio
Muestra el promedio general de todos los estudiantes.

### 5. Calcular Promedio
Calcula el promedio de notas de un estudiante a partir de 5 calificaciones ingresadas manualmente.

### 6. Salir
Cierra la aplicación.

## Estructura del Proyecto

```
Gestor_de_Estudiantes/
├── src/
│   ├── main.py          # Archivo principal con el menú y lógica principal
│   ├── funcione.py      # Módulo con las funciones de gestión
│   └── readme.md        # Este archivo
```

## Requisitos

- Python 3.6 o superior

## Instalación

No requiere instalación de dependencias externas. Solo necesita Python instalado en el sistema.

## Uso

Para ejecutar la aplicación:

```bash
python3 src/main.py
```

Luego sigue el menú interactivo para seleccionar las opciones deseadas.

## Archivos Principales

### main.py
Contiene:
- Función `menu()`: Muestra el menú inicial de bienvenida
- Función `main()`: Función principal que controla el flujo de la aplicación
- Bloque `if __name__ == "__main__"`: Punto de entrada de la aplicación

### funcione.py
Contiene las siguientes funciones:
- `agregar_estudiante()`: Agrega un nuevo estudiante
- `eliminar_estudiante()`: Elimina un estudiante
- `mostrar_estudiantes()`: Muestra todos los estudiantes
- `mostrar_estudiante2()`: Versión alternativa para mostrar estudiantes
- `calcular_promedio()`: Calcula el promedio de notas
- `mostrar_promedio()`: Muestra el promedio calculado

## Notas Técnicas

- Los estudiantes se almacenan en una lista (`estudiantes = []`)
- Las notas se almacenan en una lista separada (`notas = []`)
- El programa funciona en un bucle infinito hasta que el usuario selecciona la opción 6 (Salir)

## Autor
Creado por [Carlos Quintero]
Creado como ejercicio de gestión de estudiantes


## Licencia
Uso libre

