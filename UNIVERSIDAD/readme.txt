En general, el código sigue una estructura modular y utiliza 
conceptos de programación orientada a objetos para organizar la lógica del programa. 
Además, integra funciones para interactuar con una base de datos MySQL y realizar 
operaciones básicas de gestión de profesores. Siempre y cuando puedas ingresar
mediante un usuario y contraseña, la cual fue encriptada por md5 en la base de datos.



Los diferentes módulos interactúan de la siguiente manera para realizar 
las operaciones CRUD (Create, Read, Update, Delete) en la base de datos MySQL:

crud Módulo:
Contiene funciones que realizan operaciones CRUD específicas en la base de datos.

conex Módulo:
Contiene la función conex() que establece la conexión a la base de datos MySQL. 
Esta función es utilizada por otras partes del código que necesitan interactuar con la base de datos.

Profesor Clase:
Hereda de la clase Persona y tiene métodos que interactúan con la base de datos para 
realizar operaciones CRUD específicas para los profesores.
Los métodos relevantes incluyen insertarProfesor, eliminarProfesor, updateProfesor, 
mostrarProfesor, BuscarProfesor y buscarRut.

Menu Clase:
Crea instancias de la clase Profesor para realizar operaciones CRUD desde la interfaz de usuario.
Utiliza métodos de la clase Profesor para listar, agregar, eliminar, actualizar y buscar profesores.

Acceso Clase:
Tiene un método llamado registroUsuarios que interactúa con la base de datos para registrar nuevos usuarios. 
Este método se utiliza para registrar usuarios durante el proceso de registro.

encripteitor Módulo:
Contiene funciones para codificar y decodificar contraseñas. 
La codificación se utiliza antes de almacenar contraseñas en la base de datos, 
y la decodificación se utiliza durante el proceso de login para verificar las credenciales del usuario.

Interacción entre Módulos:
La clase Menu interactúa con la clase Acceso para manejar el registro de usuarios.
La clase Menu crea instancias de la clase Profesor para realizar operaciones CRUD en la base de datos.
Las funciones en el módulo crud interactúan con la base de datos utilizando la conexión 
proporcionada por el módulo conex.

En resumen, la coordinación entre estos módulos permite al sistema realizar operaciones CRUD 
en la base de datos MySQL de manera estructurada y modular, con funciones y clases específicas 
encargadas de diferentes aspectos de la lógica del programa.