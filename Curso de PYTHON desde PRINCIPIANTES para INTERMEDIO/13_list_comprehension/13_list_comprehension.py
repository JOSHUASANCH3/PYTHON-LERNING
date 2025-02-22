# ? List comprehension
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]  ## Se crea una lista
print(my_original_list)

my_list = [
    i for i in range()
]  ## range se crea una lista dentro del rango del valor que le asignemos
print(my_list)

my_range = range(8)
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
