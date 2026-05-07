## 📅 Daily 1

### 🎯 Objetivo del día
Construir la base del sistema y comenzar la implementación de las primeras historias de usuario siguiendo un enfoque incremental (XP).

---

### 🧱 Trabajo realizado

#### 🔹 Inicialización del proyecto
- Creación del README.md y definición de las Historias de Usuario
- Organización inicial del repositorio

#### 🔹 Arquitectura del backend
- Reorganización completa del backend siguiendo arquitectura en capas:
  - models, schemas, repositories, services, routers
- Configuración de la base de datos con SQLAlchemy
- Definición de modelos:
  - Book
  - User
  - Loan

#### 🔹 Validación y lógica de negocio
- Creación de schemas con Pydantic para validación de datos
- Implementación de repositories para acceso a datos
- Implementación de services con lógica de negocio

#### 🔹 API con FastAPI
- Creación de routers:
  - /books
  - /users
  - /loans
- Creación del punto de entrada (`main.py`)
- Integración completa de la API

#### 🔹 Infraestructura
- Configuración de Docker y docker-compose
- Levantamiento del entorno completo (FastAPI + Streamlit)

---

### 🚀 Historias de usuario implementadas

#### ✅ HU-02: Registrar un nuevo libro
- Formulario en Streamlit
- Conexión con endpoint POST /books/
- Validación de campos obligatorios

#### ✅ HU-01: Consultar catálogo de libros
- Visualización de libros desde base de datos
- Uso de DataFrame en Streamlit
- Manejo de catálogo vacío

#### ✅ HU-03: Gestión de usuarios
- Registro de usuarios
- Listado de usuarios
- Validación de email duplicado

---

### ⚠️ Problemas encontrados
- Error en configuración inicial de Docker
- Endpoints no registrados correctamente en FastAPI
- Streamlit no detectaba nuevas páginas automáticamente

---

### 🔧 Soluciones aplicadas
- Corrección de `main.py` para incluir routers
- Reinicio de contenedores Docker
- Organización correcta de páginas en Streamlit

---

### 📌 Estado del proyecto
- Backend completamente funcional
- API operativa y probada en `/docs`
- Frontend conectado correctamente

---

### 🔜 Próximos pasos
- Implementar sistema de préstamos
- Mejorar interacción entre usuarios y libros






## 📅 Daily 2

### 🎯 Objetivo del día
Completar la lógica principal del sistema de biblioteca e implementar las funcionalidades clave de préstamo.

---

### 🚀 Historias de usuario implementadas

#### ✅ HU-04: Realizar préstamo de libro
- Selección de usuario y libro disponible
- Validación de disponibilidad del libro
- Asociación libro-usuario
- Actualización automática del estado del libro

#### ✅ HU-05: Devolver libro
- Implementación de devolución de préstamos
- Uso de endpoint PATCH
- Actualización de disponibilidad del libro

#### 🔧 Mejora HU-05
- Eliminación de usuario fijo
- Selección dinámica de usuario
- Filtrado de préstamos activos
- Mejora de experiencia de usuario

#### ✅ HU-07: Búsqueda de libros
- Campo de búsqueda en catálogo
- Filtrado por título o autor
- Búsqueda parcial e insensible a mayúsculas
- Mensaje cuando no hay resultados

---

### ⚠️ Problemas encontrados
- Uso inicial de formularios sin conexión real
- Página de préstamos utilizando IDs manuales
- Necesidad de mejorar UX en devoluciones

---

### 🔧 Soluciones aplicadas
- Refactor completo de la pantalla de préstamos
- Uso de selectores dinámicos en lugar de inputs manuales
- Integración completa con backend real

---

### 📌 Estado del proyecto
- Sistema completo de biblioteca funcional:
  - libros
  - usuarios
  - préstamos
  - devoluciones
  - búsqueda

---

### 🔜 Próximos pasos
- HU-06: Historial de préstamos (objetivo notable)
- HU-08: Visualización avanzada (objetivo sobresaliente)






## 📅 Daily 3

### 🎯 Objetivo del día
Añadir testing automatizado, configurar integración continua y cerrar los requisitos de la metodología XP.

---

### 🧱 Trabajo realizado

#### 🔹 Testing con pytest
- Creación de carpeta de tests (`tests/`)
- Implementación de tests básicos:
  - Creación de libro
  - Creación de usuario
  - Validación de usuario duplicado
  - Creación de préstamo
- Uso de `TestClient` de FastAPI para pruebas de endpoints
- Solución de errores:
  - Problema de importación (`ModuleNotFoundError`)
  - Ajuste de PYTHONPATH mediante `conftest.py`
  - Corrección de duplicados usando emails únicos dinámicos

---

#### 🔹 Integración Continua (CI)
- Configuración de GitHub Actions
- Creación de workflow en `.github/workflows/ci.yml`
- Automatización de ejecución de tests en cada push
- Verificación del correcto funcionamiento desde la pestaña *Actions*

---

#### 🔹 Metodología XP
- Simulación de Pair Programming mediante commits con `Co-authored-by`
- Aplicación de refactoring continuo en funcionalidades previas
- Uso de desarrollo incremental (por historias de usuario)
- Integración continua mediante GitHub Actions


---

### ⚠️ Problemas encontrados
- Fallo en imports al ejecutar pytest dentro de Docker
- Conflictos con datos duplicados en base de datos
- Error al hacer push por divergencia con repositorio remoto

---

### 🔧 Soluciones aplicadas
- Uso de `conftest.py` para ajustar rutas de importación
- Generación de datos dinámicos en tests (`uuid`)
- Uso de `git pull --rebase` para sincronizar cambios
- Corrección del flujo de commits y pushes

---

### 📌 Estado del proyecto
- Sistema completo de gestión de biblioteca funcional
- Testing automatizado implementado
- CI activo en GitHub
- Metodología XP aplicada en el desarrollo

---

### 🔜 Próximos pasos
- HU-06: Historial de préstamos (objetivo notable)
- HU-08: Visualización avanzada (objetivo sobresaliente)



## 📅 Daily 4

### 🎯 Objetivo del día
Completar la HU-06 (historial de préstamos) y desarrollar la HU-08 (visualización avanzada del sistema), asegurando el correcto funcionamiento y resolviendo incidencias técnicas.

---

### 🧱 Trabajo realizado

#### 🔹 HU-06: Historial de préstamos
- Desarrollo de la página `Loan History` en Streamlit
- Integración con el endpoint `/loans/user/{user_id}`
- Implementación de:
  - Selector de usuario dinámico
  - Visualización de préstamos asociados
- Mejora de la interfaz:
  - Transformación de datos en tabla mediante pandas
  - Formateo de fechas para mayor legibilidad
  - Representación visual del estado del préstamo (activo/devuelto)

---

#### 🔹 HU-08: Visualización avanzada
- Desarrollo de la página `Loan Calendar`
- Implementación de:
  - Agrupación de préstamos por fecha
  - Cálculo de métricas mediante `groupby`
  - Visualización gráfica (barras) de préstamos activos y devueltos
  - Tabla detallada de eventos
- Mejora de la experiencia de usuario:
  - Separación clara entre resumen, gráfico y detalle

---

### 🐞 Problemas encontrados

- Errores de indentación en Python que impedían la ejecución del script
- Inconsistencias en la estructura de datos al trabajar con pandas
- Conflictos en la transformación de columnas al renombrar atributos
- Problemas de ejecución en contenedores Docker ya activos
- Dificultades en la sincronización del entorno entre distintos miembros del equipo

---

### 🔧 Soluciones aplicadas

- Reestructuración del código respetando correctamente la indentación de bloques
- Ajuste del tratamiento de DataFrames para evitar conflictos entre columnas
- Separación clara de las transformaciones de datos para evitar ambigüedades
- Uso adecuado de comandos Docker (`down`, `restart`) según el contexto
- Mejora del flujo de trabajo colaborativo mediante `git pull` y `git push`

---

### 📌 Estado del proyecto

- HU-06 completada y funcional
- HU-08 completada con visualización avanzada
- Sistema completamente operativo
- Arquitectura estable y bien integrada
- Metodología XP aplicada correctamente

---

### 🔜 Próximos pasos

- Revisión final del sistema
- Validación completa de funcionalidades
- Preparación de la defensa del proyecto
- HU-09 y HU-10



## 📅 Daily 5

## Asistentes
- Pepe Otero
- Jaime Carrasco
- Jaime Escriva
- Hugo Dominguez
- César González

---

## Qué hemos hecho hoy

- Continuamos el desarrollo de las HU-09 y HU-10 del proyecto Gestor de Bibliotecas.
- Implementamos un sistema de logging centralizado utilizando distintos niveles (`INFO` y `WARNING`).
- Añadimos excepciones personalizadas para controlar errores relacionados con usuarios, libros y préstamos.
- Refactorizamos los servicios y routers para mejorar la robustez del backend.
- Probamos manualmente distintos casos desde Streamlit y FastAPI `/docs`:
  - préstamos duplicados,
  - devoluciones repetidas,
  - emails duplicados,
  - validaciones de formularios.
- Implementamos un decorador propio para registrar acciones importantes del sistema.
- Añadimos propiedades con `@property` en el modelo `Loan` para encapsular el estado de los préstamos.
- Implementamos un generador con `yield` para procesar libros de forma eficiente.
- Documentamos en el README la aplicación de los principios SOLID y las técnicas avanzadas utilizadas.
- Ejecutamos tests automáticos con Pytest y configuramos `pytest-cov` para medir cobertura.
- Alcanzamos un 80% de cobertura total del proyecto.

---

## Problemas encontrados

- Durante la integración de logging y excepciones aparecieron errores internos en varios servicios del backend.
- Se detectaron conflictos entre cambios en servicios y routers, lo que provocó fallos en préstamos y usuarios.
- Fue necesario restaurar el repositorio al último commit estable mediante `git reset --hard` para recuperar un estado funcional antes de continuar con la refactorización.
- También aparecieron problemas de sincronización y reinicio de contenedores Docker durante algunas pruebas.

---

## Cómo los resolvimos

- Se rehizo la implementación de HU-09 de forma incremental y por bloques pequeños.
- Probamos cada modificación individualmente antes de continuar con la siguiente.
- Reiniciamos y reconstruimos contenedores Docker para validar correctamente cada cambio.
- Verificamos logs y endpoints desde FastAPI `/docs` para comprobar el comportamiento esperado del sistema.




## 📅 Daily 5.2

## Fecha
07/05/2026

## Asistentes
- Pepe Otero
- Jaime Carrasco
- Jaime Escriva
- Hugo Dominguez
- César González

---

## Qué hicimos
- Añadimos PostgreSQL como tercer contenedor Docker.
- Ejecutamos tests de integración y comprobamos el coverage.
- Mejoramos y rediseñamos la interfaz principal de Streamlit.
- Creamos nuevas branches para desarrollar mejoras visuales y cambios avanzados sin dañar la versión estable del proyecto.

---

## Reflexión
Nos dimos cuenta bastante tarde del potencial que tenía mejorar el frontend del proyecto. Durante casi todo el desarrollo nos centramos principalmente en la funcionalidad, arquitectura, testing y backend, dejando el diseño visual como algo secundario o extra.

Al empezar a rediseñar la interfaz vimos que realmente era bastante sencillo mejorar muchísimo el aspecto visual utilizando HTML, CSS y herramientas de IA, algo que además solemos hacer habitualmente para crear dashboards y páginas visuales más modernas.

También decidimos crear nuevas branches para probar cambios importantes sin afectar al trabajo estable que ya teníamos realizado, algo que nos permitió experimentar con más seguridad y trabajar de una forma más profesional.

Consideramos que fue un error por nuestra parte no dedicar más tiempo antes al frontend, ya que con relativamente pocos cambios el proyecto pasó de tener una interfaz muy básica a verse mucho más profesional y completo.

---

## Qué haremos después
- Finalizar y preparar la defensa del proyecto.
