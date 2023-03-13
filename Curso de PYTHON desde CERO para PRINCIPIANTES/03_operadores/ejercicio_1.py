# 1. Declara tu edad como variable entera
int_edad = 24
# 2. Declara tu altura como una variable flotante
float_altura = 1.75
# 3. Declarar una variable que almacene un número complejo
complex_numero = 4 + 5j
# 4. Escriba un script que solicite al usuario que ingrese la base y la altura del triángulo y calcule el área de este triángulo (área = 0,5 x b x h).
"""
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
    """

base_triangulo = int(input("Ingrese la base del triangulo: "))
altura_triangulo = int(input("Ingrese la altura del triangulo: "))
area_triangulo = (base_triangulo * altura_triangulo)/2
print("El area del triangulo es: ", area_triangulo)

# 5. Escriba un script que solicite al usuario que ingrese el lado a, el lado b y el lado c del triángulo.
# Calcula el perímetro del triángulo (perímetro = a + b + c).
"""
    Enter side a: 5
    Enter side b: 4
    Enter side c: 3
    The perimeter of the triangle is 12
    """
print("Ingrese los datos A, B, C, para \n para calcular el area de un triangulo")
base_a = int(input("Ingrese la base A: "))
base_b = int(input("Ingrese la base B: "))
base_c = int(input("Ingrese la base C: "))
perimetro_triangulo = base_a + base_b + base_c
print("El perimetro del triangulo es: ", perimetro_triangulo)

# 6. Obtenga la longitud y el ancho de un rectángulo usando el indicador.
# Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho))
largo_triangulo, ancho_triangulo  = 10, 20
area_triangulo = largo_triangulo * ancho_triangulo
print("E area del tringulo es: ",area_triangulo)
perimetro_triangulo = 2 * (largo_triangulo, ancho_triangulo)
print("El perimetro del triangulo es: ",perimetro_triangulo)

# 7. Obtenga el radio de un círculo usando el indicador. 
# Calcula el área (área = pi x r x r) y la circunferencia (c = 2 x pi x r) donde pi = 3,14.
pi_circulo, r_circulo, r_circulo_2 = 3.1416 , 10, 20
area_circulo = pi_circulo * r_circulo_1 * r_circulo_2
print("El area del circulo: ",area_circulo)
circunferencia_circulo = 2 * pi_circulo * r_circulo_1
print("La circuferencia del circulo: ",circunferencia_circulo)

# 8. Calcule la pendiente, la intersección x y la intersección y de y = 2x -2
"""
0 = 2x - 2
2x = 2
x = 1
"""
def line(x):
    return 2*x - 2

# Para obtener la intersección en x
interseccion_x = 1

# Para obtener la intersección en y
interseccion_y = line(0)

# Para obtener la pendiente
pendiente = 2

print("La intersección en x es:", interseccion_x)
print("La intersección en y es:", interseccion_y)
print("La pendiente es:", pendiente)

# 9. La pendiente es (m = y2-y1/x2-x1). 
# Encuentre la pendiente y la distancia euclidiana entre el punto (2, 2) y el punto (6,10).
"""
Para encontrar la pendiente de la recta que une los puntos (2,2) y (6,10), primero necesitamos identificar los valores de x1, y1, x2 e y2:

x1 = 2
y1 = 2
x2 = 6
y2 = 10

Entonces, podemos aplicar la fórmula de la pendiente:

m = (y2 - y1) / (x2 - x1)
m = (10 - 2) / (6 - 2)
m = 8 / 4
m = 2

Por lo tanto, la pendiente de la recta que une los puntos (2,2) y (6,10) es de 2.

Para encontrar la distancia euclidiana entre los dos puntos, podemos aplicar la fórmula:

d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
d = sqrt((6 - 2)^2 + (10 - 2)^2)
d = sqrt(4^2 + 8^2)
d = sqrt(16 + 64)
d = sqrt(80)
d = 8.94

#Por lo tanto, la distancia euclidiana entre los puntos (2,2) y (6,10) es de aproximadamente 8.94 unidades.
"""
#Resolviendo el ejemplo
import math

# Definimos los puntos
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calculamos la pendiente
m = (y2 - y1) / (x2 - x1)
print("La pendiente de la recta que une los puntos es:", m)

# Calculamos la distancia euclidiana
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("La distancia euclidiana entre los puntos es:", d)


# 10. Compara las pendientes en las tareas 8 y 9.
"""YA"""
# 11. Calcula el valor de y, con la ecuacion y = x^2 + 6x + 9. 
# Trate de usar diferentes valores de x y descubra en qué valor de (x),(y) será 0.  
"""
Para calcular el valor de y para una determinada x en la ecuación y = x^2 + 6x + 9, simplemente debemos sustituir el valor de x en la ecuación y resolver para y. Por ejemplo, si queremos calcular el valor de y para x = 2, podemos hacer lo siguiente:

y = 2^2 + 6(2) + 9
y = 4 + 12 + 9
y = 25

Por lo tanto, cuando x = 2, y = 25.

Para encontrar en qué valor de x e y la ecuación será igual a cero, debemos resolver la ecuación cuadrática:

x^2 + 6x + 9 = 0

Podemos resolver esta ecuación utilizando la fórmula cuadrática:

x = (-b ± sqrt(b^2 - 4ac)) / 2a

Donde a, b y c son los coeficientes de la ecuación cuadrática (ax^2 + bx + c). En este caso, a = 1, b = 6 y c = 9. Entonces, podemos sustituir estos valores en la fórmula cuadrática:

x = (-6 ± sqrt(6^2 - 4(1)(9))) / 2(1)
x = (-6 ± sqrt(36 - 36)) / 2
x = -3

Por lo tanto, cuando x = -3, la ecuación es igual a cero. Podemos comprobarlo sustituyendo x = -3 en la ecuación original:

y = (-3)^2 + 6(-3) + 9
y = 9 - 18 + 9
y = 0

Por lo tanto, cuando x = -3, y = 0.
"""
# Definimos la ecuación
def ecuacion(x):
    return x**2 + 6*x + 9

# Calculamos el valor de y para diferentes valores de x
print("Para x = 2, y =", ecuacion(2))
print("Para x = 3, y =", ecuacion(3))
print("Para x = -1, y =", ecuacion(-1))

# Resolvemos la ecuación para encontrar en qué valor de x e y es igual a cero
a, b, c = 1, 6, 9
x = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
print("Cuando x =", x, ", y =", ecuacion(x))

# 12. Encuentre la longitud de 'python' y 'dragon' y haga una declaración de comparación falsa.
word1 = 'python'
word2 = 'dragon'

# Longitud de las palabras
len_word1 = len(word1)
len_word2 = len(word2)

# Comparación falsa
if len_word1 == len_word2 + 1:
    print("La longitud de 'python' es:", len_word1)
    print("La longitud de 'dragon' es:", len_word2)
    print("La declaración de comparación falsa es verdadera.")
else:
    print("La longitud de 'python' es:", len_word1)
    print("La longitud de 'dragon' es:", len_word2)
    print("La declaración de comparación falsa es falsa.")

# 13. Use un operador para verificar si 'on' se encuentra tanto en 'python' como en 'dragon'.
word1 = 'python'
word2 = 'dragon'

# Verificar si 'on' está en ambas palabras
if 'on' in word1 and 'on' in word2:
    print("'on' se encuentra en ambas palabras.")
else:
    print("'on' no se encuentra en ambas palabras.")

# 14. Espero que este curso no esté lleno de jerga. Use el operador in para verificar si hay jerga en la oración.
# a?

# 15. No hay 'on' tanto en dragon como en python.
# no

# 16. Encuentre la longitud del texto python y convierta el valor en flotante y conviértalo en una cadena
float_len_word1 = float(len_word1);
str_len_word1 = str(float_len_word1);

# 17. Los números pares son divisibles por 2 y el resto es cero. ¿Cómo verifica si un número es par o no usando python?
# 18. Verifique si la división del piso de 7 por 3 es igual al valor int convertido de 2.7.
# 19. Compruebe si el tipo de '10' es igual al tipo de 10
# 20. Comprueba si int('9.8') es igual a 10
# 21. Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora. ¿Calcular el salario de la persona?.
"""
    Enter hours: 40
    Enter rate per hour: 28
    Your weekly earning is 1120
    """
# 22. Escriba un script que solicite al usuario que ingrese el número de años. Calcular el número de segundos que puede vivir una persona. Supongamos que una persona puede vivir cien años.
"""
    Enter number of years you have lived: 100
    You have lived for 3153600000 seconds.
    """

# 23. Escriba un script de Python que muestre la siguiente tabla.
"""
    1 1 1 1 1
    2 1 2 4 8
    3 1 3 9 27
    4 1 4 16 64
    5 1 5 25 125
    """
