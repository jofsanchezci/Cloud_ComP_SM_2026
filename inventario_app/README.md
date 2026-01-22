# Inventario Electrónicos - Aplicación Web

Este proyecto es una aplicación web para gestionar el inventario de una tienda de productos electrónicos. Permite la gestión en **tiempo real** del inventario usando **Flask** y **SocketIO**, además de funcionalidades completas CRUD y carga masiva de productos desde archivos de texto.

## 📦 Características

- Visualización del inventario en tiempo real (WebSocket)
- Operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
- Carga masiva de productos desde archivos `.txt`
- Cálculo automático del precio con IVA (19%)

## 🛠️ Tecnologías utilizadas

- Python 3
- Flask
- Flask-SocketIO
- SQLite
- HTML, CSS y JavaScript

## 🗃️ Estructura del proyecto

```
inventario_app/
├── app.py                  # Aplicación principal Flask
├── templates/
│   ├── index.html          # Página principal
│   └── editar.html         # Formulario de edición
├── static/                 # Archivos estáticos (CSS, JS)
├── inventario.db           # Base de datos SQLite (se genera automáticamente)
```

## 🚀 Instrucciones de uso

1. Clona o descomprime el proyecto.
2. Instala las dependencias necesarias:

```bash
pip install flask flask-socketio eventlet
```

3. Ejecuta la aplicación:

```bash
python app.py
```

4. Abre tu navegador y accede a:

```
http://localhost:5000
```

## 📁 Formato de archivo de carga masiva (`.txt`)

El archivo debe tener el siguiente formato:

```
ID,Nombre,CantidadActual,Precio,CantidadFutura
1,Monitor 24",15,450000,10
2,Audífonos Bluetooth,20,95000,5
```

## 📋 Notas

- La base de datos se crea automáticamente al ejecutar el proyecto.
- El precio con IVA se calcula como `precio * 1.19` y se muestra en la tabla.
- Los cambios se sincronizan en tiempo real entre todos los clientes conectados.

---

Desarrollado por ChatGPT para uso educativo y de pruebas.
