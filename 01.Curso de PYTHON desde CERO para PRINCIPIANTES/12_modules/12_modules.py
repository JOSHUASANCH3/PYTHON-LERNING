##Modulos
import my_module  # #Se importa una libreria

my_module.sum_functions(3, 2, 1)
my_module.printValue("Hola python")

##importar una funcion especifica del fichero
from my_module import sum_functions

##se importa la funcion
sum_functions(3, 2, 1)

##importa la biblioteca math
import math

print(math.pi)

##renombrar una variable a un valor dentro de un modulo
from math import pi as PI_VALUE

print(PI_VALUE)
