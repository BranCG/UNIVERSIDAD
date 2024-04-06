# Esta clase no se usara en la base de datos.
from persona import Persona

class Estudiante(Persona):
    def __init__(self, rut, nombre,  edad, calificacion, carrera):
        super().__init__(rut, nombre,  edad)
        self.calificacion = calificacion
        self.carrera = carrera

