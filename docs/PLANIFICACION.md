# Planificación del Proyecto: Organizador de Horario Universitario

> Documento de análisis y diseño inicial. No contiene código.
> Fecha: Junio 2026

---

## Arquitectura general

El proyecto tiene **dos capas separadas**:

- **Backend (API):** Python + FastAPI. Maneja los datos, la lógica de negocio y la detección de conflictos.
- **Frontend (interfaz visual):** HTML + CSS + JavaScript puro (sin frameworks). Muestra el horario como una grilla visual y permite al usuario interactuar con formularios.

La comunicación entre ambas capas se hace a través de una API REST (el frontend le pide datos al backend mediante peticiones HTTP).

## Estructura de archivos

```
horario-universitario/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── schemas.py          # Estructura de datos (Materia, Bloque)
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── materias.py         # Endpoints: POST/GET/DELETE /materias
│   │   │   └── bloques.py          # Endpoints: POST/GET/DELETE /bloques, GET /conflictos
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── horario_service.py  # Lógica: leer/guardar/modificar datos en JSON
│   │   │   └── conflictos.py       # Algoritmo de detección de solapamiento
│   │   └── utils/
│   │       ├── __init__.py
│   │       └── tiempo.py           # Helpers: convertir horas a minutos, validar formato
│   ├── data/
│   │   └── horario.json            # Persistencia (reemplaza una base de datos)
│   ├── tests/
│   │   ├── test_materias.py        # Pruebas de materias
│   │   └── test_conflictos.py      # Pruebas del algoritmo de solapamiento
│   ├── main.py                     # Punto de entrada: arranca el servidor
│   └── requirements.txt            # Dependencias: fastapi, uvicorn
├── frontend/
│   ├── index.html                  # Gestión: formularios y lista de materias
│   ├── horario.html                # Visualización: grilla visual + descarga
│   ├── css/
│   │   └── styles.css              # Estilos globales y layout de la grilla
│   └── js/
│       ├── api.js                  # Único archivo que hace fetch() al backend
│       ├── grilla.js               # Construye y renderiza la grilla en el DOM
│       ├── main.js                 # Orquesta index.html: conecta eventos con funciones
│       └── materias.js             # Renderiza lista de materias y alertas
├── docs/
│   └── PLANIFICACION.md
├── .gitignore
└── README.md
```

---

## 1. ¿Cuál es el problema exacto que resuelve?

Los estudiantes universitarios manejan múltiples materias con horarios fragmentados durante el semestre. Actualmente dependen de anotaciones manuales, hojas de cálculo o apps genéricas que no están pensadas para el contexto académico.

**El problema concreto:** No existe una herramienta personalizada que permita registrar materias, asignarles horarios, detectar automáticamente si hay solapamiento entre clases, visualizar la semana de forma clara y descargar el horario.

---

## 2. ¿Quién es el usuario objetivo?

**Perfil principal:** Estudiante universitario de pregrado que lleva entre 4 y 7 materias por semestre, en una institución con horarios por bloques (Lunes-Viernes, con posible sábado).

**Características del usuario:**
- Maneja su propio horario (no lo gestiona nadie más)
- Puede tener materias en distintos salones o edificios
- A veces inscribe grupos alternativos con horarios distintos
- Necesita detectar rápidamente si dos clases se cruzan
- Quiere poder **descargar su horario** (PDF o imagen) para tenerlo a mano

---

## 3. Alcance mínimo viable (MVP)

El MVP debe ser funcional con lo estrictamente necesario para resolver el problema central.

**Backend incluye:**
- Registrar una materia con nombre, código (opcional) y créditos
- Registrar uno o más bloques de horario por materia (día, hora inicio, hora fin, salón)
- Detectar conflictos entre bloques
- Exponer una API REST que el frontend pueda consumir
- Persistir los datos en un archivo JSON (simple, sin base de datos)

**Frontend incluye:**
- Formulario para registrar materias y horarios
- Grilla visual semanal (Lunes–Sábado, bloques de tiempo)
- Indicación visual de conflictos
- Botón para **descargar el horario** como PDF o imagen

**Criterio de "listo":** Un estudiante puede ingresar todas sus materias, ver su horario visualmente y descargarlo, todo desde el navegador.

---

## 4. Funcionalidades fuera de la primera versión

| Funcionalidad | Razón para diferir |
|---|---|
| Autenticación / múltiples usuarios | Complejidad de sesiones y seguridad |
| Base de datos real (SQL, MongoDB) | JSON es suficiente para uso personal |
| Importar horarios desde PDF/imagen | Complejidad alta (OCR, parsing) |
| Notificaciones o recordatorios | Requiere integración con sistema operativo o servicios externos |
| Materias con horarios variables por semana | Edge case poco frecuente |
| Modo oscuro / temas visuales | Cosmético, no funcional |
| Compartir horario con otros usuarios | Requiere backend más complejo |

---

## 5. ¿Qué datos necesita almacenar el sistema?

### Entidad: Materia
- Nombre (ej. "Cálculo I")
- Código (ej. "MAT101") — opcional
- Créditos — opcional
- Color de representación en la grilla — opcional

### Entidad: Bloque de Horario
- Referencia a la materia a la que pertenece
- Día de la semana (Lunes, Martes… Sábado)
- Hora de inicio (ej. 08:00)
- Hora de fin (ej. 09:30)
- Salón / Ubicación — opcional

### Relación
Una materia puede tener **uno o más bloques de horario** (por ejemplo, Cálculo I: Lunes 8-10am y Miércoles 8-10am).

---

## 6. Casos de uso principales

1. **Registrar materia** — El usuario llena un formulario con nombre, código y color.
2. **Registrar horario** — El usuario asigna uno o más bloques de tiempo a una materia.
3. **Detectar conflicto** — El sistema resalta visualmente si dos bloques se solapan.
4. **Ver horario semanal** — El frontend muestra una grilla visual de lunes a sábado con las materias ubicadas por bloques.
5. **Listar materias** — El usuario ve un panel con todas las materias registradas.
6. **Eliminar materia u horario** — El usuario puede borrar entradas incorrectas.
7. **Descargar horario** — El usuario exporta la grilla visual como PDF o imagen (PNG).

---

## 7. Dificultades técnicas anticipadas

| Dificultad | Descripción |
|---|---|
| Representar tiempo | Comparar horas como strings es peligroso. El backend debe trabajar con un formato estándar (ej. "HH:MM" en 24h). |
| Detectar solapamiento | La lógica de "¿se cruzan dos rangos?" tiene casos borde (inicio exacto del otro, mismo fin, etc.). |
| Comunicación frontend-backend | El frontend debe saber qué endpoints existen, qué enviar y qué esperar. Requiere diseñar la API antes de programar. |
| Renderizar la grilla visual | Colocar cada bloque en la posición correcta según hora y día, con tamaño proporcional a la duración. |
| Exportar a PDF/imagen | Hay librerías para esto, pero capturar el HTML/CSS como imagen fiel puede tener quirks en distintos navegadores. |
| CORS | Cuando el frontend y el backend corren en puertos distintos localmente, el navegador bloquea las peticiones por defecto. Hay que configurarlo explícitamente. |
| Escalabilidad de datos | El archivo JSON puede crecer. La estructura en memoria debe ser fácil de serializar y de leer. |

---

## 8. Etapas de desarrollo progresivo

---

### Etapa 1 — Diseño de la API y estructuras de datos (Semana 1)
**Capa:** Backend

- Definir los modelos de datos: `Materia` y `Bloque`
- Diseñar los endpoints de la API (qué rutas existirán, qué reciben y qué devuelven)
- Elegir el framework de backend (ej. FastAPI o Flask para Python)
- No hay código todavía — solo documentación de la API

**Entregable:** Lista de endpoints con método HTTP, ruta, cuerpo y respuesta esperada.

---

### Etapa 2 — Backend: CRUD de materias y bloques (Semana 1-2)
**Capa:** Backend

- Implementar los endpoints para crear, listar y eliminar materias
- Implementar los endpoints para crear, listar y eliminar bloques de horario
- Persistir los datos en un archivo JSON
- Probar los endpoints con una herramienta como Postman o Thunder Client

**Entregable:** API funcional que responde correctamente a peticiones HTTP.

---

### Etapa 3 — Backend: Detección de conflictos (Semana 2)
**Capa:** Backend

- Implementar la lógica de solapamiento entre dos bloques
- Exponer un endpoint que devuelva la lista de conflictos detectados
- Considerar los casos borde (inicio exacto del otro, mismo fin)

**Entregable:** Endpoint `/conflictos` que devuelve qué bloques se cruzan y entre qué materias.

---

### Etapa 4 — Frontend: Formularios y conexión a la API (Semana 2-3)
**Capa:** Frontend

- Crear la interfaz con formularios para registrar materias y bloques
- Conectar los formularios a los endpoints del backend (peticiones fetch o axios)
- Mostrar la lista de materias registradas
- Mostrar alertas cuando hay conflictos

**Entregable:** El usuario puede registrar su horario desde el navegador y ver los datos en tiempo real.

---

### Etapa 5 — Frontend: Grilla visual semanal (Semana 3-4)
**Capa:** Frontend

- Renderizar una grilla con columnas por día (Lunes–Sábado) y filas por hora
- Colocar cada bloque en la posición y tamaño correctos
- Usar colores distintos por materia para diferenciarlas visualmente
- Marcar visualmente los bloques en conflicto

**Entregable:** Vista del horario semanal que se actualiza al registrar o eliminar materias.

---

### Etapa 6 — Exportar horario (Semana 4-5)
**Capa:** Frontend

- Implementar botón "Descargar como PDF" o "Descargar como imagen"
- Capturar la grilla visual y generar el archivo descargable
- Asegurar que el resultado se vea fiel al horario en pantalla

**Entregable:** El usuario puede descargar su horario con un solo clic.

---

### Etapa 7 — Pulido y pruebas (Semana 5-6)
**Capas:** Frontend y Backend

- Validar entradas en ambos lados (formato de hora, campos vacíos, etc.)
- Mejorar la experiencia visual (mensajes de error, estados vacíos, feedback al usuario)
- Revisar todos los flujos con casos extremos
- Escribir un README con instrucciones para correr el proyecto

**Entregable:** MVP completo, visual y funcional.

---

## 9. Decisiones de diseño

| # | Decisión | Estado |
|---|---|---|
| 1 | **Backend:** Python + FastAPI | ✅ Decidido |
| 2 | **Frontend:** HTML + CSS + JavaScript puro (sin frameworks) | ✅ Decidido |
| 3 | **¿Cómo representar las horas internamente?** (string "08:00", entero en minutos…) | ⏳ Pendiente |
| 4 | **¿Un bloque que termina a las 10:00 y otro que empieza a las 10:00 es conflicto?** | ⏳ Pendiente |
| 5 | **¿Una materia puede tener múltiples grupos con horarios distintos?** | ⏳ Pendiente |
| 6 | **¿El color de la materia lo elige el usuario o lo asigna el sistema?** | ⏳ Pendiente |

---

*Este documento es vivo. Actualízalo conforme el proyecto evoluciona.*
