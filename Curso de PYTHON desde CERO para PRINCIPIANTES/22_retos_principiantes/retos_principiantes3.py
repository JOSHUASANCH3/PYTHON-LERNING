###     EJERCICIO:
# * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en PYTHON
#? Estructuras soportadas en python
#Listas (Lists), Tuplas (Tuples), Conjuntos (Sets), Diccinario (Dictionaries)

#! Lists
my_list = [1, 2, 3, 4]

#Insercion de datos
my_list.append(5) # Añade al final de la lista el numero 5
#[1, 2, 3, 4, 5]
my_list.insert(2, 10) # Añade el numero 10 en la posicion numero 2
#[1, 2, 10, 3, 4, 5]

#Borrar datos
my_list.remove(3) #Elimina el primer elemennto con el valor 3
#[1, 2, 10, 4, 5]
del my_list[0] #Elimina el elemento en la posicion 0
#[2, 10, 4, 5]


#Actualizacion
my_list[1] = 20 #Cambia el valor en la posicion 1 a 20
#[2, 20, 4, 5]

#Ordenacion
my_list.sort() #Ordena la lista de forma ascendente
#[2, 20, 4, 5]
my_list.sort(reverse=True) #Ordena la lista de forma descendente
print("Lista final", my_list)
#Lista final [20, 5, 4, 2]

#! Tuples
#? Las tuplas son colecciones ordenadas e inmutables (no pueden modificarse después de su creación).
my_tupla = [1, 2, 3, 4]

# Las tuplas no permiten inserción, borrado o actualización directamente
# Pero puedes convertirla a lista, modificarla y volver a tupla
lista_temp = list(my_tupla)
lista_temp.append(5)  # Añade un elemento
my_tupla = tuple(lista_temp)  # Convierte de nuevo a tupla

# Ordenación (necesitas convertir a lista)
lista_temp = list(my_tupla)
lista_temp.sort()
my_tuplaa = tuple(lista_temp)

print("Tupla final:", my_tupla)

#! Dictionaries
# Creación de un diccionario
my_dictionary = {
    "Nombre":"Joshua", 
    "Apellido":"Sanchez", 
    "Edad":25
    }

# Inserción
my_dictionary["Profesion"] = "Programador"  # Añade una nueva clave-valor
my_dictionary["Lenguaje_Favorito"] = "Python"
my_dictionary["Ciudad"] = "Managua"

# Borrado
del my_dictionary["Edad"]  # Elimina la clave "edad"
my_dictionary.pop("Ciudad", None)  # Elimina la clave "ciudad" si existe

# Actualización
my_dictionary["Nombre"] = "German"  # Cambia el valor de la clave "nombre"
my_dictionary["Apellido"] = "Garay"

# Ordenación (puedes ordenar por claves o valores)
diccionario_ordenado = dict(sorted(my_dictionary.items()))  # Ordena por claves

print("Diccionario final:", my_dictionary)
print("Diccionario ordenado por claves:", diccionario_ordenado)

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

#! PUNTOS EXTRAS
#?Retos adicionales (opcionales):
#*Persistencia de datos:
#Guarda la agenda en un archivo (por ejemplo, agenda.txt) para que los contactos no se pierdan al cerrar el programa.
#Usa el módulo json para guardar y cargar los datos en formato JSON.

#*Interfaz más amigable:
#Usa colores o tablas para mostrar los contactos de manera más organizada.

#*Búsqueda avanzada:
#Permite buscar contactos por parte del nombre (por ejemplo, buscar "Ju" para encontrar "Juan").

my_condition = True
agenda = {
    "nombre":None,
    "apellido":None,
    "ciudad":None,
    "numero":11111111
}

def is_number_int():
    if "numero" in agenda:
        dic_number = agenda["numero"]
        if dic_number.isdigit() and len(dic_number) <= 11:
            print("El numero es correcto")
        else:
            print("El numero es incorrecto")




print("Loop")

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
        pass
    elif opcion == "3":
        # Actualizar contacto
        pass
    elif opcion == "4":
        # Eliminar contacto
        pass
    elif opcion == "5":
        # Salir del programa
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")