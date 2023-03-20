#List
"""
Hay cuatro tipos de datos de colección en Python:

Lista: es una colección ordenada y cambiable (modificable). Permite miembros duplicados.
Tupla: es una colección ordenada e inmutable o inmodificable (inmutable). Permite miembros duplicados.
Conjunto: es una colección desordenada, no indexada y no modificable, pero podemos agregar nuevos elementos al conjunto. No se permiten miembros duplicados.
Diccionario: es una colección desordenada, cambiable (modificable) e indexada. No hay miembros duplicados.
"""

#Como crear una 'List'
# Using list built-in function
lst = list()#syntax
empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0

#Using square brackets, []
lst = []
empty_list = [] # this is an empty list, no item in the list
print(len(empty_list)) # 0

#?Lists with initial values. We use len() to find the length of a list.
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

#?Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

#?Lists can have items of different data types
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types

#?Accessing List Items Using Positive Indexing
"""
Accedemos a cada elemento de una lista utilizando su índice. 
El índice de una lista comienza desde 0. La siguiente imagen muestra claramente dónde comienza el índice
"""
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

#?Accessing List Items Using Negative Indexing
"""
La indexación negativa significa comenzar desde el final, 
-1 se refiere al último elemento, -2 se refiere al penúltimo elemento.
"""
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango

#?Unpacking List Items
# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = lst
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

#?Slicing Items from a List
"""
Indexación positiva: podemos especificar un rango de índices positivos especificando el inicio, el final y 
el paso, el valor de retorno será una nueva lista. (valores predeterminados para 
inicio = 0, final = len (lst) - 1 (último elemento), paso = 1)
"""
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']

"""
Indexación negativa: podemos especificar un rango de índices negativos especificando el inicio, el final y 
el paso, el valor devuelto será una nueva lista.
"""
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']

#?Modifying Lists
    #List is a mutable or modifiable ordered collection of items. Lets modify the fruit list.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

#?Checking Items in a List
    #Checking an item if it is a member of a list using in operator. See the example below.
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

#?Adding Items to a List
    #To add item to the end of an existing list we use the method append().
# syntax
lst = list()
lst.append(item)
#Other example
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)

#?Inserting Items into a List
"""
Podemos usar el método insert() para insertar un solo elemento en un índice específico en una lista. 
Tenga en cuenta que otros elementos se desplazan a la derecha. Los métodos insert() toman dos argumentos: 
índice y un elemento para insertar.
"""
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)

#?Removing Items from a List
    #The remove method removes a specified item from a list
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']

#?Removing Items Using Pop
    #El método pop() elimina el índice especificado (o el último elemento si no se especifica el índice):
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']

