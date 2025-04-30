import os
import time

# ? Importamos la libreria de pandas y asignamos una alias especifico 'pd'
import pandas as pd

# ? Se crea una variable que contenga el path del archivo
path_file_access = "Curso de PYTHON para BLUIDING-APPS/Constuyendo 10 Aplicaciones en 10 dias/_example_file.txt"

while True:
    if os.path.exists(path_file_access):
        # ? with: se usa para manejar el archivo y lo cierra correctamente
        with open(path_file_access, "r+") as txt_file_read:
            # for line in txt_file_read.readlines():
            # print(line + "/n")
            data = pd.read_csv(txt_file_read, sep=",")
            # print(data)
            # si solo queremos los datos de una sola columna
            print(data.mean()["st1"])
    else:
        print(f"El archivo '{path_file_access}' ya existe. No se sobreescribirá./n")
        break
    time.sleep(10)
