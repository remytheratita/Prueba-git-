

class alumno:
    def __init__(self): #tiene un constructor
        self.nombre = "sin nombre" #propiedades
        self.apellido = "sin apellido"


    def __str__(self): #regresa a una cadena de caracteres del objeto
        return self.nombre + " " + self.apellido

