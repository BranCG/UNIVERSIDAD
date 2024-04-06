from CRUD.encripteitor import encode, decode
from CRUD.crud import registroUsuarios
from CONEX.conex import conex
conection = conex()

# Clase que gestiona el registro de usuarios. Almacena la información de usuario, correo y clave en la base de datos.


class Acceso():
    def registroUsuarios(self): #Instanciamos objeto en esta clase para luego insertar con la funcion registroUsuarios
        usuario = input("Ingrese Usuario : ")
        email = input("Ingrese Correo : ")
        clave = input("Ingrese clave : ")
        registroUsuarios(usuario, email, encode(clave), conection) #se lleva la clave encriptada bajo "encode".
        #print(f"la clave encriptada es {encode(clave)}")   #ACon esta linea puedo conocer la clave encriptada como tal.
