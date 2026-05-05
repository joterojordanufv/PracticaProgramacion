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




