# * DIFICULTAD EXTRA (opcional):
# * Crea una agenda de contactos por terminal.
# * - Debes implementar funcionalidades de búsqueda, inserción, actualización
# *   y eliminación de contactos.
# * - Cada contacto debe tener un nombre y un número de teléfono.
# * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
# *   y a continuación los datos necesarios para llevarla a cabo.
# * - El programa no puede dejar introducir números de teléfono no númericos y con más
# *   de 11 dígitos (o el número de dígitos que quieras).
# * - También se debe proponer una operación de finalización del programa.

#! PUNTOS EXTRAS ESTA PARTE SE AÑADE A CURSO INTEMEDIO
#?Retos adicionales (opcionales):
#*Persistencia de datos:
#Guarda la agenda en un archivo (por ejemplo, agenda.txt) para que los contactos no se pierdan al cerrar el programa.
#Usa el módulo json para guardar y cargar los datos en formato JSON.

#*Interfaz más amigable:
#Usa colores o tablas para mostrar los contactos de manera más organizada.

#*Búsqueda avanzada:
#Permite buscar contactos por parte del nombre (por ejemplo, buscar "Ju" para encontrar "Juan").

agenda = {
    "nombre":None,
    "apellido":None,
    "ciudad":None,
    "numero":None
}

def get_nombre(nombre):
    nombre = agenda['nombre']
    return nombre

def get_apellido(apellido):
    apellido = agenda['apellido']
    return apellido

def get_ciudad(ciudad):
    ciudad = agenda['ciudad']
    return ciudad

def get_numero(numero):
    numero = agenda['numero']
    return numero

def set_nombre(_nombre):
    if isinstance(_nombre, str):
        agenda['nombre'] = _nombre
    else:
        print("El nombre debe ser una cadena de texto")

def set_apellido(_apellido):
    if isinstance(_apellido, str):
        agenda['apellido'] = _apellido
    else:
        print("El apellido debe ser una cadena de texto")

def set_ciudad(_ciudad):
    if isinstance(_ciudad, str):
        agenda['apellido'] = _ciudad
    else:
        print("El apellido debe ser una cadena de texto")

def set_numero(_numero):
    if _numero.isdigit() or len(_numero) > 11 :
        print("Numero de telefono no es valido, debe tener solo digitos y que sean menos de 11")
    else:
        agenda['numero'] = _numero
    print(f"Contacto '{_numero}' agregado correctamente")


while True:
    # Mostrar menú
    print("1. Buscar contacto")
    print("2. Insertar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        # Buscar contacto
        pass
    elif opcion == "2":
        # Insertar contacto
        add_nombre = input("Ingresa el nombre: ")
        add_apellido = input("Ingrese el apellido: ")
        add_cuidad = input("Ingrese la cuidad: ")
        
        add_numero = input("Ingrese el numero: ")            
        pass
    elif opcion == "3":
        # Actualizar contacto
        pass
    elif opcion == "4":
        # Eliminar contacto
        pass
    elif opcion == "5":
        # Salir del programa
        print("Has salido")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")