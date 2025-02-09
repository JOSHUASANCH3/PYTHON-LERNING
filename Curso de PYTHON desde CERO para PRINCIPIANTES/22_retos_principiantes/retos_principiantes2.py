
# * EJERCICIO:
# ?  - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
# *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia
print("Adiccion: ", 1 + 2) #3
print("Resta: ", 2 -1) #1
print("Multiplicacion: ", 2 * 3) #6
print("Multiplicacion: ", 2.5 * 3.6) #9 #! Se puede multiplicar decimales
print("Divison: ", 4 / 2) #2
print("Division sin resto: ", 7 // 2) #2
print("Modulos: ", 3 % 2) #1
print("Potenciacion:", 2 ** 3) # 9 = 2 * 2 * 2
# ? Crea ejemplos
# *   Condicionales, iterativas, excepciones...
# if condition
a = 3
if a > 0:
    print("A is a positive number")

#if else
a = 5
if a < 0:
    print("A is a negative number")
else:
    print("A is a positive number")

#if elif else
a = 0
if a > 0:
    print("A es un numero negativo")
elif a < 0:
    print("A es un numero positivo")
else:
    print("A es cero")# el resultado es cero

#If and Or logical operators
user = "James"
access_level = 3
if user == "admin" or access_level >= 4:
    print("Acceso Obtenido")
else:
    print("Acceso denegado") # el acceso esta denegado

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

