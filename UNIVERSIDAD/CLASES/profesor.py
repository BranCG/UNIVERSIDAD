from CLASES.persona import Persona
from CRUD.crud import *

# CRUD a la tabla profesor en MySQL, hereda de persona.
# Representa a un profesor con atributos adicionales como especialidad.
# Esta clase es la que funciona y maneja la interacción con la base de datos para el CRUD
# (Create, Read, Update, Delete) de profesores.
class Profesor(Persona):
    def __init__(self, rut, nombre, edad, especialidad):
        super().__init__(rut, nombre, edad)
        self.especialidad = especialidad


    def datos_profesor(self):   #Metodo para instanciar profesor.
        while True:
                rut = input("Ingresa RUT (SIN PUNTOS NI GUION, K REEMPLAZAR POR UN 0): ")
                if not validar_rut(rut):     #toma el rut y valida que cumpla condiciones de calidar_rut
                    print("Error: El RUT debe tener 8 o 9 dígitos y solo puede contener números.")
                    break
                else:    
                    nombre = input("Ingrese nombre del profesor: ").title()
                    try:
                        edad = int(input("Ingrese edad del profesor: "))
                    except ValueError:
                        print("¡Error!Ingresa valores númericos en edad, vuelve a intentarlo")
                    else:
                        especialidad = input("Ingrese especialidad del profesor: ").title()
                        self.__rut = rut
                        self.nombre = nombre
                        self.edad = edad
                        self.especialidad = especialidad
                        insertarProfesor(self.__rut, self.nombre, self.edad, self.especialidad)  # Llamar al método para insertar en la base de datos
                        break
        
    #algunas funciones de la eva2 para instanciar.
    #def mostrar_profesor(self):
        #print(f"Mi nombre es {self.nombre}, rut {self.obtener_rut()}, tengo {self.edad} años y mi especialidad es {self.especialidad}")




