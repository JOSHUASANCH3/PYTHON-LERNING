## Diccionario
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

## Lo que tiene mi libreria
my_other_dict = {"Nombre":"Joshua", "Apellido":"Sanchez", "Edad":25 }

my_dict = {"Nombre":"Joshua", 
           "Apellido":"Sanchez", 
           "Edad":25, 
           "Lenguajes": {"Python", "CSS", "HTMl"},
           1: 1.5
           }

print(my_other_dict)
print(my_dict)

##El numero de item que tiene mi libreria
print("En my_other_dict hay:" +str(len(my_other_dict)))
print("En my_dict hay:" + str(len(my_dict)))

##Buscar dentro del diccionario algun dato que tenga
print(my_dict["Nombre"])

##Cambio el valor de item que hay en el diccionario
my_dict["Nombre"] = "German"
print(my_dict["Nombre"])

##Agregar un valor a mi diccionario
my_dict["Calle"] = "CalleProgramacion"
print(my_dict)

##Eliminar de manera especifica un valor dentro del diccionario
del my_dict["Calle"]
print(my_dict)

##Para comproar si un item esta en el diccionario
print("German" in my_dict)
print("Nombre" in my_dict)

##Claves del diccionario
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, ("Joshua", "Sanchez"))
print(my_new_dict)