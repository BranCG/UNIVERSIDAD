
from CONEX.conex import conex
from datetime import datetime
import traceback
conection = conex()
import json
from faker import Faker  #libreria de nueva funcionalidad.


# Módulo que contiene funciones para interactuar con la base de datos MySQL. 
# Incluye funciones para registrar 
# usuarios, buscar claves, mostrar profesores, insertar, eliminar, actualizar y buscar profesores en la base de datos.
def validar_rut(rut):  #Para validar rut, lo recicle de mi codigo eva 2.
    return rut.isdigit() and (len(rut) == 8 or len(rut) == 9)


# FUNCIONES PARA LOGIN-------------------------------------------------------------------------------------------
# Aca recibimos los atributos desde la clase acceso y se hace la query para insertar.
def registroUsuarios(usuario, correo, clave, conection):
    sql = "insert into login (usuario, correo, clave, fecha) values (%s,%s,%s,%s)"
    try:
        fecha = datetime.now() #Fecha actual y se almacena
        cursor = conection.cursor() #Cursor se utiliza para ejecutar querys en la base de datos.
        cursor.execute(sql, (usuario, correo, clave, fecha))  #Se ejecuta la consulta SQL con los valores proporcionados como parámetros.
        conection.commit()  # Se confirman los cambios en la base de datos.
        filas = cursor.rowcount     #Se obtiene el número de filas afectadas por la operación de inserción.
        if filas > 0:
            print("¡¡Usuario ingresado con exito!!")   #Si al menos 1 fila fue afectada se ejecuta el print.
        else:
            print("No hay cambios")
    except:
        print(traceback.print_exc())    #Imprime información detallada sobre la excepción que ocurrió.

# Acá se comparan las claves encriptadas la que esta almacenada con la que se ingresa.
def buscarClave(usuario, conection):  #Busca la clave en la base de datos .
    sql = "select clave from login where usuario = %s" #Variable sql toma este valor SELECT
    try:
        usuario_tupla = (usuario,)      #Tupla de un solo elemento.
        usuario_str = str(usuario_tupla[0]) #Se convierte el primer elemento de la tupla (usuario_tupla) a una cadena y se guarda en la variable usuario_str. 
        cursor = conection.cursor() 
        cursor.execute(sql, (usuario_str,))
        resultado = cursor.fetchone() #Se obtiene la primera fila del resultado de la consulta y se guarda en la variable resultado.
        return resultado[0] #Se devuelve el valor de la primera columna de la fila obtenida. En este caso, sería la clave del usuario.

    except:
        print(traceback.print_exc())


# FUNCIONES PARA PROFESOR-------------------------------------------------------------------------------------------
# Acá hacemos la consulta para listar profesores con select.
def mostrarProfesor(conection):
    try:
        conection = conex()   #Se abre la conexión.
        cur = conection.cursor()
        cur.execute("SELECT rut, nombre, edad, especialidad FROM profesor")  #query para mostrar tabla.
        result = cur.fetchall()

        print("RUT      NOMBRE        EDAD      ESPECIALIDAD ")
        for row in result:
            print("{:<9} {:<12} {:<9} {}".format(row[0], row[1], row[2], row[3])) #Lo busque para listar ordenado.

    except Exception as ex:
        conection.rollback()
        print("Error:", ex)
        traceback.print_exc()


#Se insertan los datos que trae la clase profesor al instanciar con sus input en datos_profesor.
def insertarProfesor(rut, nombre, edad, especialidad):
    sql = "INSERT INTO profesor (rut, nombre,  edad, especialidad) VALUES (%s, %s, %s, %s)"
    try:
        conection = conex() #Abrir conexión.
        cur = conection.cursor()
        
        cur.execute("SELECT * FROM profesor WHERE rut = %s", (rut,)) #Verificar si el profesor con el rut proporcionado existe
        result = cur.fetchone()
        if result:
            print("¡Error, profesor ya existe en nuestros registros!")
        else:
            conexion = conex()
            cursor = conexion.cursor()
            cursor.execute(sql, (rut, nombre, edad, especialidad))
            conexion.commit()
            filas = cursor.rowcount
            if filas > 0:
                print("¡Profesor ingresado con exito!")
            else:
                print("No se presentaron cambios")
    except:
        print(traceback.print_exc())
        conection.close() #cierro la conexion.


def eliminarProfesor(rut, conection):
    try:
        conection = conex()
        cur = conection.cursor()
        cur.execute("SELECT * FROM profesor WHERE rut = %s", (rut,)) # Verificar si el profesor con el rut proporcionado existe
        result = cur.fetchone()

        if result:
            # El profesor existe, realizar la eliminación
            cur.execute("DELETE FROM profesor WHERE rut = %s", (rut,))
            conection.commit()
            print("Profesor eliminado con éxito.")
        else:
            print("¡No se encontro profesor con rut asociado.")

    except Exception as ex:
        conection.rollback()
        print("Error:", ex)
        traceback.print_exc()
        conection.close()


def updateProfesor(rut, nuevo_nombre, nueva_edad, nueva_especialidad, conection):
    sql = "SELECT * FROM profesor WHERE rut = %s"
    try:
        conection = conex()
        cur = conection.cursor()
        cur.execute(sql, (rut,)) #Verificar si el profesor con el rut proporcionado existe.
        result = cur.fetchone()
        if result:
            #El profesor existe, realizar la actualización.
            cur.execute("UPDATE profesor SET nombre = %s, edad = %s, especialidad = %s WHERE rut = %s",
                        (nuevo_nombre, nueva_edad, nueva_especialidad, rut))
            conection.commit()
            print("Profesor actualizado con éxito.")
        else:
            print("No se encontró un profesor con el RUT proporcionado.")

    except Exception as ex:
        conection.rollback()
        print("Error:", ex)
        traceback.print_exc()
        conection.close()


def BuscarProfesor(rut, conection):
    sql = "SELECT rut, nombre, edad, especialidad FROM Profesor WHERE rut = %s"
    try:
        conection = conex()  
        cur = conection.cursor()
        cur.execute(sql, (rut,))
        result = cur.fetchone()

        if result is not None:
            print("RUT      NOMBRE        EDAD      ESPECIALIDAD ")
            print("{:<9} {:<12} {:<9} {}".format(result[0], result[1], result[2], result[3]))#Lo busque para listar ordenado.

        else:
            print("No se encontró un profesor con el RUT proporcionado.")

    except Exception as ex:
        conection.rollback()
        print("Error:", ex)
        traceback.print_exc()
    finally:
        pass


def buscarRut(rut, conection):
    sql = "SELECT rut from profesor WHERE rut = %s"

    try:
        cur = conection.cursor()
        cur.execute(sql, (rut,))
        result = cur.fetchone()

        if result is not None:
            return True
        else:
            pass


    except:
        print("")


# FUNCIONES PARA JSON-------------------------------------------------------------------------------------------

# Importar
def leerJson():
    try:
        ruta = 'Profesores.json'
        with open(ruta) as file:
            data = json.load(file)
    except FileNotFoundError:
        print("¡ESPERA, PRIMERO DEBES EXPORTAR EL ARCHIVOOO!")
    
    else:
        for y in data['Datos']:
            print(y)


# AGREGUE FUNCIONALIDAD DE QUE ANTES DE INSERTAR A LA BD, PRIMERO VERIFIQUE SI HAY RUT YA EXISTENTES
# SI HAY DATO RUT DUPLICADO, NO HARA LA INSERCIÓN Y NO IMPORTARA archivo Profesores.json
def importarProfesoresJson():
    try:
        lista = []
        ruta = 'Profesores.json'

        with open(ruta) as file:
            data = json.load(file)   #Serializacion, diccionario a string.

        for x in data['Datos']:
            # Verificar si el RUT ya existe en la base de datos
            if not buscarRut(x["rut"], conection):
                lista.append(
                    (x["rut"], x["nombre"], x["edad"], x["especialidad"]))
            else:
                print(f"¡Error!: El RUT {x['rut']} ya está registrado. No se importara archivo JSON.")

        if lista:
            sql = "INSERT INTO profesor (rut, nombre, edad, especialidad) VALUES (%s, %s, %s, %s)"
            conexion = conex()
            cursor = conexion.cursor()
            cursor.executemany(sql, lista)
            conexion.commit()
            filas = cursor.rowcount
            if filas > 0:
                print("Datos agregados satisfactoriamente")
            else:
                print("No se realizaron cambios")

    except Exception as e:
        print(f"Error al insertar JSON, primero debes exportar: {e}")


def prepararExportarJson():
    lista = []  #Se crean tres listas vacías: lista, lista2, y un diccionario vacío dic.
    lista2 = []
    dic = {}
    c = conex()

    try:
        cursor = c.cursor() #Se crea un cursor para ejecutar consultas SQL en la base de datos.
        cursor.execute("SELECT rut,nombre,edad,especialidad FROM profesor") #Se hace un select
        result = cursor.fetchall() #Lo que salga del select se almacena en result mediante el fetchall.
        # convierte filas en objetos

        for u in result:
            # lista de tuplas llamada lista donde cada tupla representa un profesor con sus datos.
            profesor = (u[0], u[1], u[2], u[3])
            lista.append(profesor)
        # se itera sobre esta lista de tuplas y se crea una nueva lista llamada lista2, 
        #donde cada elemento es un diccionario que representa un profesor con claves como
        for w in lista:
            lista2.append({'rut': w[0], 'nombre': w[1],'edad': w[2], 'especialidad': w[3]})
            dic['Datos'] = lista2 #Se asigna esta lista de diccionarios al diccionario dic con la clave 'Datos'.

        print("Exportación OK")
        exportarProfesores("Profesores.json", dic)
# Se llama a la función exportarProfesores con dos argumentos: el nombre del archivo ("Profesores.json") y 
# el diccionario dic que contiene los datos de los profesores.

    except Exception as ex:
        print(ex)

    return lista
# Finalmente, la función retorna la lista lista que contiene las tuplas con los datos de los profesores.


def exportarProfesores(archivo, obj):
    resu = {}
    try:
        out_file = open(archivo, "w", encoding="utf-8")
        json.dump(obj, out_file, indent=4)  #Deserializacion, str a diccionario, dump objeto + archivo.
        out_file.close()
        resu["mensaje"] = "Datos exportados satisfactoriamente"

    except Exception as ex:
        resu["Error"] = ex




# FUNCIONES ADICIONAL FAKER-------------------------------------------------------------------------------------------


def leerFakerJson():
    try:
        ruta = 'ProfesoresFaker.json'
        with open(ruta) as file:
            data = json.load(file)  # Serializacion, diccionario a string.
    except FileNotFoundError:
        print("¡ESPERA, PRIMERO DEBES EXPORTAR EL ARCHIVOOO!")
    else:
        for y in data['Datos']: 
            print(y)


def importarFaker():
    try:
        datos_json = []
        ruta = 'ProfesoresFaker.json'

        with open(ruta) as file:
            datos_json = json.load(file)  #Serializacion, diccionario a string.

        datos_insertar = []

        for x in datos_json['Datos']:
            # Verificar si el RUT ya existe en la base de datos
            if not buscarRut(x["rut"], conex()):
                datos_insertar.append(
                    (x["rut"], x["nombre"], x["edad"], x["especialidad"]))
            else:
                print(f"¡Error!: El RUT {x['rut']} ya está registrado. No se importará el archivo JSON.")

        if datos_insertar:
            sql = "INSERT INTO profesor (rut, nombre, edad, especialidad) VALUES (%s, %s, %s, %s)"
            conexion = conex()
            cursor = conexion.cursor()
            cursor.executemany(sql, datos_insertar)
            conexion.commit()
            filas = cursor.rowcount
            if filas > 0:
                print("Datos agregados satisfactoriamente")
            else:
                print("No se realizaron cambios")

    except Exception as e:
        print(f"Error al insertar JSON, primero debes exportar: {e}")


def exportarFaker(archivo, obj):
    resu = {"mensaje": "", "Error": ""} #Este diccionario lo utilizo para almacenar mensajes de salida sobre el resultado de la operación.
    try:
        with open(archivo, "w", encoding="utf-8") as out_file:
            json.dump(obj, out_file, indent=4)  #Deserializacion, str a diccionario, dump objeto + archivo.
        resu["mensaje"] = "Datos exportados satisfactoriamente"

    except Exception as ex:
        resu["Error"] = f"Error al exportar datos: {ex}"

    return resu


def prepararExportarFaker():
    data = []
    data2 = []
    dic = {}
    c = conex()

    try:
        cursor = c.cursor()
        cursor.execute("SELECT rut, nombre, edad, especialidad FROM profesor")
        result = cursor.fetchall()

        for i in range(100):  #cargo 100 datos falsos.
            profesor = Faker() 
            rut = profesor.unique.random_number(digits=9) #8 digitos random para el rut.
            data.append((rut, profesor.name(), profesor.random_int(min=25, max=65), profesor.job())) 
            #Aca condicionamos los datos que traemos de fake, datos randoms.
        for w in data:
            data2.append({'rut': w[0], 'nombre': w[1],'edad': w[2], 'especialidad': w[3]})
            dic['Datos'] = data2

        print("Exportación OK")
        exportarFaker("ProfesoresFaker.json", dic)

    except Exception as ex:
        print(f"Error al preparar exportación: {ex}")

    return data


