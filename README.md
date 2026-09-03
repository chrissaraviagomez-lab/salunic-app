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
├── main.py                    # Archivo principal de la aplicación / controlador de pantallas
├── requirements.txt           # Dependencias del proyecto
├── .gitignore                 # Archivos a ignorar en Git
├── README.md                  # Este archivo
├── shoot.py                   # Utilidad de captura de pantalla para desarrollo
├── DIAGRAMAS.md               # Documentación de Diagramas de Flujo de Datos (DFD)
├── diagramas_img/             # Imágenes de los DFD del proyecto (DFD_Documento_1..4.png)
├── generar_dfd_svg.py         # Generador de los PNG de los DFD (con Pillow)
├── salunic-defensa.docx       # Guía de estudio para la defensa en grupo (5 integrantes)
├── nombre_proyecto_integrador_grupo#8/  # Prototipo por consola (1er corte - Programación Estructurada)
│   ├── main.py                # Menú consola (24 opciones) + datos iniciales
│   ├── entidades.py           # @dataclass: Usuario, CitaMedica, Medicamento, AlmacenMedicamento
│   ├── datos.py               # Listas (usuarios, citas, medicamentos, almacen) + inventario inicial
│   └── funciones.py           # Validaciones + CRUD completo + manejo de errores
├── data/                      # Módulo de datos del usuario
│   ├── __init__.py
│   └── users_data.py          # Persistencia de usuarios (JSON)
└── screens/                   # Módulo de pantallas
    ├── __init__.py
    ├── styles.py              # Colores, dimensiones y helpers de UI (create_rounded_rect, gradiente)
    ├── splash_screen.py       # Pantalla de inicio animada
    ├── inicio_screen.py       # Pantalla de bienvenida (Estado 2 - tarjeta sobre gradiente)
    ├── login_screen.py        # Pantalla de inicio de sesión
    ├── registro_screen.py     # Pantalla de registro de usuario
    ├── home_screen.py         # Dashboard principal (scroll + footer de navegación)
    ├── citas_screen.py        # Lista de citas médicas
    ├── historial_screen.py    # Historial médico
    ├── medicamentos_screen.py # Lista de medicamentos / tomas de hoy
    ├── estadisticas_screen.py # Estadísticas de salud
    ├── forms/                 # Formularios
    │   ├── __init__.py
    │   ├── form_registro.py   # Editar Perfil (campo por campo sobre gradiente)
    │   └── form_medicamento.py# Agregar Medicamento
    └── password_reset/        # Recuperación de contraseña
        ├── __init__.py
        └── screen_2_otp.py    # Verificación de código OTP
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
- Menú inferior de navegación (Inicio / Estadísticas / Perfil / Salir)

### 6. Citas
- Lista de citas médicas como tarjetas individuales sobre el gradiente
- Botón "VOLVER AL INICIO"

### 7. Historial
- Registros médicos como tarjetas individuales sobre el gradiente
- Botón "VOLVER AL INICIO"

### 8. Medicamentos
- Lista de "tomas de hoy" como tarjetas sobre el gradiente
- Botón "AGREGAR MEDICAMENTO" que lleva al formulario

### 9. Estadísticas de Salud
- Resumen de temperatura, pulso, presión y citas
- Tarjetas individuales sobre el gradiente

### 10. Editar Perfil (FormRegistro)
- Formulario de campos individuales sobre el gradiente
- Pre-rellena los datos del usuario actual

### 11. Agregar Medicamento (FormMedicamento)
- Formulario de medicamentos sobre el gradiente

### 12. Recuperar Contraseña (OTP)
- Verificación de código de 6 dígitos
- Campo sobre tarjeta redondeada

## 🎯 Credenciales de Prueba

- **Email**: usuario@salunic.com
- **Contraseña**: 123456

## 🛠️ Desarrollo

### Colores Utilizados
- Verde: #2ECC71
- Fucsia: #E91E8C
- Rosado: #F48FB1
- Azul: #1565C0 (azul primario)
- Celeste: #4FC3F7
- Amarillo (ámbar): #F9A825
- Naranja: #FF7043
- Blanco: #FFFFFF
- Azul Noche (fondo): #0A2342
- Texto oscuro: #333333 / gris: #777777 / claro: #999999
- Gradiente de fondo: #0A2342 → #0D3B7A → #0A4D2E → #062A1A

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
