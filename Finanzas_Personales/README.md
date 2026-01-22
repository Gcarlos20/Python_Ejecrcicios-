# Sistema de Finanzas Personales

Un sistema simple de gestión de finanzas personales desarrollado en Python. Permite a los usuarios agregar ingresos y gastos, ver transacciones y obtener un resumen financiero básico.

## Características

- **Gestión de usuarios**: Crear un perfil de usuario.
- **Agregar transacciones**: Ingresos y gastos con categorías.
- **Visualización**: Mostrar lista de transacciones y resumen financiero (ingresos, gastos y balance).
- **Interfaz de consola**: Menú interactivo en la terminal.

## Estructura del Proyecto

```
Finanzas_Personales/
├── models/
│   ├── usuario.py          # Clase Usuario
│   └── transacciones.py    # Clase Transaccion
├── service/
│   └── gestor.py           # Clase GestorFinanzas
├── main.py                 # Script principal con menú interactivo
└── README.md               # Este archivo
```

## Requisitos

- Python 3.6 o superior (usa solo bibliotecas estándar, como `datetime`).

## Instalación

1. Clona o descarga el proyecto en tu máquina.
2. Asegúrate de tener Python instalado.
3. Navega al directorio del proyecto:
   ```
   cd /ruta/a/Finanzas_Personales
   ```

## Uso

1. Ejecuta el script principal:
   ```
   python3 main.py
   ```

2. Sigue las instrucciones en pantalla:
   - Ingresa tu nombre.
   - Selecciona opciones del menú:
     - 1: Agregar ingreso.
     - 2: Agregar gasto.
     - 3: Mostrar transacciones.
     - 4: Mostrar resumen financiero.
     - 5: Salir.

### Ejemplo de uso

```
Ingrese su nombre: Carlos

--- Sistema de Finanzas Personales ---
1. Agregar ingreso
2. Agregar gasto
3. Mostrar transacciones
4. Mostrar resumen
5. Salir
Seleccione una opción: 1
Monto del ingreso: 1000
Categoría: Salario
Ingreso agregado correctamente.
```

## Clases Principales

- **Usuario**: Representa a un usuario con nombre y listas de transacciones.
- **Transaccion**: Representa una transacción con tipo, monto, categoría y fecha.
- **GestorFinanzas**: Gestiona las operaciones del usuario, como agregar transacciones y calcular totales.

## Contribución

Si quieres contribuir:
1. Haz un fork del proyecto.
2. Crea una rama para tu feature.
3. Envía un pull request.

## Licencia

Este proyecto es de código abierto. Úsalo bajo tu propio riesgo.

## Autor

Desarrollado por Carlos Quintero