# ? List comprehension
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]  ## Se crea una lista
print(my_original_list)

my_list = [
    i for i in range(6)
]  ## range se crea una lista dentro del rango del valor que le asignemos
print(my_list)

my_range = 8  # el valor de my_range solo se puede definir por un numero entero
my_list = [
    i for i in range(my_range)
]  ## Nos sirve para crear una lista de datos que necesitemos
print(my_list)

my_list = [i + 1 for i in range(my_range)]  ## Se suma +1 a cada valor de lista
print(my_list)

my_list = [
    i * 2 for i in range(my_range)  ## Se multiplica el doble a cada valor de lista
]
print(my_list)

my_list = [i * i for i in range(my_range)]  ## Se potencia cada valor de lista
print(my_list)


def sum_five(number):
    return number + 5


my_list = [sum_five(i) for i in range(my_range)]  ## Se potencia cada valor de lista
print(my_list)

## Una forma mas eficiente de utilizar las listas de comprension
temps = [221, 234, 340, 230]
new_temps = [temp / 10 for temp in temps]
print(new_temps)

##Para evitar cierto valor que esta en la lista
temps = [221, 234, 340, -9999, 230]
new_temps = [temp / 10 for temp in temps if temps != -9999]
print(new_temps)

##Para evitar cierto valor que esta en la lista
temps = [221, 234, 340, -9999, 230]
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]
print(new_temps)
