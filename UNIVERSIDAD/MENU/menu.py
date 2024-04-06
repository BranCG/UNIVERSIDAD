from CLASES.profesor import *
from CRUD.crud import *
from CRUD.encripteitor import encode, decode
from CONEX.conex import conex
conection = conex()

# Clase que maneja la interfaz de usuario para realizar operaciones como 
# listar profesores, agregar, eliminar, actualizar, buscar y 
# realizar importación/exportación de datos desde/hacia un archivo JSON.
# Antes de insertar datos desde el archivo JSON a la base de datos, 
# se verifica si ya existen registros con el mismo RUT.
class Menu:
    def __init__(self):
        listaProfesores = []  # lista para guardar profesores.

        while True:
            print("\n----MENU UNIVERSIDAD----")
            print("1- Listar Profesor")
            print("2- Agregar un Profesor")
            print("3- Eliminar un Profesor")
            print("4- Actualizar datos del Profesor")
            print("5- Buscar profesor")
            print('6- Leer Archivos Json')
            print('7- Importar a Json') #Serializacion, de un diccionario a string.
            print('8- Exportar a Json') #Deserializacion, de un string a archivo json(diccionario).
            print("__________________________________________________________________________________________________________")
            print('"FUNCIONALIDAD ADICIONAL(PRIMERO EXPORTAR)" esta libreria permite cargar datos falsos de manera masiva.')
            print('9- LEER DATOS FAKER(100 datos)')# Se necesita descargar libreria faker para utilizar.
            print('10- IMPORTAR DATOS FAKER A BD')
            print('11- EXPORTAR DATOS FAKER A JSON')
            print("0- Salir")

            opcion = input("\nIngresa la opcion que desees ejecutar: ")
            print("")

            if opcion == "1":
                mostrarProfesor(conection)

            elif opcion == "2":
                p = Profesor("", "", 0, "")  #Instancio p desde la clase Profesor()
                nuevo_profesor = p.datos_profesor() #Uso funcion datos_profesor para perdir input"s al usuario.  
                listaProfesores.append(nuevo_profesor) #Guardo en la listaProfesores el objeto obtenido.

            elif opcion == "3":
                while True:
                    rut_eliminar = input("Ingrese el rut del profesor a eliminar(SIN PUNTOS NI GUION, K REEMPLAZAR POR UN 0): ")
                    if not validar_rut(rut_eliminar):# toma el rut y valida que cumpla condiciones de calidar_rut
                        print(
                            "Error: El RUT debe tener 8 o 9 dígitos y solo puede contener números.")
                        break
                    else:
                        eliminarProfesor(rut_eliminar, conection)
                        break

            elif opcion == "4":
                while True:
                    rut = input("Ingrese RUT a actualizar(SIN PUNTOS NI GUION, K REEMPLAZAR POR UN 0): ")
                    if not validar_rut(rut):  # Revisa si el rut cuenta con las condiciones.
                        print("Error: El RUT debe tener 8 o 9 dígitos y solo puede contener números.")
                    else:
                        encontrado = buscarRut(rut, conection) #Revisa si el rut existe en la bd
                        if encontrado:
                            nuevo_nombre = input("Ingrese el nuevo nombre del profesor: ").title()
                            try:
                                nueva_edad = int(input("Ingrese la nueva edad del profesor: "))
                            except ValueError:
                                print("¡Error!Ingresa valores númericos en edad, vuelve a intentarlo!")
                            else:
                                nueva_especialidad = input("Ingrese la nueva especialidad del profesor: ").title()
                                updateProfesor(rut, nuevo_nombre, nueva_edad, nueva_especialidad, conection) #Se envian input a la funcion en crud para luego insertar.
                                break
                        else:
                            print("No se encontró un profesor con el RUT proporcionado.")

            elif opcion == "5":
                while True:
                    rut = input("Ingrese RUT del profesor a buscar(SIN PUNTOS NI GUION, K REEMPLAZAR POR UN 0):")
                    if not validar_rut(rut):
                        print("Error: El RUT debe tener 8 o 9 dígitos y solo puede contener números.")
                        break
                    else:
                        BuscarProfesor(rut, conection)
                        break

            elif opcion == '6':
                print('Leer datos de JSON existentes\n')
                leerJson()        

            elif opcion == '7':
                print('Vamos a importar desde un JSON hacia la BD\n')
                importarProfesoresJson()    

            elif opcion == '8':
                print('Vamos a exportar a JSON')
                prepararExportarJson()    

            elif opcion == "9":
                print('Leer datos de FAKER JSON existentes\n')
                leerFakerJson()

            elif opcion == "10":
                print('Vamos a importar DATOS FAKER desde JSON hacia la BD\n')
                importarFaker()
            elif opcion == "11":
                print('Vamos a exportar DATOS FAKER a JSON\n ')
                prepararExportarFaker()

            elif opcion == "0":
                break
            else:
                print("Opción invalida(ingrese 1-11)")
