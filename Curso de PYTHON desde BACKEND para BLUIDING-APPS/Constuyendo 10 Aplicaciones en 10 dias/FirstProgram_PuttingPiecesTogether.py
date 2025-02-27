### Repetir un primer programa
# ? Importamos la libreria de expresiones regulares
import re

# ? Se crea una variable para obtener los datos
say_someting = None


# ? Se creara una funciona para formatear las oraciones
def formater_sentence(formater_word):
    # Lista de palabras que indican una pregunta
    word_question = [
        "qué",
        "que",
        "cómo",
        "como",
        "dónde",
        "donde",
        "cuándo",
        "por qué",
        "por que",
        "quién",
        "quien",
        "cuál",
        "cual",
    ]

    # Capitalizar la primera letra
    formater_word = formater_word.capitalize()

    # Vamos a verificar si la oracion tiene ? y .
    formater_word = re.sub(r"[.?]", "", formater_word)

    # Verificar si es una pregunta
    is_question = any(f_word in formater_word.lower() for f_word in word_question)

    # Agregar signos de puntuación
    if is_question:
        formater_word = f"{formater_word}?"  # Agrega signos de interrogación
    else:
        formater_word = f"{formater_word}."  # Agrega un punto final

    return formater_word


# ? Se crea una funcion para almacenar datos mediante una lista
my_list = []


def save_sentence(save_list):
    my_list = []
    my_list.append(save_list)


# ?Se crea un loop para mantener la secuencia del programa
while True:
    say_someting = input("Say something: ")
    # Primera verificacion que 'Say Something' es /end
    if say_someting == "/end":
        for element in my_list:
            print(element)
        break
    # Si Say Something es /end se termina el programa
    elif say_someting != "/end":
        sentence_correct = formater_sentence(say_someting)
        my_list.append(sentence_correct)
    else:
        print("Opcion Incorrecta")
