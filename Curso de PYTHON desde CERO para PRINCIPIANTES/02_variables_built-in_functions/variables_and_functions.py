# Variables
"""
Reglas de nombres de variables de Python

- Un nombre de variable debe comenzar con una letra o el carácter de subrayado
- Un nombre de variable no puede comenzar con un número
- Un nombre de variable solo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9 y _)
- Los nombres de las variables distinguen entre mayúsculas y minúsculas (firstname, Firstname, FirstName y 
    FIRSTNAME) son variables diferentes)
"""
# Ejemplos
# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
ccity = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}

#Ejemplo de uso de variables con print()
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

#Declaring Multiple Variable in a Line
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#Obteniendo datos con input() con variables
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

#Tipos de datos
# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Asabeneh'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set

"""
Casting: convertir un tipo de datos a otro tipo de datos. Usamos int(), float(), str(), list, set . 
Cuando hacemos operaciones aritméticas, los números de cadena deben convertirse primero a int o float; 
de lo contrario, devolverá un error.
"""
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

"""
Tipos de datos numéricos en Python:

Números enteros: números enteros (negativos, cero y positivos) Ejemplo: ... -3, -2, -1, 0, 1, 2, 3 ...

Números de coma flotante (números decimales) Ejemplo: ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

Ejemplo de números complejos: 1 + j, 2 + 4j, 1 - 1j
"""

#Terminado 
#Realizar ejericios