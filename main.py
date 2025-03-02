# main.py
from Estudiante import Estudiante

list_student = []  # Lista para almacenar objetos de clientes

def registrar_estudiante():
    print('Se va a registrar un estudiante')
    name = input('Ingresar el nombre: ')
    address = input('Ingrese el dirección: ')
    age = input('Ingrese la edad: ')
    course=input('Ingresar el curso: ')

    estudiante = Estudiante(name, age, address,course)  # Creación de un objeto Cliente
    list_student.append(estudiante)  # Agregar estudiante a la lista
    print('\nEstudiante guardado con éxito\n')


def mostrar_estudiante():
    num = 1    
    if len(list_student) == 0:
        print("\nNo hay cliente en la lista.\n\n")
    else:
        print('\nSe va a mostrar un listado de estudiantes:\n')
        for estudiante in list_student:
            print(f'#{num}.')
            num += 1
            print(estudiante, "\n")
        print("Estudiantes listados en su totalidad con éxito.\n")
    
                
"""def eliminar_cliente(nombre):
        for cliente in list_clientes:
            if cliente.get_name().lower() == nombre.lower():
                list_clientes.remove(cliente)
                print(f"Cliente '{nombre}' eliminado con éxito.")
                return
        print(f"Cliente '{nombre}' no encontrado.")
        
def actualizar_contacto(nombre, new_phone):
        for cliente in list_clientes:
            if cliente.get_name().lower() == nombre.lower():
                try:
                    cliente.set_phone(new_phone)
                    print(f"El telefono de '{nombre}' fue actualizado a {new_phone}.")
                except ValueError as e:
                    print(f"Error: {e}")
                return
        print(f"Cliente '{nombre}' no encontrado.")
"""

while True:
    print('::: MENU :::')
    print("""    1. Registrar estudiante 
    2. Consultar Listado
    3. Actualizar estudiante
    4. Eliminar un estudiante 
    5. Salir""")
    op = input('Ingresa la opcion que desee ejecutar: ')
    
    if op == '1':
        registrar_estudiante()
        
    elif op == '2':
        mostrar_estudiante()
    
    elif op == '5':
        print('saliendo del sistemas')
        exit()
    else:
        print('opcion invalida')
    """elif op == '3':
       nombre = input("Ingresa el nombre del estudiante a actualizar: ")
       try:
                new_phone = int(input(f"Ingresa el nuevo telefono de '{nombre}': "))
                actualizar_contacto(nombre, new_phone)
       except ValueError:
                print("Error: el telefono debe ser un número.")
    elif op == '4':
         nombre = input("Ingresa el nombre del producto a eliminar: ")
         eliminar_cliente(nombre)
"""    


