##Practica de bucles

## While

my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print("Mi condicion es mayor o igual a 10")

print("La ejecucion continua")

##Segundo ejercicio
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15")
        break

    print(my_condition)
print("La ejecucion continua")
##termina el while

##For
my_list = [13, 14, 56, 54, 98, 1, 20]

##Inicio del for
for element in my_list:
    print(element)
##se termina el for

##Una tupla
my_tuple = (35, 1.77, "Joshua", "Sanchez", "Garay")
for element in my_tuple:
    print(element)

##Un set
my_set = {"Joshua", "Sanchez", 35}
for element in my_set:
    print(element)

##Un diccionario
my_dict = {
    "first_name": "Joshua",
    "last_name": "Sanchez",
    "age": 24,
    "country": "Nicaragua",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
for element in my_dict.values():
    print(element)
    if element == "age":
        continue
        print("Se ejecuta ")
        ##break
else:
    print("El bucle for ha finalizado")
