# Esta clase no se usara en la base de datos, pero le pasa atributos a profesor.
class Persona:
    def __init__(self, rut, nombre, edad):
        self.__rut = rut  # Atributo privado
        self.nombre = nombre
        self.edad = edad

    def obtener_rut(self):
        return self.__rut

