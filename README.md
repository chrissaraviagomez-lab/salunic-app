# SALUNIC - Salud y Bienestar Nicaragua

Aplicación de salud y bienestar desarrollada con Python y Tkinter.

## 🚀 Características

- **Splash Screen**: Pantalla de inicio animada
- **Autenticación**: Sistema de login y registro de usuarios
- **Panel de Control**: Interfaz principal con datos vitales
- **Servicios Principales**: Citas médicas, medicamentos, historial médico y perfil
- **Próximas Citas**: Visualización de citas programadas
- **Menú Navegación**: Acceso rápido a todas las secciones

## 📋 Requisitos

- Python 3.6 o superior
- Tkinter (incluido por defecto en Python)

## 💻 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/chrissaraviagomez-lab/salunic-app.git
cd salunic-app
```

2. Instala las dependencias (opcional):
```bash
pip install -r requirements.txt
```

## ▶️ Ejecución

Ejecuta la aplicación:
```bash
python main.py
```

## 📁 Estructura del Proyecto

```
salunic-app/
├── main.py                    # Archivo principal de la aplicación
├── requirements.txt           # Dependencias del proyecto
├── .gitignore                 # Archivos a ignorar en Git
├── README.md                  # Este archivo
└── screens/                   # Módulo de pantallas
    ├── __init__.py
    ├── splash_screen.py       # Pantalla de inicio animada
    ├── inicio_screen.py       # Pantalla de bienvenida
    ├── login_screen.py        # Pantalla de inicio de sesión
    ├── registro_screen.py     # Pantalla de registro de usuario
    └── home_screen.py         # Pantalla principal del dashboard
```

## 🎨 Pantallas

### 1. Splash Screen
- Animación de círculos rotativos
- Duración: 3 segundos
- Transición automática a la pantalla de inicio

### 2. Inicio
- Bienvenida al usuario
- Botones para comenzar o iniciar sesión
- Interfaz intuitiva

### 3. Login
- Inicio de sesión con email y contraseña
- Enlace para registrar nueva cuenta
- Validación de campos

### 4. Registro
- Formulario para crear nueva cuenta
- Confirmación de contraseña
- Validación de datos

### 5. Home (Panel de Control)
- Datos vitales: Temperatura, Pulso, Citas, Medicinas
- Avatar del usuario
- Servicios principales: Citas, Medicamentos, Historial, Perfil
- Próximas citas con detalles del médico
- Menú inferior de navegación

## 🎯 Credenciales de Prueba

- **Email**: usuario@salunic.com
- **Contraseña**: 123456

## 🛠️ Desarrollo

### Colores Utilizados
- Azul Primario: #1565c0
- Verde Secundario: #2ecc71
- Rojo Alertas: #e74c3c
- Blanco: #ffffff
- Gris Fondo: #f5f5f5

### Fuentes
- Font: Nunito (requiere instalación del sistema o uso de fuentes predeterminadas)

## 📝 Notas

- La aplicación está diseñada para una resolución de 375x812 (móvil simulado)
- Todas las pantallas utilizan el framework Tkinter
- Los datos son demostrativo, sin conexión a base de datos real

## 📞 Soporte

Para reportar errores o sugerencias, crea un issue en el repositorio.

## 📄 Licencia

Este proyecto está bajo licencia MIT.

---

**Desarrollado por**: chrissaraviagomez-lab
**Última actualización**: Junio 2026
