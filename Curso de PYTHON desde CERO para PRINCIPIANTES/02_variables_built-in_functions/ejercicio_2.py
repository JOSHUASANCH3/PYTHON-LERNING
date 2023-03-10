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
    total_variable = num_one + num_two;
    print(total_variable);

    #2. Reste num_two de num_one y asigne el valor a una variable diff
    variable_diff = num_one - num_two;
    print(variable_diff);

    #3. Multiplique num_two y num_one y asigne el valor a un producto variable
    producto_variable = num_one * num_two;
    print(producto_variable);

    #4. Divide num_one por num_two y asigna el valor a una división variable
    división_variable = num_one / num_two;
    print(división_variable);

    #5. Use la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un residuo variable
    residuo_variable = num_one % num_two;
    print(residuo_variable);

    #6. Calcula num_one a la potencia de num_two y asigna el valor a una variable exp
    variable_exp = num_one ** num_two;
    print(variable_exp);

    #7. Encuentra la división de piso de num_one por num_two y asigna el valor a una variable floor_division
    floor_division = num_one // num_two;
    print(floor_division);

#5. El radio de un círculo es de 30 metros.
    r = 30; #radio del circulo
    pi = 3.1416;

    #1. Calcule el área de un círculo y asigne el valor a una variable con el nombre de *area_of_circle*
    area_of_circle = pi * (pow(r,2));

    #2. Calcule la circunferencia de un círculo y asigne el valor a un nombre de variable de *circum_of_circle*
    circum_of_circle = 2*pi*r;

    #3. Tome el radio como entrada del usuario y calcule el área.
    area_user = input("Digite el area del cirulo : ");
    area_of_circle = pi * pow(area_user,2);
    print("El area del circulo es :",area_of_circle);

#6. Use la función de entrada integrada para obtener el nombre, el apellido, el país y la edad de un usuario y almacene el valor en sus nombres de variables correspondientes
    name = input("Escriba su nombre: ");
    last_name = input("Escriba su apellido: ");
    country = input("Escriba su pais: ");
    year_old = input("Escriba su edad: ");
    print("Sus datos son: ", name, last_name, country, year_old);

#7. Ejecute la ayuda ('palabras clave') en el shell de Python o en su archivo para verificar las palabras reservadas o las palabras clave de Python
    