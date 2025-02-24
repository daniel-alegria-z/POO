from Estudiante import Estudiante

lista_estudiante=[]

def registrar_estudiante():
    print("Se va a registrar un estudiante")
    name=input("Ingrese el nombre del estudiante: ")
    age=input("Ingrese la edad del estudiante: ")
    address=input("Ingrese la dirección del estudiante: ")
    course=input("El curso es: ")

    estudiante=Estudiante(name, age, address, course)
    lista_estudiante.append(Estudiante)

    print("Estudiante registrado con éxito")
