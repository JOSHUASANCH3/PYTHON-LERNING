"""
#1 EL FAMOSO "FIZZ BUZZ"
 * Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
    #? - Múltiplos de 3 por la palabra "fizz".
    #? - Múltiplos de 5 por la palabra "buzz".
    #? - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def fizzbuzz():
    for index in range(1, 101):
        if index % 3 and index % 5 == 0:
            ##Para saber si un numero es multiplo de 3 y 5, es que su modulo es 0
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)


fizzbuzz()

"""
#2 ¿ES UN ANAGRAMA?
 * Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
    #? - Un Anagrama consiste en formar una palabra reordenando TODAS
    #? - las letras de otra palabra inicial.
    #? - NO hace falta comprobar que ambas palabras existan.
    #? - Dos palabras exactamente iguales no son anagrama.
"""


def is_anagram(word_one, word_two):
    ##Aqui verifica si es la misma la palabra
    if word_one.lower() == word_two.lower():
        return False
    ##Aqui ordena y crea una lista de caracteres y verifica si todas son las mismas
    return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram("Amor", "Roma"))
