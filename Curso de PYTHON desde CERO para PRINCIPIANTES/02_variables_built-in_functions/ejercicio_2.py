#Ejercicio 2
#1. Verifique el tipo de datos de todas sus variables usando la función incorporada type()
first_name = "Germán";       # str
last_name = "Sánchez";       # str
country = "Nicaragua";       # str
city= 'Helsinki';            # str
age = 250;                   # int, it is not my real age, don't worry about it
    #Confirmando los tipos de datos
print(type('Asabeneh'));     # str
print(type(first_name));     # str
print(type(250));            # int
print(type(age));            #int

#2. Usando la función integrada *len()* , encuentre la longitud de su nombre
print("Cantidad del nombre: ",len(first_name)); #Cantidad de letras
print("Cantidad del apellido: ",len(last_name));

#3. Compara la longitud de tu nombre y tu apellido
if(len(first_name) > len(last_name)){ #comparacion de quien tiene mas letras
    print("Mi primer nombre es mayor que mi apellido");    
}else{
    print("Mi apellido es mayor que mi nombre");
}

#4. Declare 5 como num_one y 4 como num_two
    num_one, num_two = 5, 4;
    #1. Sume num_one y num_two y asigne el valor a un total variable
    #2. Reste num_two de num_one y asigne el valor a una variable diff
    #3. Multiplique num_two y num_one y asigne el valor a un producto variable
    #4. Divide num_one por num_two y asigna el valor a una división variable
    #5. Use la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un residuo variable
    #6. Calcula num_one a la potencia de num_two y asigna el valor a una variable exp
    #7. Encuentra la división de piso de num_one por num_two y asigna el valor a una variable floor_division
#5. El radio de un círculo es de 30 metros.
    #1. Calcule el área de un círculo y asigne el valor a una variable con el nombre de *area_of_circle*
    #2. Calcule la circunferencia de un círculo y asigne el valor a un nombre de variable de *circum_of_circle*
    #3. Tome el radio como entrada del usuario y calcule el área.
#6. Use la función de entrada integrada para obtener el nombre, el apellido, el país y la edad de un usuario y almacene el valor en sus nombres de variables correspondientes
#7. Ejecute la ayuda ('palabras clave') en el shell de Python o en su archivo para verificar las palabras reservadas o las palabras clave de Python