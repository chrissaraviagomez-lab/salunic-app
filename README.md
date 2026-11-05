# SALUNIC - Sistema de Salud y Bienestar

Proyecto integrador (Programación) — App Tkinter + Módulo por consola, integrados con la misma lógica y datos.

## Estructura (requerida por el profesor)

```text
salunic-app/
├── Entidades/              # DataClass (4): Usuario, CitaMedica, Medicamento, AlmacenMedicamento
├── Datos/                  # Listas en memoria + datos iniciales + persistencia JSON
│   └── datos.py            # cargar_datos / guardar_datos / salunic_datos.json (raíz)
├── Funciones/              # Lógica (una por cada DataClass) + utilidades
│   ├── usuario.py
│   ├── cita_medica.py
│   ├── medicamento.py
│   ├── almacen_medicamento.py
│   ├── sistema.py          # servicios para la app
│   ├── busqueda_lineal.py  # búsqueda lineal
│   ├── cola_atencion.py    # cola con prioridad (heapq, adulto mayor primero)
│   └── validaciones.py
├── app/                    # Aplicación gráfica Tkinter
│   ├── main.py
│   └── screens/            # UI: SOLO usa Funciones y Entidades
├── consola/                # Módulo por consola (usa Entidades, Datos, Funciones)
│   └── main.py
├── core/                   # Compatibilidad (delega a Entidades/Datos/Funciones)
├── docs/pdfs/              # Guías/PDFs de estudio y defensa
├── scripts/
└── salunic_datos.json      # Archivo de datos compartido (app + consola)
```

## Reglas de acceso (arquitectura)
- `app/screens/` → **solo** puede usar `Funciones` y `Entidades` (no accede directo a `Datos`).
- `Funciones/` → **solo** puede usar `Datos` y `Entidades`.
- `consola/` → usa `Entidades`, `Datos` y `Funciones` (misma lógica compartida).

## Temas implementados
- **4 DataClass**: `Usuario`, `CitaMedica`, `Medicamento`, `AlmacenMedicamento`.
- **Cola con prioridad** (heapq): adulto mayor = prioridad 0, normal = 1, `turno_global` desempata (no FIFO puro).
- **Búsqueda lineal**: recorrido elemento por elemento (ej. autenticación/consultas).
- **Archivo de datos JSON**: `salunic_datos.json` (guardar con `asdict`, cargar reconstruyendo objetos).

## Cómo ejecutar

### Aplicación gráfica (Tkinter)
```bash
py app/main.py
```

### Módulo por consola
```bash
py consola/main.py
```

## PDF de estudio (recomendado)
- `docs/pdfs/GUIA_ESTUDIO_FINAL_SALUNIC_ESTRUCTURA_REQUERIDA.pdf` — guía explicativa final (estructura, reglas, conexión app↔consola, código y tips de defensa).

## Nota sobre `core/`
`core/` se conserva solo por **compatibilidad** con versiones anteriores; delega a `Entidades/`, `Datos/` y `Funciones/` para mantener un único estado/lógica. La estructura a presentar y defender es la requerida (`Entidades/`, `Datos/`, `Funciones/`).
