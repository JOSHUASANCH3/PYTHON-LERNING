
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



