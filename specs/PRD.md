# PRD -- Organizador Web para TFG

## 1. Visión del producto

Crear una **aplicación web** que permita a estudiantes universitarios
**planificar, organizar, ejecutar y finalizar su Trabajo de Fin de Grado
(TFG)** en un único espacio, reduciendo el estrés, la desorganización y
el riesgo de retrasos.

> **Propuesta de valor**: Un único entorno guiado que acompaña al alumno
> desde la idea inicial hasta la entrega final del TFG.

------------------------------------------------------------------------

## 2. Problema

Los estudiantes que realizan un TFG suelen enfrentarse a: - Falta de
estructura y planificación clara. - Uso de múltiples herramientas
inconexas (Word, Drive, Excel, Notion...). - Pérdida de referencias,
ideas y notas. - Dificultad para medir el progreso real. -
Incumplimiento de deadlines importantes.

------------------------------------------------------------------------

## 3. Objetivos del producto

### Objetivos de negocio

-   Incrementar la tasa de finalización de TFG a tiempo.
-   Reducir la curva de aprendizaje en la gestión de trabajos largos.
-   Crear una base sólida para futuras extensiones (tutores,
    universidades).

### Objetivos de usuario

-   Saber **qué hacer, cuándo y por qué** en cada momento.
-   Centralizar todo el trabajo del TFG en una sola herramienta.
-   Visualizar progreso y detectar retrasos de forma temprana.

------------------------------------------------------------------------

## 4. Usuarios y personas

### Usuario principal

**Alumno/a universitario/a (Grado)**\
- Primer TFG o experiencia limitada en proyectos largos.\
- Alta carga emocional y presión por la entrega.

### Usuario secundario (futuro)

**Tutor/a académico/a** (fuera de alcance del MVP).

------------------------------------------------------------------------

## 5. Alcance del producto (MVP)

### Incluido

-   Gestión de tareas y planificación.
-   Gestión de capítulos del TFG.
-   Escritura por capítulos.
-   Gestión de referencias bibliográficas.
-   Gestión de ideas y notas.
-   Visualización de progreso.
-   Alertas de deadlines.

### Fuera de alcance (por ahora)

-   Colaboración con tutor.
-   Exportación a PDF/Word.
-   Gestión de citas automática (APA, MLA...).
-   IA para corrección o sugerencias.

------------------------------------------------------------------------

## 6. Requisitos funcionales

### RF-01 Gestión de tareas

-   Crear, editar y eliminar tareas.
-   Asignar fechas límite.
-   Estados: pendiente, en progreso, completada.

### RF-02 Progreso

-   Cálculo automático del progreso según tareas y capítulos.
-   Visualización porcentual.

### RF-03 Capítulos

-   Crear, editar y eliminar capítulos.
-   Estados: borrador, revisión, final.

### RF-04 Escritura

-   Editor de texto básico por capítulo.
-   Guardado automático.
-   Contador de palabras.

### RF-05 Referencias

-   Añadir referencias con metadatos básicos.
-   Notas por referencia.
-   Marcar referencias como usadas.

### RF-06 Ideas y notas

-   Crear notas rápidas.
-   Edición y eliminación.

### RF-07 Alertas

-   Avisos por deadlines próximos o vencidos.

------------------------------------------------------------------------

## 7. Requisitos no funcionales

-   Aplicación web responsive.
-   Persistencia automática de datos.
-   Tiempo de carga inicial \< 3s.
-   Interfaz clara, minimalista y orientada a estudiantes.
-   Seguridad básica de datos (login futuro).

------------------------------------------------------------------------

## 8. Métricas de éxito (KPIs)

  Métrica                        Objetivo
  ------------------------------ --------------------
  Tareas completadas / creadas   \>70%
  Uso semanal activo             \>60%
  Entregas a tiempo              Incremento medible
  NPS de alumnos                 \>7

------------------------------------------------------------------------

## 9. Riesgos y mitigaciones

  Riesgo                        Mitigación
  ----------------------------- ----------------------------
  Producto demasiado complejo   MVP estricto
  Abandono temprano             Onboarding guiado
  Falta de hábito               Alertas y progreso visible

------------------------------------------------------------------------

## 10. Roadmap de alto nivel

### Sprint 1

-   Planificación de tareas
-   Dashboard básico
-   Progreso general

### Sprint 2

-   Capítulos y escritura
-   Notas e ideas

### Sprint 3

-   Referencias
-   Alertas de deadlines

------------------------------------------------------------------------

## 11. Principios de producto

-   **Simplicidad \> potencia**
-   **Guía al usuario, no lo abruma**
-   **Visibilidad constante del progreso**

------------------------------------------------------------------------

**Estado del PRD**: Aprobado para generación de backlog

------------------------------------------------------------------------

## 12. Feature Specs (Detailed)

### 12.1 Task Management (Gestión de Tareas)
The Task Management feature allows students to create, track, and organize the specific activities required to complete their TFG. It acts as the central hub for translating theoretical work into actionable steps, reducing anxiety and disorganization.

#### Actors
- **Student (`STUDENT`)**: Full control (CRUD) over their own tasks.

#### Access Levels
- **Private Access**: Tasks are strictly private to the creating user. No public or shared access in this version.

#### Requirements and Constraints
- **Security Constraint**: Must enforce strict ownership boundaries (Row-Level Security pattern).
- **Performance Requirement**: Interaction (create/toggle status) must feel instant (< 100ms) to encourage frequent usage.
- **Privacy**: Data must be encrypted in transit.
