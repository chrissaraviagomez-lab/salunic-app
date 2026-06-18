# 🏥 SALUNIC - Salud y Bienestar Nicaragua

Una aplicación de salud integral diseñada para facilitar el acceso a servicios médicos, gestión de medicamentos y bienestar en Nicaragua.

## 📱 Características principales

### 🎯 Pantallas principales

- **Splash Screen**: Pantalla de carga inicial con animación
- **Inicio (Inicio Screen)**: Bienvenida e información principal
- **Home**: Panel de control con estadísticas de salud
- **Formularios**:
  - 📋 Registro de usuario
  - 📅 Reserva de citas médicas
  - 💊 Gestión de medicamentos

### 🔐 Recuperación de contraseña

- **Pantalla 1**: Ingreso de correo electrónico
- **Pantalla 2**: Verificación OTP (One-Time Password)
- **Pantalla 3**: Creación de nueva contraseña

## 🛠️ Tecnologías utilizadas

- **Python 3.x**
- **Tkinter**: Interfaz gráfica
- **Canvas**: Dibujo de componentes visuales

## 📁 Estructura del proyecto

```
salunic-app/
├── main.py                          # Archivo principal
├── README.md                        # Este archivo
└── screens/
    ├── __init__.py
    ├── splash_screen.py             # Pantalla de carga
    ├── inicio_screen.py             # Pantalla de inicio
    ├── home_screen.py               # Panel de control
    ├── password_reset/
    │   ├── __init__.py
    │   ├── screen_1_email.py        # Recuperación paso 1
    │   ├── screen_2_otp.py          # Recuperación paso 2
    │   └── screen_3_password.py     # Recuperación paso 3
    └── forms/
        ├── __init__.py
        ├── form_registro.py         # Formulario de registro
        ├── form_cita.py             # Formulario de cita médica
        └── form_medicamento.py      # Formulario de medicamentos
```

## 🚀 Instalación

### Requisitos previos
- Python 3.6 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/chrissaraviagomez-lab/salunic-app.git
   cd salunic-app
   ```

2. **Crea un entorno virtual** (opcional pero recomendado)
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En Mac/Linux
   source venv/bin/activate
   ```

3. **Ejecuta la aplicación**
   ```bash
   python main.py
   ```

## 📱 Dimensiones de la interfaz

- **Ancho**: 375px (Tamaño móvil estándar)
- **Alto**: 812px (iPhone X+)
- **Colores principales**:
  - Verde: `#2ecc71` (Botones, acciones)
  - Azul: `#1565c0` (Headers)
  - Blanco: `#ffffff` (Fondo)
  - Rosa: `#e91e8c` (Acentos)

## 🎨 Componentes visuales

### Pantalla Splash
- Logo animado de SALUNIC
- Barra de carga progresiva
- Información de versión

### Pantalla Inicio
- Cartas de características principales
- Botones de acción (Comenzar, Iniciar sesión)
- Indicadores visuales

### Home Screen
- Estadísticas de salud (temperatura, pulso, citas, medicamentos)
- Servicios principales (Citas, Medicamentos, Historial, Perfil)
- Próximas citas médicas
- Recordatorio de medicamentos

### Formularios
- Validación de campos
- Indicadores de progreso
- Instrucciones claras para el usuario

## 🔄 Flujo de la aplicación

```
Splash Screen → Inicio Screen → Login Screen → Form Registro → Home Screen
```

## 📋 Requisitos de usuario

### Usuarios
- Crear cuenta con información personal
- Recuperar contraseña olvidada
- Ver estadísticas de salud
- Reservar citas médicas
- Gestionar medicamentos
- Recibir recordatorios de medicamentos

## 🔒 Seguridad

- Validación de OTP (One-Time Password)
- Requisitos de contraseña fuerte
- Información de usuario protegida

## 🌐 Información de contacto

**Proyecto**: Salunic - Salud y Bienestar Nicaragua
**Autor**: chrissaraviagomez-lab
**Año**: 2026
**Repositorio**: https://github.com/chrissaraviagomez-lab/salunic-app

## 📝 Notas de desarrollo

### Próximas mejoras
- Integración con API de backend
- Autenticación con Firebase
- Base de datos local SQLite
- Envío de notificaciones push
- Interfaz de historial médico completo
- Integración de mapas para ubicar centros médicos

### Consideraciones técnicas
- Todas las pantallas utilizan Canvas de Tkinter para mayor flexibilidad visual
- Los colores utilizan notación HEX
- Las fuentes utilizan "Nunito" como familia principal
- Responsive design basado en proporciones

## 📄 Licencia

Este proyecto es parte de un trabajo académico de la UNAN Managua.

---

**Estado**: En desarrollo 🚧

**Última actualización**: Junio 17, 2026
