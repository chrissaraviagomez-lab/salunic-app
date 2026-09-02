# Diagrama de Datos y Flujo de Datos - SaluNic

---

## Nivel 0 - Diagrama de Contexto

```
                          ┌─────────────────────┐
                          │                     │
                          │    APLICACIÓN       │
                          │      SaluNic        │
                          │                     │
                          └─────────────────────┘
                               ▲           ▲
                               │           │
              ┌────────────────┘           └───────────────┐
              │                                              │
              │                                              │
              ▼                                              ▼
   ┌─────────────────────┐                     ┌─────────────────────┐
   │                     │                     │                     │
   │      PACIENTE       │◄───────────────────▶│      MÉDICO         │
   │                     │                     │                     │
   └─────────────────────┘                     └─────────────────────┘
```

### Flujo de Datos - Nivel 0

| Flujo | Origen | Destino | Datos |
|-------|--------|---------|-------|
| F1 | Paciente | SaluNic | Datos de registro, credenciales, datos de medicamentos, solicitud de citas, datos de perfil médico |
| F2 | SaluNic | Paciente | Confirmación de registro, acceso al sistema, horarios de medicamentos, recordatorios, fichas médicas |
| F3 | Médico | SaluNic | Información de citas, diagnósticos, prescripciones, especialidades |
| F4 | SaluNic | Médico | Confirmación de citas, datos del paciente (con autorización) |

---

## Nivel 1 - Diagrama de Flujo de Datos

```
                         ┌─────────────────────┐
                         │                     │
                    ┌────│      PACIENTE       │────┐
                    │    │                     │    │
                    │    └─────────────────────┘    │
                    │                               │
              F1, F3, F5, F7                  F2, F4, F6, F8
                    │                               │
                    │                               │
                    ▼                               ▼
┌───────────────────────────────────────────────────────────────────────┐
│                                                                       │
│                       SISTEMA SALUNIC                                 │
│                                                                       │
│  ┌──────────────────────┐  ┌──────────────────────┐                  │
│  │                       │  │                       │                  │
│  │  1. Registro e       │  │  2. Gestión de        │                  │
│  │     Inicio de Sesión │  │     Medicamentos       │                  │
│  │                       │  │                       │                  │
│  │  Entrada:            │  │  Entrada:              │                  │
│  │  - usuario, contraseña│  │  - nombre medicamento │                  │
│  │  - nombre completo   │  │  - dosis               │                  │
│  │                       │  │  - frecuencia          │                  │
│  │  Salida:             │  │  - horaInicio          │                  │
│  │  - acceso al sistema │  │  - duracionDias        │                  │
│  │  - mensajes de error │  │                        │                  │
│  └───────────┬──────────┘  │  Salida:               │                  │
│              │             │  - horario registrado  │                  │
│              │             └───────────┬────────────┘                  │
│              │                         │                               │
│              │                         │                               │
│              ▼                         ▼                               │
│  ┌──────────────────────┐  ┌──────────────────────┐                  │
│  │                       │  │                       │                  │
│  │  3. Gestión de       │  │  4. Generación de    │                  │
│  │     Citas Médicas    │  │     Recordatorios     │                  │
│  │                       │  │                       │                  │
│  │  Entrada:            │  │  Entrada:              │                  │
│  │  - nombre paciente   │  │  - fechas de citas    │                  │
│  │  - nombre doctor     │  │  - horas de citas     │                  │
│  │  - especialidad      │  │  - horarios de meds   │                  │
│  │  - fecha última cita │  │                        │                  │
│  │  - fecha nueva cita  │  │  Salida:              │                  │
│  │  - hora nueva cita   │  │  - alerta cita médica │                  │
│  │                       │  │  - alarma medicamento│                  │
│  │  Salida:             │  └───────────┬────────────┘                  │
│  │  - cita renovada     │              │                               │
│  └───────────┬──────────┘              │                               │
│              │                         │                               │
│              ▼                         ▼                               │
│  ┌──────────────────────┐  ┌──────────────────────┐                  │
│  │                       │  │                       │                  │
│  │  5. Administración   │  │    BASE DE DATOS      │                  │
│  │     Perfil Médico    │  │                       │                  │
│  │                       │  │  ┌────────────────┐  │                  │
│  │  Entrada:            │  │  │  Usuarios      │  │                  │
│  │  - datos personales  │◀─┼──│  Medicamentos  │  │                  │
│  │  - grupo sanguíneo   │  │  │  Citas         │  │                  │
│  │  - alergias          │  │  │  Perfiles Méd  │  │                  │
│  │  - antecedentes      │  │  └────────────────┘  │                  │
│  │  - contacto emergencia│  └──────────────────────┘                  │
│  │                       │                                            │
│  │  Salida:             │                                            │
│  │  - ficha médica      │                                            │
│  └──────────────────────┘                                            │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘
                               ▲
                               │
                               │
                         ┌─────┴────────────┐
                         │                  │
                         │     MÉDICO       │
                         │                  │
                         └──────────────────┘
```

### Diccionario de Datos - Nivel 1

| Flujo | Origen | Destino | Descripción |
|-------|--------|---------|-------------|
| F1 | Paciente | Proceso 1 | usuario, contraseña, nombre completo |
| F2 | Proceso 1 | Paciente | confirmación de registro, error de validación |
| F3 | Paciente | Proceso 2 | nombreMedicamento, dosis, frecuencia, horaInicio, duracionDias |
| F4 | Proceso 2 | Paciente | horario registrado, error de datos |
| F5 | Paciente | Proceso 3 | nombrePaciente, nombreDoctor, especialidad, fechas |
| F6 | Proceso 3 | Paciente | cita agendada, renovación exitosa |
| F7 | Paciente | Proceso 5 | datos personales, clínicos y emergencia |
| F8 | Proceso 5 | Paciente | ficha médica completa |
| F9 | Médico | Proceso 3 | disponibilidad, especialidades, horarios |
| F10 | Proceso 3 | Médico | confirmación de cita, datos del paciente |

---

## Nivel 2 - Diagrama de Flujo de Datos (Subprocesos)

### 2.1 Subproceso: Registro e Inicio de Sesión

```
                    ┌─────────────────────┐
                    │                     │
                    │     PACIENTE        │
                    │                     │
                    └──────┬──────────────┘
                           │
                  F1.1     │     F1.2
            (registro)     │     (login)
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  1. Registro e Inicio de Sesión                                      │
│                                                                      │
│  ┌────────────────────┐    ┌────────────────────┐                    │
│  │                    │    │                    │                    │
│  │ 1.1 Registro      │───▶│ 1.2 Validación    │                    │
│  │ de Usuario        │    │ de Datos          │                    │
│  │                    │    │                    │                    │
│  │ Datos entrada:     │    │ Validación:        │                    │
│  │ - nombre           │    │ - campos no vacíos │                    │
│  │ - email            │    │ - contraseña >=6   │                    │
│  │ - contraseña       │    │ - contraseñas      │                    │
│  │ - confirmación     │    │   coinciden        │                    │
│  └─────────┬──────────┘    └────────┬───────────┘                    │
│            │                        │                                │
│            │                        ▼                                │
│            │               ┌────────────────┐                       │
│            │               │  ¿Datos        │                       │
│            │               │  válidos?      │                       │
│            │               │ ┌────┐ ┌────┐ │                       │
│            │               │ │ Sí │ │ No │ │                       │
│            │               │ └─┬──┘ └─┬──┘ │                       │
│            │               └───┼──────┼────┘                       │
│            │                   │      │                              │
│            ▼                   ▼      ▼                              │
│  ┌────────────────┐   ┌──────────┐  ┌────────────────┐              │
│  │ Almacenar      │   │ 1.3      │  │ Mostrar error  │              │
│  │ en BD         │   │ Verificar │  │ (campos        │              │
│  └────────┬───────┘   │ Login    │  │ inválidos)     │              │
│           │           └────┬─────┘  └────────────────┘              │
│           │                │                                         │
│           ▼                ▼                                         │
│  ┌────────────────────────────────────────────┐                     │
│  │              BD Usuarios                   │                     │
│  │  ┌──────────────┐  ┌──────────────────┐    │                     │
│  │  │ Credenciales │  │  Perfiles        │    │                     │
│  │  └──────────────┘  └──────────────────┘    │                     │
│  └──────────────────────┬─────────────────────┘                     │
│                         │                                            │
│                         ▼                                            │
│              ┌────────────────────┐                                 │
│              │ ¿Credenciales      │                                 │
│              │ correctas?         │                                 │
│              │ ┌────┐ ┌────┐      │                                 │
│              │ │ Sí │ │ No │      │                                 │
│              │ └─┬──┘ └─┬──┘      │                                 │
│              └───┼──────┼────────┘                                 │
│                  │      │                                            │
│                  ▼      ▼                                            │
│           ┌────────┐ ┌──────────────────────┐                      │
│           │ Acceso │ │ ¿Intentos < 3?       │                      │
│           │ al     │ │ ┌────┐ ┌───────────┐ │                      │
│           │ Menú   │ │ │ Sí │ │ No         │ │                      │
│           └────────┘ │ └─┬──┘ │ Bloquear  │ │                      │
│                      └───┼────┼───────────┘ │                      │
│                          │    └─────────────┘                      │
│                          ▼                                          │
│                   ┌────────────┐                                   │
│                   │ Reintentar │                                   │
│                   └────────────┘                                   │
└──────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ F1.3 (resultado)
                                    ▼
                           ┌─────────────────────┐
                           │                     │
                           │     PACIENTE        │
                           │                     │
                           └─────────────────────┘
```

### 2.2 Subproceso: Gestión de Medicamentos

```
                    ┌─────────────────────┐
                    │                     │
                    │     PACIENTE        │
                    │                     │
                    └──────┬──────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  2. Gestión de Medicamentos                                          │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  2.1 Ingreso de Datos del Medicamento                        │    │
│  │                                                              │    │
│  │  Datos recolectados:                                         │    │
│  │  - nombreMedicamento (texto)                                 │    │
│  │  - dosis (ej: "1 pastilla", "5ml")                          │    │
│  │  - frecuencia (ej: "cada 8 horas", "1 vez al día")          │    │
│  │  - horaInicio (HH:MM)                                       │    │
│  │  - duracionDias (entero positivo)                           │    │
│  │                                                              │    │
│  └──────────────────────────┬──────────────────────────────────┘    │
│                             │                                        │
│                             ▼                                        │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  2.2 Validación de Datos                                     │    │
│  │                                                              │    │
│  │  ¿nombreMedicamento ≠ "" Y dosis ≠ "" Y frecuencia ≠ ""     │    │
│  │   Y horaInicio ≠ "" Y duracionDias > 0?                     │    │
│  │                                                              │    │
│  │  ┌────────────┐               ┌────────────┐                │    │
│  │  │   Sí       │               │   No       │                │    │
│  │  └─────┬──────┘               └─────┬──────┘                │    │
│  └────────┼───────────────────────────┼────────────────────────┘    │
│           │                           │                              │
│           ▼                           ▼                              │
│  ┌────────────────────────┐  ┌────────────────────┐                 │
│  │ 2.3 Mostrar Resumen    │  │ Mostrar error:     │                 │
│  │                        │  │ "Datos incompletos │                 │
│  │  - Medicamento: [nom]  │  │ o duración         │                 │
│  │  - Dosis: [dosis]      │  │ inválida"          │                 │
│  │  - Frecuencia: [frec]  │  └────────────────────┘                 │
│  │  - Primera toma: [hora]│                                        │
│  │  - Duración: [días]    │                                        │
│  └───────────┬────────────┘                                        │
│              │                                                      │
│              ▼                                                      │
│  ┌──────────────────────────────────────────────────────────┐      │
│  │  2.4 Confirmación                                        │      │
│  │                                                          │      │
│  │  ¿Desea confirmar el horario?                            │      │
│  │                                                          │      │
│  │  ┌────────────┐               ┌────────────┐            │      │
│  │  │   SI       │               │   NO       │            │      │
│  │  └─────┬──────┘               └─────┬──────┘            │      │
│  └────────┼───────────────────────────┼────────────────────┘      │
│           │                           │                              │
│           ▼                           ▼                              │
│  ┌────────────────┐        ┌────────────────────┐                   │
│  │ Guardar en BD │        │ Cancelar registro  │                   │
│  │ Medicamentos   │        └────────────────────┘                   │
│  └───────┬────────┘                                                │
│          │                                                          │
│          ▼                                                          │
│  ┌──────────────────────────────────────────────────────────┐      │
│  │              BD Medicamentos                              │      │
│  │  ┌──────────────┐  ┌──────────────────┐                   │      │
│  │  │ Medicamentos │  │  Horarios        │                   │      │
│  │  └──────────────┘  └──────────────────┘                   │      │
│  └──────────────────────────────────────────────────────────┘      │
└──────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ F2.1 (resultado)
                                    ▼
                           ┌─────────────────────┐
                           │                     │
                           │     PACIENTE        │
                           │                     │
                           └─────────────────────┘
```

### 2.3 Subproceso: Gestión de Citas Médicas

```
                    ┌─────────────────────┐
                    │                     │
                    │     PACIENTE        │
                    │                     │
                    └──────┬──────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  3. Gestión de Citas Médicas                                        │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  3.1 Solicitud de Renovación                                 │    │
│  │                                                              │    │
│  │  Datos entrada:                                              │    │
│  │  - nombrePaciente                                            │    │
│  │  - nombreDoctorActual (última cita)                          │    │
│  │  - especialidadActual                                        │    │
│  │  - fechaUltimaCita (DD/MM/AAAA)                             │    │
│  │                                                              │    │
│  └──────────────────────────┬──────────────────────────────────┘    │
│                             │                                        │
│                             ▼                                        │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  3.2 Validación de datos iniciales                           │    │
│  │                                                              │    │
│  │  ¿nombrePaciente ≠ "" Y nombreDoctorActual ≠ ""             │    │
│  │   Y especialidadActual ≠ ""?                                │    │
│  │                                                              │    │
│  │  ┌────────────┐               ┌────────────┐                │    │
│  │  │   Sí       │               │   No       │                │    │
│  │  └─────┬──────┘               └─────┬──────┘                │    │
│  └────────┼───────────────────────────┼────────────────────────┘    │
│           │                           │                              │
│           ▼                           ▼                              │
│  ┌────────────────────────┐  ┌────────────────────┐                 │
│  │ 3.3 Consultar          │  │ Mostrar error:     │                 │
│  │ Disponibilidad (BD)    │  │ "Campos            │                 │
│  │                        │  │ obligatorios"      │                 │
│  │ ┌──────────┐           │  └────────────────────┘                 │
│  │ │Disponible│           │                                        │
│  │ └─────┬────┘           │                                        │
│  └───────┼────────────────┘                                        │
│          │                                                          │
│          ▼                                                          │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  3.4 Ingreso de Nueva Cita                                   │    │
│  │                                                              │    │
│  │  - fechaNuevaCita (DD/MM/AAAA)                              │    │
│  │  - horaNuevaCita (HH:MM)                                    │    │
│  │                                                              │    │
│  └──────────────────────────┬──────────────────────────────────┘    │
│                             │                                        │
│                             ▼                                        │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  3.5 Validación: ¿fechaNuevaCita ≠ "" Y horaNuevaCita ≠ ""?│    │
│  │                                                              │    │
│  │  ┌────────────┐               ┌────────────┐                │    │
│  │  │   Sí       │               │   No       │                │    │
│  │  └─────┬──────┘               └─────┬──────┘                │    │
│  └────────┼───────────────────────────┼────────────────────────┘    │
│           │                           │                              │
│           ▼                           ▼                              │
│  ┌────────────────────────┐  ┌────────────────────┐                 │
│  │ 3.6 Confirmación       │  │ Mostrar error:     │                 │
│  │                        │  │ "Fecha y hora      │                 │
│  │  Mostrar resumen:      │  │ inválidas"         │                 │
│  │  - Paciente            │  └────────────────────┘                 │
│  │  - Especialidad        │                                        │
│  │  - Doctor              │                                        │
│  │  - Nueva Fecha         │                                        │
│  │  - Nueva Hora          │                                        │
│  │                        │                                        │
│  │  ¿Confirmar cita?      │                                        │
│  │  ┌────┐ ┌────┐        │                                        │
│  │  │ SI │ │ NO │        │                                        │
│  │  └─┬──┘ └─┬──┘        │                                        │
│  └────┼──────┼───────────┘                                        │
│       │      │                                                      │
│       ▼      ▼                                                      │
│  ┌────────┐ ┌────────────────────┐                                 │
│  │ Cita   │ │ Cancelar          │                                 │
│  │agendada│ │ renovación        │                                 │
│  └───┬────┘ └────────────────────┘                                 │
│      │                                                              │
│      ▼                                                              │
│  ┌──────────────────────────────────────────────────────────┐      │
│  │              BD Citas                                     │      │
│  │  ┌──────────────┐  ┌──────────────────┐                   │      │
│  │  │ Citas        │  │ Doctores         │                   │      │
│  │  └──────────────┘  └──────────────────┘                   │      │
│  └──────────────────────────────────────────────────────────┘      │
└──────────────────────────────────────────────────────────────────────┘
                                    │
                                    │
                                    ▼
                           ┌─────────────────────┐
                           │                     │
                           │     PACIENTE        │
                           │                     │
                           └─────────────────────┘
```

### 2.4 Subproceso: Generación de Recordatorios

```
                    ┌─────────────────────┐
                    │                     │
                    │     PACIENTE        │
                    │                     │
                    └──────┬──────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  4. Generación de Recordatorios                                      │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  4.1 Consultar BD                                           │    │
│  │                                                              │    │
│  │  Consulta: Obtener todas las citas próximas y                │    │
│  │  horarios de medicamentos activos desde la BD               │    │
│  │                                                              │    │
│  │  ┌────────────────────────────────────────────────────┐     │    │
│  │  │  BD Citas        → fechasCitas, horasCitas        │     │    │
│  │  │  BD Medicamentos  → horariosMedicamentos          │     │    │
│  │  └────────────────────────────────────────────────────┘     │    │
│  │                                                              │    │
│  └──────────────────────────┬──────────────────────────────────┘    │
│                             │                                        │
│                             ▼                                        │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  4.2 Evaluación de Tiempos                                   │    │
│  │                                                              │    │
│  │  ¿Fecha actual + 1 día >= fechaCita?                        │    │
│  │  ¿Hora actual + 1 hora >= horaMedicamento?                  │    │
│  │                                                              │    │
│  │  ┌────────────┐               ┌────────────┐                │    │
│  │  │ Próximo    │               │ No próximo │                │    │
│  │  └─────┬──────┘               └────────────┘                │    │
│  └────────┼────────────────────────────────────────────────────┘    │
│           │                                                          │
│           ▼                                                          │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  4.3 Generar Alerta                                          │    │
│  │                                                              │    │
│  │  ┌─────────────────────────┐  ┌──────────────────────────┐  │    │
│  │  │ Alerta de Cita Médica  │  │ Alarma de Medicamento    │  │    │
│  │  │                         │  │                          │  │    │
│  │  │ "Estimado/a [nombre],   │  │ "Hora de tomar          │  │    │
│  │  │  Le recordamos su cita  │  │  [medicamento]          │  │    │
│  │  │  con Dr./Dra. [doctor]  │  │  Dosis: [dosis]"        │  │    │
│  │  │  Fecha: [fecha]         │  │                          │  │    │
│  │  │  Hora: [hora]"          │  └──────────────────────────┘  │    │
│  │  └─────────────────────────┘                               │    │
│  └──────────────────────────┬─────────────────────────────────┘    │
│                             │                                        │
│                             ▼                                        │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  4.4 Envío de Notificación                                   │    │
│  │                                                              │    │
│  │  - Notificación push en pantalla                            │    │
│  │  - Alarma sonora (opcional)                                 │    │
│  │  - Visualización en panel de control (Home)                 │    │
│  │                                                              │    │
│  └─────────────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────────────┘
                                    │
                                    │
                                    ▼
                           ┌─────────────────────┐
                           │                     │
                           │     PACIENTE        │
                           │                     │
                           └─────────────────────┘
```

### 2.5 Subproceso: Administración de Perfil Médico

```
                    ┌─────────────────────┐
                    │                     │
                    │     PACIENTE        │
                    │                     │
                    └──────┬──────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  5. Administración de Perfil Médico                                  │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  5.1 Datos Personales                                        │    │
│  │                                                              │    │
│  │  - nombrePaciente (texto)                                   │    │
│  │  - apellidoPaciente (texto)                                 │    │
│  │  - fechaNacimiento (DD/MM/AAAA)                             │    │
│  │                                                              │    │
│  └──────────────────────────┬──────────────────────────────────┘    │
│                             │                                        │
│                             ▼                                        │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  5.2 Grupo Sanguíneo                                        │    │
│  │                                                              │    │
│  │  - grupoSanguineo (ej: "A+", "O-", "AB+")                  │    │
│  │                                                              │    │
│  └──────────────────────────┬──────────────────────────────────┘    │
│                             │                                        │
│                             ▼                                        │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  5.3 Alergias                                               │    │
│  │                                                              │    │
│  │  - alergias (separadas por coma, "Ninguna" si no aplica)   │    │
│  │                                                              │    │
│  └──────────────────────────┬──────────────────────────────────┘    │
│                             │                                        │
│                             ▼                                        │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  5.4 Antecedentes Médicos                                   │    │
│  │                                                              │    │
│  │  - antecedentesMedicos (ej: Hipertensión, Diabetes, etc.)   │    │
│  │                                                              │    │
│  └──────────────────────────┬──────────────────────────────────┘    │
│                             │                                        │
│                             ▼                                        │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  5.5 Contacto de Emergencia                                  │    │
│  │                                                              │    │
│  │  - contactoEmergenciaNombre (texto)                         │    │
│  │  - contactoEmergenciaTelefono (texto)                       │    │
│  │                                                              │    │
│  └──────────────────────────┬──────────────────────────────────┘    │
│                             │                                        │
│                             ▼                                        │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  5.6 Generar Ficha Médica                                    │    │
│  │                                                              │    │
│  │  ┌────────────────────────────────────────────────────────┐ │    │
│  │  │              FICHA MÉDICA                              │ │    │
│  │  │                                                        │ │    │
│  │  │  Nombre: [nombrePaciente] [apellidoPaciente]          │ │    │
│  │  │  Fecha de Nacimiento: [fechaNacimiento]               │ │    │
│  │  │  Grupo Sanguíneo: [grupoSanguineo]                    │ │    │
│  │  │  Alergias: [alergias]                                  │ │    │
│  │  │  Antecedentes Médicos: [antecedentesMedicos]          │ │    │
│  │  │  Contacto Emergencia: [contactoEmergenciaNombre]      │ │    │
│  │  │                     - [contactoEmergenciaTelefono]    │ │    │
│  │  └────────────────────────────────────────────────────────┘ │    │
│  │                                                              │    │
│  └──────────────────────────┬──────────────────────────────────┘    │
│                             │                                        │
│                             ▼                                        │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                                                              │    │
│  │  5.7 Confirmación                                           │    │
│  │                                                              │    │
│  │  ¿Los datos mostrados son correctos?                        │    │
│  │                                                              │    │
│  │  ┌────────────┐               ┌────────────┐                │    │
│  │  │   Sí       │               │   No       │                │    │
│  │  └─────┬──────┘               └─────┬──────┘                │    │
│  └────────┼───────────────────────────┼────────────────────────┘    │
│           │                           │                              │
│           ▼                           ▼                              │
│  ┌────────────────┐        ┌────────────────────┐                   │
│  │ Guardar en BD │        │ Revisar y editar   │                   │
│  │ Perfiles Méd  │        │ perfil médico      │                   │
│  └───────┬────────┘        └────────────────────┘                   │
│          │                                                          │
│          ▼                                                          │
│  ┌──────────────────────────────────────────────────────────┐      │
│  │              BD Perfiles Médicos                          │      │
│  │  ┌──────────────┐  ┌──────────────────┐                   │      │
│  │  │ Perfiles     │  │ Contactos        │                   │      │
│  │  └──────────────┘  └──────────────────┘                   │      │
│  └──────────────────────────────────────────────────────────┘      │
└──────────────────────────────────────────────────────────────────────┘
                                    │
                                    │
                                    ▼
                           ┌─────────────────────┐
                           │                     │
                           │     PACIENTE        │
                           │                     │
                           └─────────────────────┘
```

---

## Tabla Resumen de Flujos de Datos

### Nivel 0 (Contexto)

| ID Flujo | Origen | Destino | Descripción |
|----------|--------|---------|-------------|
| F0-1 | Paciente | SaluNic | Datos de registro, login, medicamentos, citas, perfil |
| F0-2 | SaluNic | Paciente | Confirmaciones, accesos, horarios, recordatorios, ficha |
| F0-3 | Médico | SaluNic | Información de citas, diagnósticos, prescripciones |
| F0-4 | SaluNic | Médico | Confirmaciones, datos de pacientes autorizados |

### Nivel 1

| ID Flujo | Origen | Destino | Datos |
|----------|--------|---------|-------|
| F1-1 | Paciente | P1-Registro | usuario, contraseña, nombre |
| F1-2 | P1-Registro | Paciente | confirmación, error |
| F1-3 | Paciente | P2-Medicamentos | nombreMed, dosis, frecuencia, hora, duración |
| F1-4 | P2-Medicamentos | Paciente | horario registrado, error |
| F1-5 | Paciente | P3-Citas | datos paciente, doctor, especialidad, fechas |
| F1-6 | P3-Citas | Paciente | cita agendada, error |
| F1-7 | Paciente | P5-Perfil | datos personales, clínicos, emergencia |
| F1-8 | P5-Perfil | Paciente | ficha médica completa |
| F1-9 | Médico | P3-Citas | disponibilidad, horarios |
| F1-10 | P3-Citas | Médico | confirmación de cita |

### Nivel 2 (Subprocesos detallados en cada diagrama arriba)

| Proceso | Subprocesos | Almacenes de Datos |
|---------|-------------|-------------------|
| P1-Registro | 1.1 Registro, 1.2 Validación, 1.3 Verificar Login | BD Usuarios |
| P2-Medicamentos | 2.1 Ingreso, 2.2 Validación, 2.3 Resumen, 2.4 Confirmación | BD Medicamentos |
| P3-Citas | 3.1 Solicitud, 3.2 Validación, 3.3 Disponibilidad, 3.4 Nueva Cita, 3.5 Validación, 3.6 Confirmación | BD Citas |
| P4-Recordatorios | 4.1 Consulta BD, 4.2 Evaluación, 4.3 Generar Alerta, 4.4 Envío | BD Citas, BD Medicamentos |
| P5-Perfil | 5.1-5.5 Datos, 5.6 Generar Ficha, 5.7 Confirmación | BD Perfiles Médicos |
