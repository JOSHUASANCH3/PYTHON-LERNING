### File Handling ###
import os

#! .txt File\
##? w+: Abre el archivo para escritura y lectura, pero borra el contenido existente si ya existe.
##? r+: Abre para lectura y escritura sin borrar el contenido.
##? a+: Abre para añadir contenido, pero permite leer también.
file_path_txt = "Curso de PYTHON desde CERO para INTERMEDIO/File_Handling/my_file.txt"
## txt_file = open(file_path_txt, "w+")
## print(txt_file.read()) ## Lee todo el fichero
## print(txt_file.read(10))  ## Lee los primeros 10 caracteres del fuchero
## print(txt_file.readline()) ## Lee una linea completa del fichero
## print(txt_file.readline()) ## Lee la segun linea.
## print(txt_file.readlines())  ##Lee todas las lineas y las junta en un listado
## Vuelve al inicio del archivo para leer
## txt_file.seek(0)

##? Se cierra el txt
## txt_file.close()

##? Se va eliominar el fichero
## os.remove(file_path_txt)

if os.path.exists(file_path_txt):
    print(f"El archivo '{file_path_txt}' ya existe. No se sobreescribirá.\n")
else:
    ##? with: se usa para manejar el archivo y lo cierra correctamente
    with open(file_path_txt, "w+") as txt_file_write:
        txt_file_write.write(
            "Mi nombre es Joshua\nMi apellido es Sanchez\nMi edad es 25 años\nMi ciudad natal es Managua\nMi lengua de programacion preferido es Python\n"
        )
        print(f"Archivo '{file_path_txt}' creado exitosamente.")

#! Se imprime el resultado del archivo para saber si se escriio
with open(file_path_txt, "r+") as txt_file_read:
    for line in txt_file_read.readlines():
        print(line)

## Archivos JSON
import json

##? Colocamos la ruta en una varible
file_path_json = "Curso de PYTHON desde CERO para INTERMEDIO/File_Handling/my_file.json"
json_file = open(file_path_json, "w+")  # ? Abrimos el archivo, si no existe lo creamos

json_test = {
    "name": "Joshua",
    "surname": "Sanchez",
    "age": 35,
    "languages": ["Python", "CSS", "HTML", "MongoBD"],
    "phrase": "Hello World",
}

##? json.dump() de Python sirve para convertir objetos de Python en datos JSON.
json.dump(json_test, json_file, indent=2)
## json.dump(json_test, json_file, indent=2) #? Crea otra vez el archivo apartir del ultimo fichero modificado,
##? pero genera un fallo ya que no genera los corchetes y la coma para que el JSON sea tangible

## Cerramos el archivo
json_file.close()

with open(file_path_json) as my_other_file:
    for line in my_other_file.readlines():
        print(line)

##? Se eliminara el archivo
## os.remove(file_path_json)

##? Para saber si hay un fichero y datos o crearlos
if os.path.exists(file_path_json):
    print(f"El archivo '{file_path_json}' ya existe. No se sobreescribirá.\n")
else:
    ##? with: se usa para manejar el archivo y lo cierra correctamente
    with open(file_path_json, "w+") as json_file_write:
        json.dump(json_test, json_file_write, indent=2)
        print(f"Archivo '{file_path_json}' creado exitosamente.")


## Pasar un JSON a un diccionario
## Se puede usar el JSON como un diccionario para obtener sus datos de manera mas eficienciente
json_dict = json.load(open(file_path_json))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])
