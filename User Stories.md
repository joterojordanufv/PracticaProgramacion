Historias de usuario.

# HU-01 Consultar el catálogo de libros
Como usuario de la biblioteca,
quiero ver el listado completo de libros con su título, autor, género y disponibilidad,
para saber qué libros puedo pedir prestados.
Criterios de aceptación

Se muestra una tabla con todos los libros del sistema: título, autor, género y si está disponible o no.
Si no hay libros, aparece un mensaje informativo en lugar de una tabla vacía.
La información está siempre actualizada: refleja el estado real del sistema en ese momento.

# HU-02 Registrar un nuevo libro
Como bibliotecario,
quiero añadir un nuevo libro al catálogo introduciendo su título, autor y género,
para mantener el inventario actualizado.
Criterios de aceptación

Hay un formulario para dar de alta un libro con los campos título, autor y género.
El libro aparece en el catálogo inmediatamente después de añadirlo.
Si se deja algún campo vacío, el sistema avisa con un mensaje claro y no guarda nada.


# HU-03 Gestionar el perfil de un usuario

Como bibliotecario,
quiero crear y consultar usuarios registrados con su nombre y correo electrónico,
para poder asociarlos después a préstamos.
Criterios de aceptación

Hay un formulario para registrar un usuario con nombre y email.
Se puede consultar el listado completo de usuarios registrados.
Si se intenta registrar un email que ya existe, el sistema lo avisa con un mensaje claro y no crea el duplicado.

# HU-04 Realizar un préstamo de libro
Como usuario de la biblioteca,
quiero solicitar el préstamo de un libro disponible,
para poder llevármelo a casa.
Criterios de aceptación

Se puede solicitar el préstamo indicando qué libro y qué usuario lo solicita.
Si el libro ya está prestado, el sistema lo indica claramente y no permite el préstamo.
Si el libro o el usuario no existen, el sistema avisa con un mensaje descriptivo.
Tras el préstamo, el libro aparece como no disponible en el catálogo.


# HU-05  Devolver un libro prestado
Como usuario de la biblioteca,
quiero registrar la devolución de un libro que tengo en préstamo,
para que quede disponible de nuevo para el resto.
Criterios de aceptación

Se puede registrar la devolución de un préstamo activo.
Tras la devolución, el libro aparece de nuevo como disponible en el catálogo.
Si se intenta devolver un préstamo que no existe o ya estaba cerrado, el sistema lo indica con un mensaje claro.


# HU-06 Consultar el historial de préstamos de un usuario
Como bibliotecario,
quiero ver todos los préstamos, activos y pasados, de un usuario concreto,
para hacer seguimiento de su actividad en la biblioteca.
Criterios de aceptación

Se puede buscar un usuario y ver su historial completo de préstamos.
Cada entrada del historial muestra el título del libro, la fecha en que se prestó y la fecha en que se devolvió (si aplica).
Los préstamos activos se distinguen visualmente de los ya cerrados.
Si el usuario no tiene historial, aparece un mensaje informativo, no un error.

# HU-07  Buscar libros por título o autor
Como usuario de la biblioteca,
quiero buscar libros filtrando por título o autor,
para encontrar rápidamente lo que me interesa sin recorrer todo el catálogo.
Criterios de aceptación

El catálogo tiene un campo de búsqueda que filtra por título o por autor.
La búsqueda funciona aunque se escriba en minúsculas, mayúsculas o solo una parte del nombre ("orwell" encuentra "George Orwell").
Si la búsqueda no devuelve resultados, la interfaz lo indica claramente.


# HU-08  Ver el historial de préstamos en un calendario
Como bibliotecario,
quiero visualizar los préstamos de un usuario en un calendario,
para entender de un vistazo su actividad a lo largo del tiempo sin tener que leer una lista de fechas.
Criterios de aceptación

El historial de préstamos de un usuario puede verse en un calendario interactivo, donde cada préstamo aparece como un evento con el título del libro y su rango de fechas.
Los préstamos activos se muestran de forma diferente a los ya devueltos.
Se puede navegar entre meses en el calendario.

# Prioridad

## Mínima imprescindible para la práctica
HU-02 > HU-01 > HU-03 > HU - 04 > HU-05 >  HU-07

## Para optar al Notable

HU-06

## Para optar al Sobresaliente

HU - 08