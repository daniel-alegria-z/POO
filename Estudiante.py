from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, direccion, curso):
        super().__init__(nombre, edad, direccion)
        self.__curso = curso

    def get_curso(self):
        return self.__curso
    
    def set_curso(self, curso):
        self.__curso=curso

    
    def __str__(self):
        return f"Los datos del estudiante son los siguientes:\n{super().__str__()}\nY su curso es: {self.get_curso()} "