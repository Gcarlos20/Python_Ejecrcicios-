# Lista de Tareas

Una aplicación de escritorio simple para gestionar tareas pendientes, desarrollada en Java con interfaz gráfica Swing.

## 📋 Descripción

Esta aplicación permite crear, visualizar, marcar como completadas y eliminar tareas de una lista. Cada tarea tiene una descripción, fecha y estado de completado. La interfaz gráfica facilita la interacción con la lista de tareas de manera intuitiva.

## ✨ Características

- ✅ Agregar nuevas tareas con descripción y fecha
- 📝 Visualizar lista de tareas con estado de completado
- ✔️ Marcar tareas como completadas
- 🗑️ Eliminar tareas de la lista
- 🎨 Interfaz gráfica intuitiva con Java Swing
- 📅 Información de fecha para cada tarea

## 🛠️ Tecnologías Utilizadas

- **Java**: Lenguaje de programación principal
- **Swing**: Framework para la interfaz gráfica de usuario
- **JOptionPane**: Para diálogos de entrada de datos

## 📋 Requisitos

- Java Development Kit (JDK) 8 o superior
- Entorno de desarrollo Java (opcional, para modificar el código)

## 🚀 Instalación y Ejecución

### Opción 1: Ejecutar directamente

1. Asegúrate de tener Java instalado en tu sistema
2. Navega al directorio del proyecto
3. Compila los archivos Java:
   ```bash
   javac src/*.java
   ```
4. Ejecuta la aplicación:
   ```bash
   java -cp src Main
   ```

### Opción 2: Usando un IDE

1. Abre el proyecto en tu IDE Java favorito (Eclipse, IntelliJ IDEA, NetBeans, VS Code)
2. Ejecuta la clase `Main.java` como aplicación Java

## 📖 Uso

### Agregar una tarea:
1. Haz clic en el botón "Agregar"
2. Ingresa la descripción de la tarea
3. Ingresa la fecha de la tarea
4. La tarea se agregará a la lista

### Marcar como completada:
1. Selecciona una tarea de la lista
2. Haz clic en el botón "Completar"
3. La tarea se marcará con un check (✔)

### Eliminar una tarea:
1. Selecciona una tarea de la lista
2. Haz clic en el botón "Eliminar"
3. La tarea se removerá de la lista

### Cancelar/Salir:
- "Cancelar": Cierra la ventana actual
- "Salir": Cierra la aplicación completa

## 📁 Estructura del Proyecto

```
ListaDeTraeas/
├── README.md              # Este archivo
└── src/
    ├── Main.java          # Clase principal con la interfaz gráfica
    └── Tarea.java         # Clase que representa una tarea
```

## 🔧 Clases Principales

### Tarea.java
- Representa una tarea individual
- Atributos: descripción, fecha, estado de completado
- Métodos: getters, setters y toString() personalizado

### Main.java
- Clase principal que contiene la interfaz gráfica
- Gestiona la lista de tareas usando ArrayList y DefaultListModel
- Maneja los eventos de los botones

## 🤝 Contribución

Si deseas contribuir al proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request


## 👨‍💻 Autor

Carlos Quinterp 

---

¡Gracias por usar Lista de Tareas! 🎉