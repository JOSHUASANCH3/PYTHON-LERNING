##funciones


def my_function():
    print("Esto es una funcion")


my_function()


##segunda funcion
def sum_two_valvues(first_number: int, second_number):
    print(first_number + second_number)


sum_two_valvues(5, 7)
sum_two_valvues(1234, 4321)
##sum_two_valvues("5", "7") -> aqui peta por que los datos son strings
sum_two_valvues(1.4, 5.2)


##tercera funcion
def sum_two_valvues_with_values(first_number, second_number):
    my_sum = first_number + second_number
    return my_sum


my_result = sum_two_valvues_with_values(20, 5)
print(my_result)


##tercera funcion
def print_name(name, sur_name):
    print(f"{name} {sur_name}")


print_name("Joshua", "Snachez")
print_name(sur_name="Sanchez", name="Joshua")


##alternativa
def print_name_with_default(name, sur_name, alias="sin alias"):
    print(f"{name} {sur_name} {alias}")


print_name_with_default("Joshua", "Snachez", "@JOSHUASANCH3")
print_name_with_default("Joshua", "Snachez")


##Cuarta funcion
def print_texts(*texts):
    for text in texts:
        print(text)


print_texts("Hola", "Muundo")
print("Hola")


##Quinta funcion, Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    def is_divisible_by_2_or_3(n):
        return n % 2 == 0 or n % 3 == 0

    if n <= 3:
        return n > 1
    if is_divisible_by_2_or_3(n):
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


# Example usage:
print(is_prime(2))  # True
print(is_prime(17))  # True
print(is_prime(20))  # False
