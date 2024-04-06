#usuario con md5 para login.
from MENU.menu import Menu
from CRUD.encripteitor import decode
from CRUD.crud import *
from CLASES.acceso import Acceso

# llaves para ingresar al admin principal
# user: brandon
# pass: 1234
# Sistema de login simple. El usuario puede registrarse, y luego iniciar sesión ingresando su usuario y contraseña. 
# Si las credenciales son correctas, el usuario tiene acceso al menú principal.

while True:

    print("\n----Login----")
    print("1- Registrar usuario")
    print("2- Login ")
    print("0- Exit ")
    op = input("Ingrese opción: ")

    if op == "1":
        a = Acceso() 
        a.registroUsuarios() #Instancia la clase Acceso para usar luego metodo registroUsuarios.

    elif op == "2":
        usuario = input("Ingrese usuario: ")
        clave = input("Ingrese su contraseña: ")
        acceso = decode(clave, buscarClave(usuario, conection)) 
        if acceso == True: #Si el acceso es exitoso, deja entrar al menu.
            m = Menu()
        else:
            print("Usuario y/o contraseña invalida")
    elif op == "0":
        print("¡Hasta luego, saludos!")
        break


