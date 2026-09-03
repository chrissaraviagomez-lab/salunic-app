# Diagramas de Flujo de Datos (DFD) - SALUNIC

> Prototipo de consola - 1er corte evolutivo - Grupo 8
> Programacion Estructurada - II Semestre 2026

Este documento describe los Diagramas de Flujo de Datos (DFD) de SALUNIC,
correspondientes al **prototipo de consola** que se desarrolla durante el 1er corte.

Las imagenes generadas se encuentran en la carpeta `diagramas_img/`:

| Archivo | Descripcion |
|---------|-------------|
| `DFD_Documento_1.png` | Nivel 0 (contexto) + Nivel 1 (procesos principales) |
| `DFD_Documento_2.png` | Nivel 2: P1 Usuarios + P2 Citas medicas |
| `DFD_Documento_3.png` | Nivel 2: P3 Medicamentos + P4 Almacen/Inventario |
| `DFD_Documento_4.png` | Modelo de entidades @dataclass y operaciones CRUD |

> Para regenerar las imagenes: `python generar_dfd_svg.py`
> (usa Pillow, no requiere librerias externas adicionales).

---

## Entidades del sistema

El sistema usa 4 entidades definidas con `@dataclass` en `entidades.py`:

| Entidad | Campos | Lista (datos.py) |
|---------|--------|------------------|
| `Usuario` | id, nombre, email, password, telefono | `usuarios = []` |
| `CitaMedica` | id, paciente_id, medico_id, especialidad, fecha, hora, lugar | `citas = []` |
| `Medicamento` | id, nombre, dosis, frecuencia, presentacion | `medicamentos = []` |
| `AlmacenMedicamento` | id, medicamento_id, cantidad, fecha_vencimiento | `almacen = []` |

### Relacion entre entidades

- `AlmacenMedicamento.medicamento_id` se relaciona con `Medicamento.id`:
  cada registro del almacen indica el medicamento al que corresponde su stock.
- `CitaMedica.paciente_id` y `CitaMedica.medico_id` se relacionan con `Usuario.id`.

---

## Nivel 0 - Diagrama de contexto

```
                      ┌─────────────────────┐
                      │      USUARIO        │
                      └──────────┬──────────┘
                                 │
                        datos, opciones
                                 │
                                 ▼
                      ┌─────────────────────┐
                      │       SALUNIC       │
                      │  Sistema de Salud   │
                      │  (consola / texto)  │
                      └──────────┬──────────┘
                                 │
                      resultados, mensajes
                                 │
                                 ▼
                      ┌─────────────────────┐
                      │       ADMIN         │
                      └─────────────────────┘
```

| Flujo | Origen | Destino | Datos |
|-------|--------|---------|-------|
| F1 | Usuario | SALUNIC | Datos de las entidades, opciones del menu |
| F2 | SALUNIC | Usuario | Resultados, mensajes de exito o error |
| F3 | Admin | SALUNIC | Gestion de datos del sistema |
| F4 | SALUNIC | Admin | Respuesta / confirmacion |

---

## Nivel 1 - Procesos principales

| Proceso | Nombre | Operaciones (CRUD) |
|---------|--------|--------------------|
| P1 | Gestion de Usuarios | registrar, buscar, actualizar, eliminar, contar, listar |
| P2 | Gestion de Citas Medicas | registrar, buscar, actualizar, eliminar, contar, listar |
| P3 | Gestion de Medicamentos | registrar, buscar, actualizar, eliminar, contar, listar |
| P4 | Gestion de Almacen / Inventario | registrar stock, buscar, actualizar, eliminar, contar, listar |

Los 4 procesos escriben y leen de un Almacen de Datos unico que contiene las
listas: `usuarios`, `citas`, `medicamentos` y `almacen`.

---

## Nivel 2 - Detalle de cada proceso

### P1. Gestion de Usuarios

1. **1.1 Ingresar datos**: nombre, email, password, telefono.
2. **1.2 Validar datos**: nombre solo letras/espacios; email con formato valido;
   password minimo 4 caracteres; telefono solo digitos. (Manejo de errores.)
3. **1.3 Agregar a la lista**: se asigna un id unico (`max + 1`) y se hace
   `usuarios.append(Usuario(...))`.
4. **1.4 Buscar / Actualizar / Eliminar**: por email (usar `buscar_usuario`).

### P2. Gestion de Citas Medicas

1. **2.1 Ingresar datos**: paciente_id, medico_id, especialidad, fecha, hora, lugar.
2. **2.2 Validar datos**: fecha real DD/MM/AAAA; hora HH:MM.
3. **2.3 Agregar a la lista**: `citas.append(CitaMedica(...))`.
4. **2.4 Buscar / Actualizar / Eliminar**: por `medico_id`.

### P3. Gestion de Medicamentos

1. **3.1 Ingresar datos**: nombre, dosis, frecuencia, presentacion.
2. **3.2 Validar datos**: nombre letras; dosis no vacia; frecuencia texto.
3. **3.3 Agregar a la lista**: `medicamentos.append(Medicamento(...))`.
4. **3.4 Buscar / Actualizar / Eliminar**: por nombre.

> El inventario inicial se carga con medicamentos reales de la Lista Basica de
> Medicamentos Esenciales del MINSA (Paracetamol, Ibuprofeno, Amoxicilina,
> Omeprazol, Metformina, Losartan, Ciprofloxacina, etc.), como los disponibles
> en el Hospital Fernando Velez Paiz y el Hospital Bautista.

### P4. Gestion de Almacen / Inventario

1. **4.1 Ingresar datos**: medicamento_id, cantidad, fecha_vencimiento.
2. **4.2 Validar datos**: medicamento_id entero; cantidad entera >= 0; fecha real.
3. **4.3 Agregar a la lista**: `almacen.append(AlmacenMedicamento(...))`.
4. **4.4 Buscar / Actualizar / Eliminar**: por `medicamento_id`.

---

## Operaciones CRUD

Cada entidad soporta las siguientes operaciones (una funcion por operacion,
en `funciones.py`):

| Operacion | Funcion (ej. Medicamento) | Descripcion |
|-----------|----------------------------|-------------|
| Registrar | `registrar_medicamento()` | Agrega uno nuevo a la lista |
| Buscar | `buscar_medicamento()` | Encuentra y devuelve el(los) que coincidan |
| Actualizar | `actualizar_medicamento()` | Modifica los datos de uno existente |
| Eliminar | `eliminar_medicamento()` | Lo quita de la lista |
| Contar | `contar_medicamentos()` | Devuelve cuantos hay (`len(lista)`) |
| Listar | `listar_medicamentos()` | Muestra todos en pantalla |

---

## Manejo de errores y validaciones

En `funciones.py` se usan validadores y `raise ValueError` cuando un dato es
incorrecto. La funcion `pedir_campo()` envuelve la lectura de datos en un
`try/except` y vuelve a preguntar hasta que el dato sea valido.

Principales validadores:

- `validar_nombre`: solo letras y espacios.
- `validar_email`: formato de correo.
- `validar_password`: minimo 4 caracteres.
- `validar_fecha`: formato DD/MM/AAAA y fecha real.
- `validar_hora`: formato HH:MM (24 horas).
- `validar_cantidad`: numero entero positivo.
- `validar_celular`: solo digitos.
