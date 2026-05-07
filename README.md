# Práctica Final: Gestor de Bibliotecas 📚

¡Bienvenidos a la práctica final de Programación II!

Este proyecto es un esqueleto inicial para un sistema de **Gestión de Bibliotecas**. Vuestro objetivo es transformar este código base (que intencionadamente tiene ineficiencias y partes incompletas) en una aplicación robusta, mantenible y profesional, aplicando todas las buenas prácticas vistas durante el curso.

## 🎯 Objetivo

Desarrollar un sistema completo para gestionar el catálogo y préstamos de una biblioteca. Debéis demostrar vuestra capacidad para:
1.  **Entender y Refactorizar** código existente.
2.  **Diseñar** una arquitectura desacoplada y limpia.
3.  **Implementar** soluciones técnicas avanzadas (bases de datos, APIs, interfaces gráficas).
4.  **Trabajar en equipo** utilizando metodologías ágiles.

## Tecnologías Obligatorias

*   **Python 3.10+**: Lenguaje base.
*   **SQLAlchemy 2.x**: ORM para persistencia de datos (SQLite/PostgreSQL).
*   **Pytest**: Suite de tests con una cobertura mínima del **80%**.
*   **Streamlit**: Interfaz gráfica para usuarios y bibliotecarios.
*   **Git + GitHub**: Control de versiones y flujo de trabajo colaborativo.
*   **GitHub Actions**: CI/CD básico para ejecutar tests en cada push.

## Principios SOLID (Obligatorio)

---

## Principios SOLID aplicados

Durante la refactorización del proyecto se aplicaron los principios SOLID para mejorar la organización, mantenibilidad y escalabilidad del sistema.

### SRP — Single Responsibility Principle

Cada módulo del sistema tiene una única responsabilidad:

- Los routers de FastAPI se encargan únicamente de exponer los endpoints.
- Los services contienen la lógica de negocio.
- Los repositories gestionan el acceso a la base de datos.
- Los models representan las entidades persistentes mediante SQLAlchemy.
- Streamlit se limita a la interfaz gráfica y consume la API mediante peticiones HTTP.

Ejemplo: `BookService` contiene la lógica relacionada con libros, mientras que `BookRepository` se encarga exclusivamente del acceso a datos.

### OCP — Open/Closed Principle

El sistema está abierto a extensión pero cerrado a modificación.

La arquitectura permite añadir nuevas funcionalidades creando nuevos servicios, routers o repositorios sin modificar la lógica existente.

Ejemplo: se añadió el historial de préstamos y la visualización avanzada sin alterar el funcionamiento base de libros, usuarios y préstamos.

### LSP — Liskov Substitution Principle

Las clases y componentes del sistema mantienen comportamientos consistentes y predecibles.

Los servicios utilizan repositorios con métodos bien definidos, por lo que podrían sustituirse por otras implementaciones de persistencia sin afectar a la lógica de negocio principal.

Ejemplo: `BookRepository` podría ser reemplazado por otro repositorio que use PostgreSQL sin modificar el uso que hace `BookService`.

### ISP — Interface Segregation Principle

El sistema evita módulos excesivamente grandes o con responsabilidades mezcladas.

Cada repositorio y servicio expone únicamente las operaciones necesarias para su dominio:

- `BookRepository` gestiona libros.
- `UserRepository` gestiona usuarios.
- `LoanRepository` gestiona préstamos.

Esto evita que una parte del sistema dependa de métodos que no necesita.

### DIP — Dependency Inversion Principle

La lógica de negocio no depende directamente de la interfaz gráfica ni de detalles concretos de presentación.

Streamlit se comunica con FastAPI mediante HTTP, y los servicios trabajan a través de repositorios, separando las capas del sistema.

Esto permite modificar la interfaz o la persistencia sin afectar directamente a la lógica de negocio.

---

## Técnicas avanzadas implementadas

Además de la funcionalidad básica, se añadieron técnicas avanzadas para cumplir con los requisitos de calidad del proyecto:

### Logging

Se implementó un sistema de logging centralizado con distintos niveles:

- `INFO`: acciones correctas del sistema.
- `WARNING`: operaciones no válidas o intentos incorrectos.
- `ERROR`: reservado para errores inesperados.

### Excepciones personalizadas

Se crearon excepciones específicas para errores de dominio:

- `DuplicateEmailError`
- `BookNotFoundError`
- `BookNotAvailableError`
- `UserNotFoundError`
- `LoanNotFoundError`
- `LoanAlreadyReturnedError`

Esto permite gestionar errores de forma más clara y mantenible.

### Decoradores

Se implementó un decorador propio para registrar acciones importantes del sistema, como la creación de libros.

### Properties

Se utilizaron propiedades con `@property` en el modelo `Loan` para encapsular el estado del préstamo y exponerlo de forma legible.

### Generadores

Se implementó un generador con `yield` para procesar libros de forma eficiente y demostrar el uso de programación avanzada en Python.

---

## Metodología XP

El desarrollo siguió una metodología incremental basada en eXtreme Programming:

- Se realizaron commits frecuentes y semánticos.
- Se trabajó con pair programming reflejado mediante `Co-authored-by`.
- Se mantuvo un registro diario en `DAILYS.md`.
- Se aplicó refactoring continuo.
- Se añadieron tests con Pytest.
- Se configuró integración continua mediante GitHub Actions
---

##  Sistema de Evaluación Incremental

El peso de la práctica es del **35%** de la nota final. La evaluación es incremental:

### 1. Aprobado (5-6) - "Funcionamiento Básico"
*   El sistema permite listar libros, crear usuarios y gestionar préstamos básicos.
*   Uso correcto de Git (commits semánticos).
*   Tests unitarios básicos definidos y pasando (usando Mocks para aislar dependencias).
*   Código limpio y organizado.

### 2. Notable (7-8) - "Nos centramos en robustez y calidad"
*   **Todo lo del Aprobado, más:**
*   **Excepciones Personalizadas**: Gestión de errores robusta y tipada.
*   **Logging**: Sistema de logs con al menos 3 niveles (INFO, WARNING, ERROR).
*   **Refactorización del Backend**: Uso de `FastAPI` con **Enrutadores (APIRouter)** para organizar los endpoints.
*   **Optimización**: "Cachear" datos en Streamlit para mejorar el rendimiento.

### 3. Sobresaliente (9) - "Aplicamos principios de Ingeniería del Software"
*   **Todo lo del Notable, más:**
*   **Decoradores**: Uso justificado de decoradores propios.
*   **Properties**: Uso de `@property` para encapsulamiento pythonico.
*   **Context Managers**: Uso de `with ...` para gestión eficiente de recursos (sesiones DB, ficheros).
*   **Generadores**: Uso de `yield` para procesar grandes volúmenes de datos de forma eficiente.

### 4. Matrícula de Honor (10)
*   **Todo lo del Sobresaliente, más alguno de:**
*   Uso de una tecnología o técnica **no vista en clase**.
    *   *Ejemplo*: Tests de Integración/Sistema (probando endpoints con `TestClient` o BD en memoria).
    *   *Ejemplo*: Despliegue en la nube.
    *   *Ejemplo*: Uso de una base de datos NoSQL auxiliar.
* Incluir un tercer contenedor donde se encuentre la base de datos
* Sustituir docker compose por manifiestos de k8s
* ...

---

## Arquitectura del Proyecto (Estado Inicial)

El esqueleto actual es intencionadamente ineficiente.

*   `fastapi/`: Contiene el servidor API. Actualmente lee de un CSV (`books.csv`) en cada petición (¡Ineficiente!).
*   `streamlit/`: Interfaz gráfica básica. Código mezclado y poco modular.
*   `data/`: Directorio donde debéis implementar vuestros modelos de datos y conexión a BD. 

### Vuestra misión
1.  **Eliminar la dependencia del CSV**: Migrar a una base de datos real usando SQLAlchemy.
2.  **Separar responsabilidades**: Que la UI no hable directamente con la BD, sino a través de Servicios/API.
3.  **Dockerizar**: Mantener/Mejorar el `docker-compose.yml` para que todo arranque con un comando.

¡Mucho ánimo y a programar! 💻🔥
