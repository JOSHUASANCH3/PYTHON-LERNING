### File Handling ###
import os

## .txt File
txt_file = open(
    "Curso de PYTHON desde CERO para INTERMEDIO/File_Handling/my_file.txt", "w+"
)  ## r+, nos permite Leer y Escribir en el fichero
## print(txt_file.read()) ## Lee todo el fichero
## print(txt_file.read(10))  ## Lee los primeros 10 caracteres del fuchero
## print(txt_file.readline()) ## Lee una linea completa del fichero
## print(txt_file.readline()) ## Lee la segun linea.
print(txt_file.readlines())  ##Lee todas las lineas y las junta en un listado

##Forma Alterna de leer todos los datos con readLines()
for line in txt_file.readlines():
    print(line)

##Se cierra el txt
txt_file.close()

## Se va eliominar el fichero
os.remove("Curso de PYTHON desde CERO para INTERMEDIO/File_Handling/my_file.txt")

## Se va crear un nuevo fichero con la misma actualizacion
txt_file = open(
    "Curso de PYTHON desde CERO para INTERMEDIO/File_Handling/my_file.txt", "w+"
)
txt_file.write(
    "Mi nombre es Joshua\nMi apellido es Sanchez\nMi edad es 25 años\nMi ciudad natal es Managua\nMi lengua de programacion preferido es Python"
)
## Se lee el archivo de nuevo linea por linea
for line in txt_file.readlines():
    print(line)

txt_file.write("\nTambien me gusta HTML")
print(txt_file.readline())

##Se cierra el fichero
txt_file.close()
