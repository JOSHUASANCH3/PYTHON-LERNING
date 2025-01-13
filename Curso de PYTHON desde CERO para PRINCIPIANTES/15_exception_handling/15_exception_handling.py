##Haciendo expeciones
numberOne = 1
numberTwo = 2
numberTwo = "1"

##print(numberOne + numberTwo)

"""
De esta forma manual se puede verificar los tipos de datos de una variable
if type(numberTwo) == int:
    print(numberOne + numberTwo)
else:
    print("No se cumplio")
"""
## try except
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

## try except else
numberOne = 1
numberTwo = 2
# numberTwo = "1"
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    ##Esto se ejecuta sino se produce una excepcion
    print("La ejecucion continua")

## try except else finally
numberOne = 1
numberTwo = 2
##numberTwo = "1"
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  ##Opcional
    ##Esto se ejecuta sino se produce una excepcion
    print("La ejecucion continua oorrectamente")
finally:  ##Opcional
    ##Se ejecuta siempre
    print("La ejecucion continua")

##Excepciones por tipo
numberOne = 1
numberTwo = 2
numberTwo = "1"
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")

##Captura de la informacion de la excepcion
numberOne = 1
numberTwo = 2
numberTwo = "1"
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_ramdon_error_name:
    print(my_ramdon_error_name)
